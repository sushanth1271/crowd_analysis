#!/bin/bash

echo "🎥 Launching Enhanced Crowd Analysis GUI..."
echo "============================================"

# Change to the project directory
cd /Users/levi/Crowd-Analysis-main

# Activate virtual environment
source .venv/bin/activate

# Launch the enhanced GUI
python enhanced_gui.py

echo "👋 Enhanced GUI application closed."
