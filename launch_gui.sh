#!/bin/bash

# Crowd Analysis GUI Launcher Script
# This script sets up the environment and launches the GUI application

echo "🚀 Starting Crowd Analysis GUI..."
echo "=================================="

# Check if we're in the right directory
if [ ! -f "gui_app.py" ]; then
    echo "❌ Error: Please run this script from the Crowd-Analysis-main directory"
    echo "Current directory: $(pwd)"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d ".venv" ] && [ ! -d "crowd_analysis_env" ]; then
    echo "❌ No virtual environment found!"
    echo "Please run: python -m venv .venv && source .venv/bin/activate"
    exit 1
fi

# Activate virtual environment
if [ -d ".venv" ]; then
    echo "📦 Activating virtual environment (.venv)..."
    source .venv/bin/activate
elif [ -d "crowd_analysis_env" ]; then
    echo "📦 Activating virtual environment (crowd_analysis_env)..."
    source crowd_analysis_env/bin/activate
fi

# Check and install GUI requirements if needed
echo "🔧 Checking GUI dependencies..."
if [ -f "gui_requirements.txt" ]; then
    pip install -q -r gui_requirements.txt
fi

# Create required directories if they don't exist
echo "📁 Setting up directories..."
mkdir -p processed_data
mkdir -p generated_plots
mkdir -p logs

# Check if YOLO weights exist
if [ ! -f "YOLOv4-tiny/yolov4-tiny.weights" ]; then
    echo "⚠️  Warning: YOLO weights not found at YOLOv4-tiny/yolov4-tiny.weights"
    echo "Please ensure YOLO model files are properly installed."
fi

# Launch GUI
echo "🖥️  Launching Crowd Analysis GUI..."
python gui_app.py

echo "👋 GUI application closed."
