# JustBoom
## ALSA file for Surround Systems
JustBoomDigi.conf enables passthrough DTS for surround systems. Needs to be saved under /usr/share/alsa/cards

## Rotary encoder volume control
jb-rotary enables control of volume level via the rotary encoder and mute/unmute function via its push button.
###Installation
1. Login via SSH or via the console.
2. Run the following command and the JustBoom rotary and push button code will be configured and installed: 
```bash
curl -sSL https://pisupp.ly/jb-rotarycode | sudo bash
```
###Usage
The default settings for the script are:
* Start Volume = 0
* Volume increment/decrement steps = 1
* Rotary pins = 16,18 (Board notation)
* Button pin = 10 (Board notation)

Script usage:
```
Usage:  jb_rotary [-sirbv]
        jb_rotary {-h|--help}         Script usage information

        -s --startvol    start volume level
        -i --volinc      volume increments/decrements
        -r --rotary      rotary encoder pins
        -b --button      button pin
```
Example:

```
python jb-rotary -s 20 -i 5       Changes the starting volume and step increments
python jb-rotary -r 19,21 -b 15   Remaps the rotary and the button pins
```
Note that the default setting for the button requires that you disable the onboard UART. This is mostly required when using the rotary encoder with the JustBoom Amp HAT via the P2 connector. [Check our main site JustBoom.co for the full pinout](https://www.justboom.co/technical-guides/boards-pinout/).

### Disable the UART on Raspberry Pi Zero, A+, B+ and 2B
on the command line execute these two commands:
``` bash
sudo systemctl stop serial-getty@ttyAMA0.service
sudo systemctl disable serial-getty@ttyAMA0.service
```
reboot the system.

### Disable the UART on Raspberry Pi 3B and Raspberry Pi Zero W
on the command line execute these two commands:
``` bash
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
```
and remove the following line from /boot/cmdline.txt
```
console=serial0,115200
```
reboot the system

### Wiring
Both the rotary pins and the button are configured to pull down. For example in the default configuration the pins will have to be connected as follows:
```
Rotary Left pin   -> pin 16
Rotary Middle pin -> GND (pin 14)
Rotary Right pin  -> pin 18

Button one pin    -> pin 10
Button other pin  -> GND (pin 9)
```
If you are planning on installing the rotary encoder on the [JustBoom DAC HAT check the FAQ](https://www.justboom.co/faqs/#FAQ-6) on the website for more information.

## LIRC lircd.conf
This is the configuration file for the JustBoom IR Remote to be used in conjunction with LIRC.
A tutorial that guides you through the whole installation of LIRC and the remote configuration can be found via [this link](https://www.justboom.co/tutorials/configure-justboom-ir-remote-lirc/).

## Chips, I2C and Pinout
The pinout for the boards can be found on the [JustBoom website](https://www.justboom.co/technical-guides/boards-pinout/) or on [Pinout.xyz](https://pinout.xyz/boards#manufacturer=JustBoom)

This list shows the various chips used and the I2C address where applicable:
* Amp HAT - [TAS5756M](http://www.ti.com/product/TAS5756M) - 0x4D
* DAC HAT - [PCM5122](http://www.ti.com/product/PCM5122) - 0x4D
* Digi HAT - [WM8804G](http://www.alldatasheet.net/view.jsp?Searchword=WM8804G&sField=2) - 0x3B
* Amp Zero - [TAS5756M](http://www.ti.com/product/TAS5756M) - 0x4D
* DAC Zero - [PCM5121](http://www.ti.com/product/PCM5121) - 0x4D
* Digi Zero - [WM8804G](http://www.alldatasheet.net/view.jsp?Searchword=WM8804G&sField=2) - 0x3B
* Amp - [TPA3118D2](http://www.ti.com/product/TPA3118D2)
* DAC - [PCM5102A](http://www.ti.com/product/PCM5102A)
