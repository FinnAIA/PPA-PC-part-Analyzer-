@echo off
title pip installer.bat
py -m pip install --upgrade pip
py -m pip install psutil
py -m pip install socket
py -m pip install getpass
timeout -t 5 <nul
exit
