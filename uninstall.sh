#!/usr/bin/env bash

#Check if script is being run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

if [ ! $? = 0 ]; then
   exit 1
else

   systemctl stop jb-rotary.service
   systemctl disable /etc/systemd/jb-rotary.service

   rm /opt/justboom/jb-rotary.py 
   rm /opt/justboom -d
   rm /etc/systemd/system/jb-rotary.service

   whiptail --title "Uninstall complete" --msgbox "JustBoom Rotary Volume Control uninstall complete. You are safe to remove the folder JustBoom." 8 78
fi
