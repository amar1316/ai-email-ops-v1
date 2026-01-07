@echo off
cd /d "%~dp0"

echo ====================================
echo  AI Email Operations Assistant (V1)
echo ====================================

if not exist venv (
    echo Virtual environment not found.
    echo Please create venv first.
    pause
    exit /b
)

call venv\Scripts\activate

python main.py

echo.
echo Agent finished running.
pause
