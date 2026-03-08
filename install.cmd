@echo off
setlocal
powershell -NoLogo -ExecutionPolicy Bypass -File "%~dp0install.ps1"
if errorlevel 1 (
  echo.
  echo Install failed.
  pause
  exit /b 1
)
echo.
echo Install completed.
pause
