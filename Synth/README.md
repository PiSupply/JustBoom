# Resources for JustBoom Synth

```
# Relevant MIDI Software list:
# http://tedfelix.com/linux/linux-midi.html

# Play midi file to output MIDI port 16:0
pmidi -p 16:0 click_on_off.mid
# To fined available port list un 
pmidi -l
# Alternatively
aplaymidi -p 16:0 Mozart_31.mid

#Test midi messages on rpi with receivemidi tool:
#https://github.com/gbevin/ReceiveMIDI
#build or download release for rpi: https://github.com/gbevin/ReceiveMIDI/releases

#Source code for making c programs around MIDI:
ftp://ftp.wayne.edu/ldp/en/MIDI-HOWTO/MIDI-HOWTO-single.html

# Synthesis with fluidsynth
# Play file
fluidsynth --audio-driver=alsa -o audio.alsa.device=hw:0 /usr/share/sounds/sf2/FluidR3_GM.sf2 song.mid
# Only run and wait for connections:
fluidsynth --audio-driver=alsa -o audio.alsa.device=hw:0 /usr/share/sounds/sf2/FluidR3_GM.sf2
# Run as server
fluidsynth --server --audio-driver=alsa -o audio.alsa.device=hw:0 /usr/share/sounds/sf2/FluidR3_GM.sf2

#ALSA sequencer connection manager
# https://linux.die.net/man/1/aconnect
# http://andrewdotni.ch/blog/2015/02/28/midi-synth-with-raspberry-p/
#show available input midi ports and software ports:
aconnect -o
#example connect sinth input MIDI port to fluidsynth software input port:
aconnect 16:0  128:0

# rtmidi development librariy c++ source
https://github.com/thestk/rtmidi
sudo apt-get install  librtaudio-dev  librtmidi-dev
# Example code:
http://www.music.mcgill.ca/~gary/rtmidi/
# compile program:
g++ -Wall -D__LINUX_ALSA__ -o rtmidiin rtmidiin.cpp -lasound -lpthread -lrtmidi
```
