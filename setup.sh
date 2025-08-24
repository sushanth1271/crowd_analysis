#!/bin/bash

# Crowd Analysis System Setup Script
# This script automates the setup process for the improved crowd analysis system

echo "🚀 Setting up Crowd Analysis System..."
echo "======================================"

# Check if Python 3.8+ is available
python_version=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))" 2>/dev/null || echo "0.0")
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Error: Python 3.8 or higher is required. Found: $python_version"
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d "crowd_analysis_env" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv crowd_analysis_env
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source crowd_analysis_env/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directory structure..."
mkdir -p logs
mkdir -p processed_data
mkdir -p YOLOv4-tiny

# Download YOLO files if they don't exist
echo "🤖 Setting up YOLO model..."
if [ ! -f "YOLOv4-tiny/yolov4-tiny.weights" ]; then
    echo "⬇️  Downloading YOLO weights..."
    wget -P YOLOv4-tiny https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4-tiny.weights
    if [ $? -eq 0 ]; then
        echo "✅ YOLO weights downloaded successfully"
    else
        echo "❌ Failed to download YOLO weights. Please download manually."
        echo "   URL: https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4-tiny.weights"
        echo "   Place in: YOLOv4-tiny/yolov4-tiny.weights"
    fi
else
    echo "✅ YOLO weights already exist"
fi

if [ ! -f "YOLOv4-tiny/yolov4-tiny.cfg" ]; then
    echo "⬇️  Downloading YOLO config..."
    wget -P YOLOv4-tiny https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg
    if [ $? -eq 0 ]; then
        echo "✅ YOLO config downloaded successfully"
    else
        echo "❌ Failed to download YOLO config. Please download manually."
        echo "   URL: https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg"
        echo "   Place in: YOLOv4-tiny/yolov4-tiny.cfg"
    fi
else
    echo "✅ YOLO config already exists"
fi

# Check if Deep SORT model exists
if [ ! -f "model_data/mars-small128.pb" ]; then
    echo "❌ Deep SORT model file missing: model_data/mars-small128.pb"
    echo "   Please ensure this file exists for tracking to work properly."
fi

# Create example environment file
if [ ! -f ".env" ]; then
    echo "📝 Creating example environment file..."
    cat > .env << EOF
# Environment Configuration for Crowd Analysis
# Copy this file and modify as needed

# Video source
VIDEO_CAP=video/7.mp4
IS_CAM=false

# Processing parameters
FRAME_SIZE=1080
MIN_CONF=0.3
SOCIAL_DISTANCE=50

# Logging
LOG_LEVEL=INFO

# Performance
ENABLE_GPU=false
EOF
    echo "✅ Created .env file with default values"
fi

# Validate installation
echo "🔍 Validating installation..."

python3 -c "
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import yaml

print('✅ All core dependencies imported successfully')

# Check OpenCV version
print(f'OpenCV version: {cv2.__version__}')

# Check TensorFlow GPU support
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f'✅ TensorFlow GPU support detected: {len(gpus)} GPU(s)')
else:
    print('ℹ️  No GPU detected (CPU-only mode)')

print('🎉 Installation validation completed!')
"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Setup completed successfully!"
    echo ""
    echo "Next steps:"
    echo "1. Activate the virtual environment:"
    echo "   source crowd_analysis_env/bin/activate"
    echo ""
    echo "2. Configure your video source in config.yaml"
    echo ""
    echo "3. Run the system:"
    echo "   python main_improved.py"
    echo ""
    echo "4. Or use the original system:"
    echo "   python main.py"
    echo ""
    echo "5. Generate analytics:"
    echo "   python -c \"from utils.analytics import generate_analytics_report; generate_analytics_report()\""
    echo ""
    echo "📖 Check the IMPROVEMENTS.md file for detailed information about new features."
else
    echo "❌ Installation validation failed. Please check the error messages above."
    exit 1
fi
