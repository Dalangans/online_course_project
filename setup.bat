@echo off
REM Setup script for Online Course Django Project on Windows

echo ===================================
echo Online Course Project Setup
echo ===================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python.
    exit /b 1
)

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo ===================================
echo Setup Complete!
echo ===================================
echo.
echo To start the development server, run:
echo   venv\Scripts\activate.bat
echo   python manage.py runserver
echo.
echo To create a superuser, run:
echo   python manage.py createsuperuser
echo.
echo Access the application at:
echo   - Home: http://localhost:8000/
echo   - Admin: http://localhost:8000/admin/
echo.
pause
