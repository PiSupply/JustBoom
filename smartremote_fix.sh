#!/usr/bin/env bash

# Create a file to modify the value corresponding to the OK and Menu button
cat > /storage/.config/hwdb.d/70-local-keyboard.hwdb << EOF
evdev:input:b0003v2252p0120*
 KEYBOARD_KEY_c0041=enter
 KEYBOARD_KEY_c0040=c
EOF

# Update the hardware database
udevadm hwdb --update && udevadm trigger -s input
