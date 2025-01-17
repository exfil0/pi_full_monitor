#!/bin/bash

echo "Setting up pi_full_monitor..."

# Ensure Python dependencies
echo "Checking Python dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip python3-venv

# Create virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv

# Activate and install the package
source venv/bin/activate
pip install --upgrade pip
pip install .

echo "pi_full_monitor is now installed. Run it with 'pi_full_monitor'!"
