#!/bin/bash
# Setup script for Online Course Django Project

echo "==================================="
echo "Online Course Project Setup"
echo "==================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

echo ""
echo "==================================="
echo "Setup Complete!"
echo "==================================="
echo ""
echo "To start the development server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "To create a superuser, run:"
echo "  python manage.py createsuperuser"
echo ""
echo "Access the application at:"
echo "  - Home: http://localhost:8000/"
echo "  - Admin: http://localhost:8000/admin/"
echo ""
