# 🔑 Cross-Platform Python ShadowLogger

A simple keylogger written in Python that works on **Linux** (using `evdev`) and **Windows** (using `pynput`). It logs all keystrokes in plain text to a file and can auto-run on boot in Linux.

---

## 📁 Project Structure

```
keylogger/
├── .gitignore
├── keylogger.py          # Cross-platform logger script
├── keylogger.service     # systemd service for Linux
├── install.sh            # Linux installer
├── uninstall.sh          # Linux uninstaller
├── install.bat           # Windows installer
├── uninstall.bat         # Windows uninstaller
├── requirements.txt      # Required Python packages
└── README.md             # This file
```

---

## 💻 Features

- ✅ Logs alphanumeric keys and common symbols
- ✅ Supports both Linux and Windows
- ✅ Auto-starts at boot via systemd (Linux)
- ✅ Logs saved as plain text (`keylog.txt`)

---

## 📦 Installation

### 🐧 Linux

1. Change device path in `keylogger.py` if needed (`/dev/input/event3`)
2. Run the installer:

```bash
sudo ./install.sh
```

3. Logs will be saved to:

```
~/keylog.txt
```

> ✅ Automatically runs on system boot via `systemd`.

---

### 🪟 Windows

1. Install dependencies:

```bat
install.bat
```

2. Logs will be saved to:

```
C:\Users\<YourName>\keylog.txt
```

---

## ❌ Uninstallation

### Linux:
```bash
sudo ./uninstall.sh
```

### Windows:
```bat
uninstall.bat
```

---

## ⚙️ Configuration

- **Log file**: Defaults to `~/keylog.txt` (Linux) or `%USERPROFILE%\keylog.txt` (Windows)
- **Keyboard device**: Edit `DEVICE = '/dev/input/event3'` in `keylogger.py` if needed (Linux only)

---

## ⚠️ Legal Disclaimer

This software is for **educational and ethical research** on devices **you own**.  
Unauthorized use may violate privacy laws and is strictly **not recommended**.