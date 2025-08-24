# 🖥️ Crowd Analysis GUI Application

A comprehensive graphical user interface for the Crowd Analysis System, providing an intuitive way to analyze videos and visualize crowd behavior patterns.

## ✨ Features

### 🎥 Video Processing
- **Easy Video Upload**: Browse and select video files through a user-friendly interface
- **Multiple Format Support**: MP4, AVI, MOV, MKV, FLV, WMV
- **Real-time Progress Tracking**: Visual progress bar and status updates during processing

### 🔍 Analysis Options
Choose from multiple analysis types:
- **🚶 Social Distancing Analysis**: Detect and track social distance violations
- **👥 Crowd Counting & Density**: Analyze crowd size and density over time
- **🏃 Movement Pattern Analysis**: Track and visualize movement flows
- **⚠️ Abnormal Behavior Detection**: Identify unusual crowd behaviors

### 📊 Integrated Dashboard
- **Real-time Results Display**: View analysis results as they're generated
- **Interactive Visualizations**: Built-in image viewer for generated plots
- **Tabbed Interface**: Organized results by analysis type
- **Summary Statistics**: Key metrics and insights at a glance

### ⚡ Quick Analysis Modes
One-click analysis options:
- Social Distancing Only
- Crowd Analysis Only  
- Movement Analysis Only
- Full Analysis (all features)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ with tkinter support
- Virtual environment with project dependencies
- YOLO model weights (yolov4-tiny.weights)

### Installation & Launch

#### Option 1: Using the Launcher Script (Recommended)
```bash
# Make sure you're in the project directory
cd /path/to/Crowd-Analysis-main

# Run the launcher
./launch_gui.sh
```

#### Option 2: Manual Launch
```bash
# Activate virtual environment
source .venv/bin/activate  # or: source crowd_analysis_env/bin/activate

# Install GUI requirements
pip install -r gui_requirements.txt

# Launch GUI
python gui_app.py
```

## 🎯 How to Use

### 1. **Upload Video**
   - Click "Browse" button
   - Select your video file
   - File path will appear in the text field

### 2. **Select Analysis Options**
   - Check the desired analysis types:
     - ✅ Social Distancing Analysis
     - ✅ Crowd Counting & Density
     - ✅ Movement Pattern Analysis
     - ✅ Abnormal Behavior Detection

### 3. **Start Analysis**
   - Click "🚀 Start Analysis" button
   - Monitor progress in the status bar
   - Wait for processing to complete

### 4. **View Results**
   - Switch to the "📊 Dashboard" tab
   - Explore individual analysis tabs
   - Click "📊 View Dashboard" to open plots folder

## 📱 User Interface Guide

### Main Window Layout

```
┌─────────────────────────────────────────────────────────────┐
│                🎥 Crowd Analysis System                     │
├─────────────────┬───────────────────────────────────────────┤
│  📋 Analysis    │           📊 Analysis Results            │
│  Controls       │                                           │
│                 │  ┌─────────────────────────────────────┐  │
│  📁 Video       │  │  📊 Dashboard │ 🚶 Social │ 👥 Crowd│  │
│  Upload         │  │                │ Distancing │ Analysis│  │
│                 │  └─────────────────────────────────────────  │
│  🔍 Analysis    │                                           │
│  Options        │                                           │
│                 │                                           │
│  ⚡ Quick       │                                           │
│  Analysis       │                                           │
├─────────────────┴───────────────────────────────────────────┤
│                    📋 Status & Progress                     │
└─────────────────────────────────────────────────────────────┘
```

### Control Panel Features

#### 📁 Video Upload Section
- **File Path Field**: Shows selected video path
- **Browse Button**: Opens file dialog for video selection
- **Supported Formats**: Automatically filters for video files

#### 🔍 Analysis Options
- **Checkboxes**: Select/deselect analysis types
- **Multiple Selection**: Choose one or more analysis options
- **Smart Validation**: Ensures at least one option is selected

#### Action Buttons
- **🚀 Start Analysis**: Begin video processing
- **⏹️ Stop Analysis**: Cancel ongoing analysis
- **📊 View Dashboard**: Open plots directory

#### ⚡ Quick Analysis
- **Social Distancing Only**: Focus on distance violations
- **Crowd Analysis Only**: Count and density analysis
- **Movement Only**: Track movement patterns

### Results Panel

#### 📊 Dashboard Tab
- **Summary Statistics**: Key metrics overview
- **Generated Visualizations**: All plots displayed inline
- **Scrollable Content**: Handle multiple charts and data

#### Individual Analysis Tabs
- **🚶 Social Distancing**: Distance violation details
- **👥 Crowd Analysis**: Count and density charts  
- **🏃 Movement Patterns**: Flow and trajectory maps
- **⚠️ Abnormal Behavior**: Anomaly detection results

## 📈 Generated Visualizations

The GUI automatically generates and displays:

1. **📊 Analytics Dashboard** - Complete overview
2. **👥 Crowd Data Analysis** - Population trends
3. **⚡ Energy Distribution** - Movement intensity
4. **📈 Energy Statistics** - Statistical summaries
5. **🗺️ Heatmap** - Location density
6. **🎯 Optical Flow** - Movement tracking

## 🔧 Technical Details

### Architecture
- **Frontend**: Python tkinter with ttk widgets
- **Backend**: Enhanced crowd analysis system
- **Threading**: Background processing for responsiveness
- **Progress Updates**: Real-time status and progress reporting

### Performance
- **Multi-threaded Processing**: GUI remains responsive during analysis
- **Memory Efficient**: Streams video processing
- **Progress Tracking**: Frame-by-frame progress updates
- **Error Handling**: Comprehensive error management

### File Organization
```
Crowd-Analysis-main/
├── gui_app.py              # Main GUI application
├── launch_gui.sh           # GUI launcher script  
├── gui_requirements.txt    # GUI-specific dependencies
├── generated_plots/        # Output visualizations
├── processed_data/         # Analysis results
├── logs/                   # Application logs
└── utils/                  # Utility modules
```

## 🐛 Troubleshooting

### Common Issues

#### "No module named 'PIL'"
```bash
pip install Pillow
```

#### "tkinter not found"
- On Ubuntu/Debian: `sudo apt-get install python3-tk`
- On macOS: tkinter is included with Python
- On Windows: tkinter is included with Python

#### "YOLO weights not found"
- Ensure `YOLOv4-tiny/yolov4-tiny.weights` exists
- Download from official YOLO repository if missing

#### GUI Freezing During Analysis
- This is normal for large videos
- Progress bar shows current status
- Use "Stop Analysis" if needed

### Performance Tips
- **Smaller Videos**: Process faster, good for testing
- **Lower Resolution**: Faster processing, acceptable results
- **Fewer Analysis Options**: Reduced processing time
- **Close Other Applications**: More system resources available

## 🎨 Customization

### Themes
The GUI supports different visual themes:
```python
# In gui_app.py, modify the style configuration
style = ttk.Style()
style.theme_use('clam')  # Try: 'default', 'alt', 'clam', 'classic'
```

### Window Size
```python
# Adjust initial window size
self.root.geometry("1200x800")  # width x height
```

### Colors
```python
# Customize color scheme
self.root.configure(bg='#f0f0f0')  # Background color
```

## 🤝 Integration

The GUI seamlessly integrates with:
- ✅ **Original Analysis Engine**: Full compatibility maintained
- ✅ **Enhanced Logging System**: All activities logged
- ✅ **Configuration Management**: Uses YAML configs
- ✅ **Performance Monitoring**: Built-in metrics
- ✅ **Analytics Engine**: Advanced crowd insights

## 📋 Future Enhancements

Planned features:
- 🔄 **Real-time Video Streaming**: Live camera analysis
- 🌐 **Web Dashboard**: Browser-based interface
- 📱 **Mobile Support**: Responsive design
- ☁️ **Cloud Integration**: Remote processing
- 🤖 **AI Insights**: Machine learning recommendations
- 📧 **Alert System**: Automated notifications

## 💡 Tips & Best Practices

1. **Video Selection**: Choose clear, well-lit videos for best results
2. **Analysis Options**: Start with one option to test performance
3. **Results Review**: Check Dashboard tab for complete overview
4. **Error Logs**: Check `logs/gui_app.log` for detailed information
5. **Performance**: Close other applications for faster processing

---

### 🎉 Enjoy analyzing crowds with the enhanced GUI interface!

For technical support or feature requests, check the project logs or documentation.
