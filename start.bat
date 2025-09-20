@echo off
echo.
echo ==================================================
echo Career ^& Skills Advisor - Web Application
echo ==================================================
echo.

REM Check if Python is available
py --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

REM Check if Flask is installed
py -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Flask not found. Installing Flask...
    py -m pip install flask
    if errorlevel 1 (
        echo Error: Failed to install Flask
        echo Please run: py -m pip install flask
        echo.
        pause
        exit /b 1
    )
)

echo Starting Career ^& Skills Advisor Web Application...
echo.

REM Start the application
py start_server.py

echo.
echo Application stopped.
pause