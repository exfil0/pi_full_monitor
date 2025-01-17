#!/bin/bash

echo "Setting up pi_full_monitor..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install .
echo "Installation complete. You can now run 'pi_full_monitor'."
