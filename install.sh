#!/bin/bash

echo "Setting up pi_full_monitor..."

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the package
pip install .

echo "pi_full_monitor is now installed. Run it with 'pi_full_monitor'."
