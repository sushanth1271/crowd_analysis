# 🎯 AI-Powered Crowd Analysis System

> **Professional crowd monitoring and analysis system using YOLOv4-tiny and Deep SORT tracking**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Windows Compatible](https://img.shields.io/badge/Windows-Compatible-brightgreen.svg)](WINDOWS_PLOT_FIX_README.md)

## 🚀 **Features**

### **Core Capabilities**
- 🤖 **Real-time people detection** using YOLOv4-tiny
- 🎯 **Multi-object tracking** with Deep SORT algorithm  
- 📊 **Social distance monitoring** and violation detection
- 📈 **Movement pattern analysis** and crowd flow tracking
- 🎨 **Professional GUI** with real-time preview and analytics
- 📋 **Comprehensive reporting** with visualizations and statistics

### **Analysis Modules**
- **Crowd Density Analysis** - Real-time people counting and density mapping
- **Movement Tracking** - Individual trajectory analysis and flow patterns
- **Social Distance Monitoring** - Automatic violation detection and alerts
- **Energy Analysis** - Movement intensity and activity level assessment
- **Statistical Reporting** - Comprehensive analytics with visual dashboards

### **Technical Highlights**
- **Multi-threaded Architecture** - Non-blocking GUI with background processing
- **Cross-platform Support** - Works on Windows, Mac, and Linux
- **Professional Visualizations** - High-quality plots and analytics dashboards
- **Flexible Configuration** - Easy setup for different scenarios and requirements
- **Export Capabilities** - CSV data and PNG visualizations

## 🛠️ **Installation**

### **Prerequisites**
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- OpenCV-compatible camera or video files

### **Quick Setup**

#### **Windows Users:**
```cmd
# Clone the repository
git clone https://github.com/srujandivakar/crowd_analysis.git
cd crowd_analysis

# Install dependencies
pip install -r requirements.txt

# Launch the interactive setup
windows_launcher.bat
```

#### **Mac/Linux Users:**
```bash
# Clone the repository
git clone https://github.com/srujandivakar/crowd_analysis.git
cd crowd_analysis

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python modern_crowd_studio.py
```

## 🎮 **Usage**

### **1. Launch the GUI**
```bash
python modern_crowd_studio.py
```

### **2. Select Video Source**
- Click **"Browse Video"** to select a video file
- Or configure camera input in `config.py`

### **3. Configure Analysis**
- Adjust detection sensitivity
- Set social distance parameters
- Enable/disable specific analysis modules

### **4. Run Analysis**
- Click **"Start Analysis"** to begin processing
- Monitor real-time progress and preview
- View live statistics and metrics

### **5. Review Results**
- Access generated plots and visualizations
- Export data in CSV format
- Review comprehensive analytics dashboard

## 📊 **System Architecture**

```
┌─────────────────────────────────────────────────┐
│                MAIN GUI THREAD                  │
│         (CustomTkinter Interface)              │
└─────────────┬───────────────────────────────────┘
              │
              ├──► 🤖 ANALYSIS THREAD
              │    • YOLOv4-tiny Detection
              │    • Deep SORT Tracking  
              │    • Data Processing
              │
              ├──► 🎬 VIDEO PREVIEW THREAD
              │    • Real-time Display
              │    • Progress Updates
              │
              └──► 📊 VISUALIZATION THREAD
                   • Plot Generation
                   • Report Creation
```

### **Core Components**
- **Detection Engine**: YOLOv4-tiny for fast, accurate people detection
- **Tracking System**: Deep SORT for consistent multi-object tracking
- **Analysis Pipeline**: Modular processing for various analytics
- **GUI Framework**: CustomTkinter for modern, responsive interface
- **Data Management**: Structured CSV/JSON output for easy integration

## 📁 **Project Structure**

```
crowd_analysis/
├── 🎯 Core System
│   ├── main.py                     # Main analysis pipeline
│   ├── modern_crowd_studio.py      # Professional GUI application
│   ├── video_process.py            # Video processing utilities
│   └── config.py                   # System configuration
│
├── 🤖 AI Models
│   ├── YOLOv4-tiny/               # Object detection model
│   ├── deep_sort/                 # Multi-object tracking
│   └── model_data/                # Pre-trained weights
│
├── 📊 Analysis Modules
│   ├── tracking.py                # Object tracking logic
│   ├── abnormal_data_process.py   # Anomaly detection
│   ├── crowd_data_present.py      # Crowd analytics
│   └── movement_data_present.py   # Movement analysis
│
├── 🎨 Visualization
│   ├── generate_all_plots.py      # Plot generation (Mac/Linux)
│   └── generate_all_plots_windows.py # Windows-compatible plots
│
├── 🪟 Windows Support
│   ├── windows_launcher.bat       # Interactive setup launcher
│   ├── fix_windows_plots.bat      # Plot caching fix
│   └── diagnose_windows_plots.bat # Diagnostic tool
│
├── 📚 Documentation
│   ├── README.md                  # This file
│   ├── TECHNICAL_REPORT.md        # Detailed technical documentation
│   └── WINDOWS_PLOT_FIX_README.md # Windows troubleshooting guide
│
└── 🎬 Demo Assets
    ├── assets/                    # Sample outputs and screenshots
    └── video/                     # Sample video files
```

## ⚙️ **Configuration**

### **Basic Configuration** (`config.py`)
```python
# Video Input
VIDEO_CONFIG = {
    "IS_CAM": False,           # Use camera (True) or video file (False)
    "VIDEO_CAP": "video/7.mp4" # Path to video file
}

# Detection Settings
YOLO_CONFIG = {
    "WEIGHTS_PATH": "YOLOv4-tiny/yolov4-tiny.weights",
    "CONFIG_PATH": "YOLOv4-tiny/yolov4-tiny.cfg"
}

# Analysis Parameters
SOCIAL_DISTANCE_THRESHOLD = 150  # Pixels
FRAME_SIZE = 720                 # Processing resolution
```

## 🎨 **Output Examples**

### **Generated Visualizations**
- `crowd_data_analysis.png` - People count and violations over time
- `optical_flow.png` - Movement tracking visualization
- `heatmap.png` - Activity density mapping  
- `energy_distribution.png` - Movement intensity analysis
- `analytics_dashboard.png` - Comprehensive summary dashboard

### **Data Exports**
- `crowd_data.csv` - Timestamped crowd metrics
- `movement_data.csv` - Individual tracking data
- `video_data.json` - Analysis metadata and settings

## 🔧 **Troubleshooting**

### **Windows Users**
If plots don't update properly:
1. Run `fix_windows_plots.bat` as administrator
2. Use `diagnose_windows_plots.bat` to identify issues
3. See [Windows Fix Guide](WINDOWS_PLOT_FIX_README.md) for details

### **Common Issues**
- **GPU not detected**: Install CUDA drivers for GPU acceleration
- **Camera not working**: Check camera permissions and drivers
- **Slow processing**: Reduce FRAME_SIZE in config.py
- **Memory issues**: Close other applications, increase virtual memory

## 📈 **Performance**

### **System Requirements**
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **CPU** | Dual-core 2.5GHz | Quad-core 3.0GHz+ |
| **RAM** | 4GB | 8GB+ |
| **GPU** | Integrated | Dedicated NVIDIA GPU |
| **Storage** | 2GB free space | 5GB+ free space |

### **Processing Speeds**
- **Real-time analysis**: 15-30 FPS depending on hardware
- **Video processing**: 2-5x real-time speed
- **GUI responsiveness**: <100ms update intervals

## 🤝 **Contributing**

We welcome contributions! Please see our [Technical Report](TECHNICAL_REPORT.md) for detailed system architecture.

### **Areas for Contribution**
- 🎯 New analysis modules
- 🎨 UI/UX improvements  
- 📊 Additional visualization types
- 🔧 Performance optimizations
- 📝 Documentation enhancements

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 **Acknowledgments**

- **YOLOv4**: Object detection framework
- **Deep SORT**: Multi-object tracking algorithm  
- **CustomTkinter**: Modern GUI framework
- **OpenCV**: Computer vision library

## 📞 **Support**

- 📖 **Documentation**: See [Technical Report](TECHNICAL_REPORT.md)
- 🪟 **Windows Issues**: See [Windows Fix Guide](WINDOWS_PLOT_FIX_README.md)
- 🐛 **Bug Reports**: Create an issue on GitHub
- 💡 **Feature Requests**: Open a discussion on GitHub

---

<div align="center">

**Built with ❤️ for intelligent crowd monitoring**

[🚀 Get Started](#installation) • [📖 Documentation](TECHNICAL_REPORT.md) • [🐛 Report Issues](https://github.com/srujandivakar/crowd_analysis/issues)

</div>
