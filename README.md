# Simple evdev Keylogger

This repository provides a Python-based keylogger that captures keystrokes from `/dev/input/event3` and logs them in plain text to `/home/hp/g/keys.log`.

# Configuration

DEVICE: If your keyboard is not /dev/input/event3, edit keylogger.py and change the DEVICE variable.

Log File: Defaults to /home/hp/g/keys.log.

## Installation & Uninstallation

```bash
cd keylogger
sudo ./install.sh

cd keylogger
sudo ./uninstall.sh