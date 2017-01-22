# Author: Francesco Vannini
# Company: Pi Supply

import alsaaudio
import RPi.GPIO as GPIO
from time import sleep
import getopt
import sys

class Rotary:
    CLOCKWISE = 0
    ANTICLOCKWISE = 1

    def __init__(self, clockPin, dataPin, buttonPin,
                 rotaryCallback, buttonCallback):
        # persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.buttonPin = buttonPin
        self.rotaryCallback = rotaryCallback
        self.buttonCallback = buttonCallback

        # setup pins
        GPIO.setup(clockPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # All pins are pull up because both
        GPIO.setup(dataPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # the encoder and the button
        GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # will be connected to Ground

    def start(self):
        GPIO.add_event_detect(self.clockPin,
                              GPIO.FALLING,
                              callback=self._clockCallback,
                              bouncetime=50)
        GPIO.add_event_detect(self.buttonPin,
                              GPIO.FALLING,
                              callback=self._switchCallback,
                              bouncetime=300)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)
        GPIO.remove_event_detect(self.buttonPin)

    def _clockCallback(self, pin):
        if GPIO.input(self.clockPin) == 0:
            data = GPIO.input(self.dataPin)
            if data == 1:
                self.rotaryCallback(self.ANTICLOCKWISE)
            else:
                self.rotaryCallback(self.CLOCKWISE)

    def _switchCallback(self, pin):
        if GPIO.input(self.buttonPin) == 0:
            self.buttonCallback()

class EasyMixer:

    def __init__(self, start_vol, vol_inc, clk, dt, btn,):
        self.startvol = start_vol
        self.volinc = vol_inc
        self.isMute = False
        self.clk = clk # First rotary pin
        self.dt = dt # Second rotary pin
        self.btn = btn # Button pin
        self.mixer = alsaaudio.Mixer('Digital')
        self.rotary = Rotary(self.clk, self.dt, self.btn, self.rotarychange, self.buttonpressed)

    def getmute(self):
        self.isMute = self.mixer.getmute()[0]
        return self.isMute

    def setmute(self, mute):
        self.mixer.setmute(mute)

    def getvolume(self):
        return self.mixer.getvolume()[0]

    def setvolume(self, volume):
        self.mixer.setvolume(volume)

    def upvolume(self):
        if (self.getvolume() + self.volinc) <= 100:
            self.setvolume(self.getvolume() + self.volinc)

    def downvolume(self):
        if (self.getvolume() - self.volinc) >= 0:
            self.setvolume(self.getvolume() - self.volinc)

    def rotarychange(self, direction):
        if not self.getmute():  # Is the audio muted?
            if direction:
                self.upvolume() # Increase the volume
            else:
                self.downvolume() # Decrease the volume
            print "Volume: " + str(self.getvolume())

    def buttonpressed(self):
        if (self.getmute()):  # Is the audio muted?
            self.setvolume(self.getvolume())  # Applies the last known value of volume (before entering mute)
            self.setmute(0)  # Unmute the sound
            print "Unmuted"
        else:
            self.setmute(1)  # Mute the audio
            print "Muted"

    def start(self):
        self.mixer.setvolume(self.startvol) # Set mixer volume to start volume
        self.rotary.start()

    def stop(self):
        self.rotary.stop()

def usage():
    print 'Usage: \tjb_rotary [-sirbv]\n' + \
          '\tjb_rotary {-h|--help}         Script usage information\n' +\
          '\n' +\
          '\t-s --startvol    start volume level\n' +\
          '\t-i --volinc      volume increments/decrements\n' +\
          '\t-r --rotary      rotary encoder pins\n' +\
          '\t-b --button      button pin'

# main

# Defaults
start_volume = 0 # Starting volume
volume_increments = 1 # Step for volume increments
rotary_pins = [16,18] # Rotary encoder pin
button_pin = 10  # Button pin

# Script arguments
try:
    options, remainder  = getopt.getopt(sys.argv[1:], "h:s:i:r:b:", ['help', 'startvol', 'volinc', 'rotary', 'button',])
except getopt.GetoptError as err:
    print str(err)
    usage()
    sys.exit(2)

for opt, arg in options:
    if opt in ('-s', '--startvol'):
        start_volume = int(arg)
    elif opt in ('-i', '--volinc'):
        volume_increments = int(arg)
    elif opt in ('-r', '--rotary'):
        rotary_pins = arg.split(',')
    elif opt in ('-b', '--button'):
        button_pin = int(arg)
    elif opt in ('-h', '--help'):
        usage()
        sys.exit()
    else:
        assert False, "unhandled option"

GPIO.setmode(GPIO.BOARD) # Set the GPIO with pin numbering

easy_mixer = EasyMixer(start_volume,volume_increments, int(rotary_pins[0]), int(rotary_pins[1]), button_pin) # New mixer instantiation

easy_mixer.start() # Start mixer and rotary encoder

# Wait for something to happen
try:
    while True:
        sleep(0.1)
finally:
    easy_mixer.stop()
    GPIO.cleanup()
