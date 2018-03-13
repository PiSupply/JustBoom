#!/usr/bin/env bash

#Check if script is being run as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

if [ ! $? = 0 ]; then
    exit 1
else
    #Installs packages which might be missing
    apt-get install git whiptail -y
    apt-get install python-alsaaudio -y
    apt-get install python-rpi.gpio -y

    JustBoomDir="JustBoom"
    if [ -d "$JustBoomDir" ]; then
        whiptail --title "Installation aborted" --msgbox "$JustBoomDir already exists, please remove it and restart the installation" 8 78
        exit
    fi

    git clone https://github.com/PiSupply/JustBoom.git
    mkdir /opt/justboom
    cp $JustBoomDir/jb-rotary.py /opt/justboom
    cp $JustBoomDir/jb-rotary.service /usr/lib/systemd/system
    cp $JustBoomDir/jb-rotary.timer /usr/lib/systemd/system

    systemctl daemon-reload
    systemctl disable jb-rotary.service
    systemctl enable jb-rotary.timer
    systemctl start jb-rotary.timer
whiptail --title "Installation complete" --msgbox "The JustBoom Rotary Volume Control installation complete. Please reboot your Raspberry Pi now." 8 78
fi
