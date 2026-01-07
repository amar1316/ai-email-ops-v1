@echo off
cd /d "%~dp0"

echo Activating virtual environment...
call venv\Scripts\activate

echo Running AI Email Operations Agent...
python main.py

pause
