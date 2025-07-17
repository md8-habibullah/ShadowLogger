@echo off
echo Killing keylogger (if running)...
taskkill /F /IM python.exe >nul 2>&1
del %USERPROFILE%\keylog.txt
echo Uninstalled.
