@echo off
title Career Advisor - Network Mode
cls

echo =============================================
echo Career Advisor - NETWORK ACCESS
echo =============================================
echo.
echo This will start the server so ANY device 
echo on your network can access it!
echo.
echo Devices that can connect:
echo - Phones (Android/iPhone)
echo - Tablets (iPad/Android)  
echo - Laptops (Windows/Mac)
echo - Any device with a web browser
echo.
echo Starting in 3 seconds...
timeout /t 3 >nul

python start_network.py
pause