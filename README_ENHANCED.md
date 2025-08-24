# 🚀 Crowd Analysis System - Enhanced Edition

An advanced, production-ready crowd analysis system with comprehensive monitoring, analytics, and performance optimizations.

## 📋 Table of Contents
- [🆕 New Features](#-new-features)
- [⚡ Quick Start](#-quick-start)
- [🏗️ Architecture](#️-architecture)
- [📊 Analytics & Insights](#-analytics--insights)
- [⚙️ Configuration](#️-configuration)
- [🔧 Development](#-development)
- [📈 Performance](#-performance)
- [🐛 Troubleshooting](#-troubleshooting)

## 🆕 New Features

### Core Improvements
- **🏗️ Modular Architecture**: Clean separation of concerns with dedicated modules
- **📝 Advanced Logging**: Comprehensive logging with rotation and performance tracking  
- **⚙️ Modern Configuration**: YAML-based config with environment variable support
- **🚨 Error Handling**: Robust error handling with graceful degradation
- **📊 Performance Monitoring**: Real-time performance metrics and optimization

### Analytics Enhancements
- **📈 Advanced Analytics**: Comprehensive crowd behavior analysis
- **🎯 Pattern Recognition**: Movement pattern clustering and anomaly detection
- **📋 Detailed Reports**: JSON-based insights and statistics
- **🔍 Data Validation**: Input validation and data quality checks

### User Experience
- **🖥️ Better CLI**: Enhanced command-line interface with progress reporting
- **📱 Modern Config**: YAML configuration with validation
- **🔧 Easy Setup**: Automated installation and setup scripts
- **📖 Documentation**: Comprehensive documentation and examples

## ⚡ Quick Start

### 1. Automated Setup (Recommended)
```bash
# Clone the repository (if not already done)
git clone <repository-url>
cd Crowd-Analysis-main

# Run the setup script
./setup.sh
```

### 2. Manual Setup
```bash
# Create virtual environment
python3 -m venv crowd_analysis_env
source crowd_analysis_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create directories
mkdir -p logs processed_data YOLOv4-tiny

# Download YOLO files
wget -P YOLOv4-tiny https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4-tiny.weights
wget -P YOLOv4-tiny https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg
```

### 3. Configure Your Video Source
Edit `config.yaml`:
```yaml
video:
  video_cap: "path/to/your/video.mp4"  # Or 0 for webcam
  is_cam: false                        # Set true for webcam
```

### 4. Run the System
```bash
# Enhanced version (recommended)
python main_improved.py

# Original version (for compatibility)
python main.py
```

## 🏗️ Architecture

### Directory Structure
```
Crowd-Analysis-main/
├── 📁 utils/                    # Utility modules
│   ├── logger.py               # Logging configuration
│   ├── config_manager.py       # Configuration management
│   ├── error_handling.py       # Error handling utilities
│   ├── performance.py          # Performance monitoring
│   └── analytics.py            # Advanced analytics
├── 📁 logs/                    # Log files
├── 📁 processed_data/          # Output data
├── 📁 YOLOv4-tiny/            # YOLO model files
├── 📄 config.yaml             # Modern configuration
├── 📄 main_improved.py        # Enhanced main module
├── 📄 enhanced_tracking.py    # Improved detection
└── 📄 setup.sh               # Setup script
```

### Core Components

#### 1. Configuration Manager (`utils/config_manager.py`)
- YAML-based configuration with validation
- Environment variable support
- Backward compatibility with legacy config
- Dynamic configuration updates

#### 2. Logging System (`utils/logger.py`)
- Structured logging with rotation
- Multiple log levels and handlers
- Performance tracking integration
- System information logging

#### 3. Error Handling (`utils/error_handling.py`)
- Custom exception classes
- Decorators for automatic error handling
- Graceful degradation strategies
- Progress reporting utilities

#### 4. Performance Monitor (`utils/performance.py`)
- Real-time CPU, memory, and FPS monitoring
- Background performance tracking
- Automatic optimization suggestions
- GPU acceleration support

#### 5. Advanced Analytics (`utils/analytics.py`)
- Comprehensive crowd behavior analysis
- Movement pattern clustering
- Statistical insights and reports
- Data export capabilities

## 📊 Analytics & Insights

### Available Analytics

#### 1. Crowd Density Analysis
- Average, peak, and minimum crowd sizes
- Density distribution patterns
- Time-based crowd analysis

#### 2. Social Distancing Monitoring
- Violation rates and patterns
- Correlation with crowd density
- Safety compliance metrics

#### 3. Movement Pattern Analysis
- Individual tracking statistics
- Path distance and speed analysis
- Movement clustering and patterns
- Behavioral anomaly detection

#### 4. Security Monitoring
- Abnormal activity detection rates
- Incident period identification
- Security alert patterns

### Generating Reports
```bash
# Generate comprehensive analytics
python -c "from utils.analytics import generate_analytics_report; print(generate_analytics_report())"

# View saved insights
cat processed_data/analytics_insights.json
```

## ⚙️ Configuration

### Configuration File (`config.yaml`)

```yaml
video:
  video_cap: "video/7.mp4"          # Video source
  is_cam: false                     # Camera mode
  high_cam: true                    # Camera height position
  
detection:
  frame_size: 1080                  # Processing frame size
  show_processing_output: true      # Show video output
  data_record: true                 # Record data
  
social_distance:
  enabled: true                     # Enable monitoring
  social_distance: 50               # Distance threshold (pixels)
  
abnormal_activity:
  enabled: true                     # Enable detection
  energy_threshold: 1866            # Energy threshold
  activity_threshold: 0.66          # Activity ratio threshold
```

### Environment Variables
Override config values with environment variables:
```bash
export VIDEO_CAP="/path/to/video.mp4"
export IS_CAM=false
export FRAME_SIZE=1080
export LOG_LEVEL=DEBUG
```

### Command Line Options
```bash
# Specify custom config file
python main_improved.py --config custom_config.yaml

# Set log level
python main_improved.py --log-level DEBUG
```

## 🔧 Development

### Code Quality Tools
```bash
# Install development dependencies
pip install -r requirements.txt

# Code formatting
black *.py utils/*.py

# Code linting  
flake8 *.py utils/*.py

# Run tests
pytest tests/ -v --cov
```

### Adding New Features

#### 1. Create a New Module
```python
# utils/my_feature.py
import logging
from utils.error_handling import handle_exceptions

class MyFeature:
    def __init__(self):
        self.logger = logging.getLogger('crowd_analysis.my_feature')
    
    @handle_exceptions()
    def process(self):
        self.logger.info("Processing...")
        # Your implementation here
```

#### 2. Update Configuration
```python
# utils/config_manager.py
@dataclass
class MyFeatureConfig:
    enabled: bool = True
    parameter: int = 100

@dataclass
class Config:
    # ... existing configs
    my_feature: MyFeatureConfig = MyFeatureConfig()
```

#### 3. Add to Main System
```python
# main_improved.py
from utils.my_feature import MyFeature

class CrowdAnalysisSystem:
    def __init__(self):
        # ... existing initialization
        self.my_feature = MyFeature()
    
    def run(self):
        # ... existing code
        if self.config.my_feature.enabled:
            self.my_feature.process()
```

## 📈 Performance

### Performance Monitoring
- Real-time CPU and memory usage tracking
- FPS monitoring and optimization
- Automatic performance warnings
- Background monitoring with configurable intervals

### Optimization Features
- Automatic OpenCV optimizations
- GPU acceleration detection
- Dynamic frame skipping
- Memory usage optimization

### Performance Tips
1. **Use GPU acceleration** when available
2. **Reduce frame size** for better performance
3. **Enable frame skipping** for non-critical applications
4. **Monitor system resources** during processing
5. **Use SSD storage** for better I/O performance

## 🐛 Troubleshooting

### Common Issues

#### 1. "Video source not found"
```bash
# Check video file path
ls -la video/
# Update config.yaml with correct path
```

#### 2. "YOLO model files missing"
```bash
# Re-download YOLO files
./setup.sh
# Or manually download and place in YOLOv4-tiny/
```

#### 3. "Memory issues during processing"
```bash
# Reduce frame size in config.yaml
frame_size: 720  # Instead of 1080

# Enable performance monitoring
python main_improved.py --log-level DEBUG
```

#### 4. "Low processing FPS"
```bash
# Check GPU availability
python -c "import cv2; print('CUDA devices:', cv2.cuda.getCudaEnabledDeviceCount())"

# Enable optimizations in code
from utils.performance import optimization_manager
optimization_manager.apply_all_optimizations()
```

### Debug Mode
```bash
# Run with debug logging
python main_improved.py --log-level DEBUG

# Check logs
tail -f logs/crowd_analysis_*.log
```

### Performance Diagnostics
```bash
# Monitor system resources
python -c "
from utils.performance import performance_monitor
performance_monitor.start_monitoring()
import time; time.sleep(30)
print(performance_monitor.get_performance_summary())
"
```

## 📚 Additional Resources

- **Original README**: See `README.md` for original project documentation
- **Improvements Plan**: See `IMPROVEMENTS.md` for detailed improvement roadmap
- **Sample Outputs**: Check `assets/` directory for example outputs
- **API Documentation**: Generated automatically from code docstrings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes with proper documentation
4. Add tests for new functionality
5. Ensure code passes all quality checks: `black`, `flake8`, `pytest`
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to the branch: `git push origin feature/amazing-feature`
8. Open a Pull Request

## 📄 License

This project maintains the same license as the original project. See `LICENSE` file for details.

---

## 🎯 What's Next?

The enhanced system provides a solid foundation for production use. Future improvements could include:

- **Web Dashboard**: Real-time monitoring interface
- **Database Integration**: Long-term data storage and querying
- **API Endpoints**: RESTful API for integration with other systems
- **Mobile App**: Mobile interface for monitoring
- **Cloud Deployment**: Docker containers and cloud deployment
- **Machine Learning**: Advanced behavioral analysis with ML models

**Happy analyzing! 🎉**
