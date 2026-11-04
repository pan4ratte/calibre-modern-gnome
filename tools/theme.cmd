@echo off
rem Runs tools\theme.py with calibre's Python. Usage: tools\theme.cmd check ^| build ^| preview
setlocal
set "CALIBRE_DEBUG=calibre-debug.exe"
where calibre-debug.exe >nul 2>nul || set "CALIBRE_DEBUG=%ProgramFiles%\Calibre2\calibre-debug.exe"
"%CALIBRE_DEBUG%" "%~dp0theme.py" %*
