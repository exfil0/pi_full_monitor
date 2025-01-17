#!/bin/bash

echo "Setting up pi_full_monitor..."

# Check for and install Python dependencies
echo "Installing Python dependencies..."
sudo apt update && sudo apt install -y python3 python3-venv python3-pip

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install the package
echo "Installing the pi_full_monitor package..."
pip install .

# Create a CLI command
echo "pi_full_monitor is now installed. Run it with 'pi_full_monitor'."
