@echo off
echo ============================================================
echo   Python IDE - Starting Server
echo ============================================================
echo.

cd /d "%~dp0"

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo.
echo Installing/Checking dependencies...
pip install -q flask flask-cors werkzeug

echo.
echo ============================================================
echo   Starting Python IDE Server...
echo   Your browser will open automatically!
echo ============================================================
echo.

python app.py

pause
