chcp 65001
@echo off
ipconfig | findstr "IPv4" | findstr "172.16." >> F:\\006.txt
getmac /FO list /V >> F:\\006.txt
echo ------------------------------------------------------------------------- >>F:\\006.txt