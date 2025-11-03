#!/bin/bash

echo "============================================================"
echo "  Python IDE - Starting Server"
echo "============================================================"
echo ""

cd "$(dirname "$0")"

echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python is not installed"
    echo "Please install Python from https://www.python.org/"
    exit 1
fi

python3 --version

echo ""
echo "Installing/Checking dependencies..."
pip3 install -q flask flask-cors werkzeug

echo ""
echo "============================================================"
echo "  Starting Python IDE Server..."
echo "  Your browser will open automatically!"
echo "============================================================"
echo ""

python3 app.py
