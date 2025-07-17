#!/usr/bin/env bash
set -e

# Stop and disable service
systemctl stop keylogger.service
systemctl disable keylogger.service

# Remove files
rm -f /home/hp/g/keylogger.py
rm -f /etc/systemd/system/keylogger.service
rm -f /home/hp/g/keys.log

systemctl daemon-reload

echo "Keylogger uninstalled. Cleanup complete."