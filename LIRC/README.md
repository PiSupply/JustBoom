# LIRC configurations

In this folder you can find a generic lircd.conf which is compatible with the JustBoom Player, Volumio and Moode Audio. You can read the [full tutorial](https://www.justboom.co/tutorials/configure-justboom-ir-remote-lirc/) on our site.

## Kodi
You can also find configuration files for LibreELEC and for OSMC. The OSMC one also comes with a PNG which is used by the OS to show the remote in My OSMC -> Remotes.
Both these files have been set with the KEY_ map names compatible with Kodi.

### LibreELEC
```bash
cp lircd.conf /storage/.config/
```

```bash
mount -o remount,rw /flash
nano /flash/config.txt
```

add

```
# Enable the lirc-rpi module
dtoverlay=lirc-rpi
 
# Override the defaults for the lirc-rpi module
dtparam=gpio_in_pin=25
```
save and reboot

```bash
mount -o remount,ro /flash
reboot
```

### OSMC

```bash
nano /boot/config.txt
```

add

```
# Enable the lirc-rpi module
dtoverlay=lirc-rpi
 
# Override the defaults for the lirc-rpi module
dtparam=gpio_in_pin=25
```

in My OSMC -> Remotes
Browse and choose the folder in which you have saved these two files

justboom-ir-remote-lircd.conf
justboom-ir-remote-lircd.png

reboot the OS



