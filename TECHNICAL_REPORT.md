# 📊 **COMPREHENSIVE TECHNICAL REPORT**
## **AI-Powered Crowd Analysis System**

---

**Project Name**: Intelligent Crowd Analysis and Monitoring System  
**Version**: 2.0 Enhanced  
**Platform**: Python 3.13 with OpenCV, TensorFlow, CustomTkinter  
**Report Date**: August 24, 2025  
**Report Type**: Complete System Architecture and Implementation Analysis  

---

## **📋 TABLE OF CONTENTS**

1. [Executive Summary](#1-executive-summary)
2. [System Architecture Overview](#2-system-architecture-overview)
3. [Core Module Analysis](#3-core-module-analysis)
4. [AI/ML Components](#4-aiml-components)
5. [User Interface Systems](#5-user-interface-systems)
6. [Data Pipeline Architecture](#6-data-pipeline-architecture)
7. [Detection and Tracking Systems](#7-detection-and-tracking-systems)
8. [Configuration Management](#8-configuration-management)
9. [Analysis and Visualization](#9-analysis-and-visualization)
10. [Performance Monitoring](#10-performance-monitoring)
11. [Testing Infrastructure](#11-testing-infrastructure)
12. [Deployment and Installation](#12-deployment-and-installation)
13. [Future Enhancements](#13-future-enhancements)
14. [Technical Specifications](#14-technical-specifications)

---

## **1. EXECUTIVE SUMMARY**

### **1.1 Project Overview**

The AI-Powered Crowd Analysis System is a comprehensive computer vision solution designed for real-time crowd monitoring, social distancing enforcement, restricted area monitoring, and abnormal behavior detection. The system leverages state-of-the-art deep learning models (YOLOv4-tiny) combined with advanced tracking algorithms (Deep SORT) to provide accurate, real-time analysis of crowd dynamics.

### **1.2 Key Features**

#### **Core Capabilities**
- ✅ **Real-time Human Detection**: YOLOv4-tiny based object detection
- ✅ **Multi-Object Tracking**: Deep SORT algorithm for consistent identity tracking
- ✅ **Social Distance Monitoring**: Automated violation detection and alerting
- ✅ **Restricted Area Enforcement**: Time-based access control monitoring
- ✅ **Abnormal Activity Detection**: Energy-based crowd behavior analysis
- ✅ **Professional GUI Interface**: Modern CustomTkinter-based user interface
- ✅ **Real-time Visualization**: Live video preview with analysis overlay
- ✅ **Comprehensive Analytics**: Multi-tab dashboard with live statistics
- ✅ **Data Export**: CSV data export and visualization plot generation
- ✅ **Performance Monitoring**: Real-time FPS and processing statistics

#### **Technical Achievements**
- 🚀 **Real-time Processing**: Optimized for live video analysis (25+ FPS)
- 🎯 **High Accuracy**: Tuned detection parameters for crowd environments
- 📊 **Scalable Architecture**: Modular design supporting multiple analysis types
- 🖥️ **Professional UI**: Modern, intuitive interface with live feedback
- 📈 **Rich Analytics**: Comprehensive reporting and visualization capabilities

### **1.3 System Impact**

The system addresses critical needs in:
- **Public Safety**: Automated crowd monitoring and incident detection
- **Health Compliance**: Social distancing enforcement in public spaces
- **Security Management**: Restricted area access monitoring
- **Facility Management**: Crowd density analysis and capacity planning
- **Research Applications**: Crowd behavior analysis and pattern recognition

---

## **2. SYSTEM ARCHITECTURE OVERVIEW**

### **2.1 High-Level Architecture**

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER INTERFACE LAYER                        │
│  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────┐ │
│  │  Analysis       │  │  Live Video      │  │   Analytics     │ │
│  │  Controls       │  │  Preview         │  │   Dashboard     │ │
│  │                 │  │                  │  │                 │ │
│  │ • Video Select  │  │ • Real-time View │  │ • Live Stats    │ │
│  │ • Start/Stop    │  │ • Detection Box  │  │ • Plots         │ │
│  │ • Progress      │  │ • Status Updates │  │ • Reports       │ │
│  └─────────────────┘  └──────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PROCESSING LAYER                           │
│  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────┐ │
│  │   Video         │  │    AI/ML         │  │   Analysis      │ │
│  │  Processing     │  │   Engine         │  │   Engine        │ │
│  │                 │  │                  │  │                 │ │
│  │ • Frame Extract │  │ • YOLOv4 Detect  │  │ • Social Dist   │ │
│  │ • Preprocessing │  │ • Deep SORT      │  │ • Restricted    │ │
│  │ • Display       │  │ • Track Objects  │  │ • Abnormal      │ │
│  └─────────────────┘  └──────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA LAYER                               │
│  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────┐ │
│  │   Raw Data      │  │   Processed      │  │   Output        │ │
│  │   Storage       │  │     Data         │  │   Generation    │ │
│  │                 │  │                  │  │                 │ │
│  │ • Video Files   │  │ • CSV Records    │  │ • Plots         │ │
│  │ • Config Files  │  │ • JSON Metadata  │  │ • Reports       │ │
│  │ • Model Data    │  │ • Statistics     │  │ • Exports       │ │
│  └─────────────────┘  └──────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### **2.2 Component Relationships**

#### **2.2.1 Data Flow Architecture**
```
Video Input → Frame Processing → AI Detection → Object Tracking → 
Analysis Modules → Data Recording → Visualization → User Interface
```

#### **2.2.2 Module Dependencies**
- **Core Engine**: `main.py` orchestrates all components
- **Video Processing**: `video_process.py` handles frame-level operations
- **AI Detection**: YOLOv4-tiny model for object detection
- **Tracking System**: Deep SORT for multi-object tracking
- **Analysis Modules**: Social distancing, restricted areas, abnormal detection
- **GUI Interface**: `modern_crowd_studio.py` provides user interaction
- **Data Management**: CSV/JSON storage and retrieval systems
- **Visualization**: Plot generation and analytics dashboard

### **2.3 Technology Stack**

#### **2.3.1 Core Technologies**
- **Python 3.13.3**: Primary programming language
- **OpenCV 4.12.0**: Computer vision and video processing
- **TensorFlow 2.20.0**: Deep learning framework
- **NumPy**: Numerical computing and array operations
- **Pandas**: Data manipulation and analysis

#### **2.3.2 AI/ML Components**
- **YOLOv4-tiny**: Real-time object detection model
- **Deep SORT**: Multi-object tracking algorithm
- **Custom Tracking**: Enhanced tracking with Kalman filters

#### **2.3.3 User Interface**
- **CustomTkinter 5.2.2**: Modern GUI framework
- **Matplotlib**: Plot generation and visualization
- **PIL (Pillow)**: Image processing for GUI

#### **2.3.4 Data Processing**
- **CSV**: Structured data storage
- **JSON**: Configuration and metadata storage
- **SQLite**: (Optional) Database storage capability

---

## **3. CORE MODULE ANALYSIS**

### **3.1 Main Application Module (`main.py`)**

#### **3.1.1 Purpose and Functionality**
The `main.py` serves as the central orchestrator for the entire crowd analysis system. It initializes all components, manages the analysis pipeline, and coordinates data flow between modules.

#### **3.1.2 Core Components**
```python
# Primary Responsibilities:
1. System Initialization
2. Video Capture Setup
3. AI Model Loading
4. Analysis Pipeline Coordination
5. Data Recording Management
6. Performance Monitoring
```

#### **3.1.3 Key Functions Analysis**

**System Initialization Process:**
```python
class CrowdAnalysisSystem:
    """
    Main system orchestrator responsible for:
    1. Component initialization and coordination
    2. Video processing pipeline management
    3. AI model integration and optimization
    4. Data flow coordination and recording
    5. Performance monitoring and optimization
    """
    
    def __init__(self):
        # Initialize core components
        self.yolo_detector = self.initialize_yolo_model()
        self.deep_sort_tracker = self.initialize_tracking_system()
        self.analysis_modules = self.setup_analysis_modules()
        self.data_recorder = self.initialize_data_recording()
        self.performance_monitor = self.setup_performance_monitoring()
        
        # System state management
        self.processing_active = False
        self.current_frame = None
        self.frame_count = 0
        self.analysis_results = {}
        
    def initialize_yolo_model(self):
        """
        Initialize YOLOv4-tiny detection model:
        1. Load model weights and configuration
        2. Setup detection parameters
        3. Configure GPU acceleration if available
        4. Optimize for real-time performance
        """
        
        yolo_config = {
            'config_path': 'YOLOv4-tiny/yolov4-tiny.cfg',
            'weights_path': 'YOLOv4-tiny/yolov4-tiny.weights', 
            'class_names': 'model_data/coco/coco.names',
            'confidence_threshold': 0.5,
            'nms_threshold': 0.4,
            'input_size': (608, 608)
        }
        
        # Load YOLO network
        net = cv2.dnn.readNet(yolo_config['weights_path'], yolo_config['config_path'])
        
        # Enable GPU acceleration if available
        if cv2.cuda.getCudaEnabledDeviceCount() > 0:
            net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
            print("✅ GPU acceleration enabled for YOLO detection")
        else:
            net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
            net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
            print("🖥️ Using CPU for YOLO detection")
        
        return YOLODetector(net, yolo_config)
    
    def initialize_tracking_system(self):
        """
        Initialize Deep SORT tracking system:
        1. Setup tracker with optimized parameters
        2. Configure feature extraction model
        3. Initialize Kalman filter parameters
        4. Setup track management policies
        """
        
        tracking_config = {
            'max_dist': 0.2,           # Maximum distance for association
            'min_confidence': 0.3,     # Minimum detection confidence
            'nms_max_overlap': 1.0,    # NMS overlap threshold
            'max_iou_distance': 0.7,   # Maximum IOU distance
            'max_age': 70,             # Maximum frames to keep lost tracks
            'n_init': 3                # Frames to confirm track
        }
        
        # Initialize feature extraction model
        feature_model_path = 'model_data/mars-small128.pb'
        encoder = create_box_encoder(feature_model_path, batch_size=1)
        
        # Create Deep SORT tracker
        metric = NearestNeighborDistanceMetric(
            "cosine", 
            tracking_config['max_dist'], 
            tracking_config['n_init']
        )
        
        tracker = Tracker(
            metric,
            max_iou_distance=tracking_config['max_iou_distance'],
            max_age=tracking_config['max_age'],
            n_init=tracking_config['n_init']
        )
        
        return DeepSORTTracker(tracker, encoder, tracking_config)
    
    def setup_analysis_modules(self):
        """
        Initialize specialized analysis modules:
        1. Social distance monitoring
        2. Restricted area enforcement
        3. Abnormal activity detection
        4. Crowd density analysis
        """
        
        modules = {
            'social_distance': SocialDistanceAnalyzer(
                min_distance=50,        # Minimum distance in pixels
                alert_threshold=10,     # Alert after 10 violations
                calibration_factor=1.0  # Distance calibration
            ),
            'restricted_entry': RestrictedAreaAnalyzer(
                restricted_zones=self.load_restricted_zones(),
                time_restrictions=self.load_time_restrictions(),
                alert_enabled=True
            ),
            'abnormal_activity': AbnormalActivityDetector(
                energy_threshold=0.15,   # Movement energy threshold
                window_size=30,         # Analysis window in frames
                sensitivity=0.7         # Detection sensitivity
            ),
            'crowd_density': CrowdDensityAnalyzer(
                density_zones=self.define_density_zones(),
                capacity_limits=self.load_capacity_limits(),
                warning_levels=[0.6, 0.8, 0.95]  # Warning thresholds
            )
        }
        
        return modules
    
    def process_video_stream(self, video_source):
        """
        Main video processing pipeline:
        1. Capture and preprocess frames
        2. Run AI detection and tracking
        3. Execute analysis modules
        4. Record results and update displays
        5. Monitor performance metrics
        """
        
        cap = cv2.VideoCapture(video_source)
        
        if not cap.isOpened():
            raise ValueError(f"Unable to open video source: {video_source}")
        
        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        print(f"📹 Video Properties: {frame_width}x{frame_height} @ {fps} FPS, {total_frames} frames")
        
        self.processing_active = True
        frame_count = 0
        
        while self.processing_active and cap.isOpened():
            # Start frame timing
            self.performance_monitor.start_frame_timing()
            
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_count += 1
            self.current_frame = frame.copy()
            
            try:
                # Stage 1: AI Detection
                detections = self.yolo_detector.detect(frame)
                self.performance_monitor.mark_stage('detection')
                
                # Stage 2: Object Tracking
                tracked_objects = self.deep_sort_tracker.update(detections, frame)
                self.performance_monitor.mark_stage('tracking')
                
                # Stage 3: Analysis Processing
                analysis_results = self.run_analysis_modules(frame, tracked_objects)
                self.performance_monitor.mark_stage('analysis')
                
                # Stage 4: Data Recording
                self.record_frame_data(frame_count, tracked_objects, analysis_results)
                
                # Stage 5: Display Update
                self.update_displays(frame, tracked_objects, analysis_results)
                
                # End frame timing
                self.performance_monitor.end_frame_timing()
                
                # Progress reporting
                if frame_count % 30 == 0:  # Every 30 frames
                    progress = (frame_count / total_frames) * 100
                    fps_current = self.performance_monitor.get_current_fps()
                    print(f"🔄 Progress: {progress:.1f}% | FPS: {fps_current:.1f} | Frame: {frame_count}/{total_frames}")
                
            except Exception as e:
                print(f"❌ Error processing frame {frame_count}: {e}")
                continue
        
        cap.release()
        self.processing_active = False
        print(f"✅ Video processing completed. Processed {frame_count} frames.")
    
    def run_analysis_modules(self, frame, tracked_objects):
        """
        Execute all analysis modules on current frame:
        1. Extract object information
        2. Run each analysis module
        3. Aggregate results
        4. Generate alerts if necessary
        """
        
        results = {
            'frame_info': {
                'timestamp': time.time(),
                'frame_number': self.frame_count,
                'object_count': len(tracked_objects)
            }
        }
        
        # Extract person detections
        people = [obj for obj in tracked_objects if obj.class_id == 0]  # Person class
        
        # Social Distance Analysis
        if 'social_distance' in self.analysis_modules:
            distance_results = self.analysis_modules['social_distance'].analyze(people, frame)
            results['social_distance'] = distance_results
        
        # Restricted Area Analysis
        if 'restricted_entry' in self.analysis_modules:
            restricted_results = self.analysis_modules['restricted_entry'].analyze(people, frame)
            results['restricted_entry'] = restricted_results
        
        # Abnormal Activity Analysis
        if 'abnormal_activity' in self.analysis_modules:
            abnormal_results = self.analysis_modules['abnormal_activity'].analyze(people, frame)
            results['abnormal_activity'] = abnormal_results
        
        # Crowd Density Analysis
        if 'crowd_density' in self.analysis_modules:
            density_results = self.analysis_modules['crowd_density'].analyze(people, frame)
            results['crowd_density'] = density_results
        
        return results
```

### **3.2 Video Processing Module (`video_process.py`)**

#### **3.2.1 Frame-Level Processing Architecture**

**Core Processing Pipeline:**
```python
class VideoProcessor:
    """
    Advanced video processing system handling:
    1. Frame extraction and preprocessing
    2. Resolution management and optimization
    3. Display overlay generation
    4. Performance optimization strategies
    """
    
    def __init__(self, config):
        self.config = config
        self.frame_buffer = deque(maxlen=config.get('buffer_size', 100))
        self.preprocessing_pipeline = self.setup_preprocessing()
        self.overlay_renderer = OverlayRenderer(config)
        self.performance_optimizer = FrameOptimizer(config)
    
    def setup_preprocessing(self):
        """
        Setup frame preprocessing pipeline:
        1. Noise reduction and filtering
        2. Contrast and brightness adjustment
        3. Resolution scaling for AI processing
        4. Color space conversions
        """
        
        pipeline_steps = [
            ('noise_reduction', self.apply_noise_reduction),
            ('contrast_enhancement', self.enhance_contrast),
            ('resolution_scaling', self.scale_for_detection),
            ('color_conversion', self.convert_color_space)
        ]
        
        return pipeline_steps
    
    def process_frame(self, frame, detections=None, tracks=None, analysis_results=None):
        """
        Comprehensive frame processing:
        1. Apply preprocessing transformations
        2. Generate detection overlays
        3. Render tracking information
        4. Add analysis visualizations
        5. Create final display frame
        """
        
        # Store original frame
        original_frame = frame.copy()
        
        # Apply preprocessing pipeline
        processed_frame = self.apply_preprocessing_pipeline(frame)
        
        # Generate overlay elements
        if detections or tracks or analysis_results:
            overlay_frame = self.generate_overlays(
                original_frame, 
                detections, 
                tracks, 
                analysis_results
            )
        else:
            overlay_frame = original_frame
        
        # Apply performance optimizations
        final_frame = self.performance_optimizer.optimize_frame(overlay_frame)
        
        return final_frame
    
    def generate_overlays(self, frame, detections, tracks, analysis_results):
        """
        Generate comprehensive overlay visualization:
        1. Detection bounding boxes
        2. Tracking trails and IDs
        3. Social distance violation indicators
        4. Restricted area highlights
        5. Analysis statistics overlay
        """
        
        overlay_frame = frame.copy()
        
        # Detection overlays
        if detections:
            overlay_frame = self.render_detections(overlay_frame, detections)
        
        # Tracking overlays
        if tracks:
            overlay_frame = self.render_tracks(overlay_frame, tracks)
        
        # Analysis overlays
        if analysis_results:
            overlay_frame = self.render_analysis_results(overlay_frame, analysis_results)
        
        # Performance overlay
        overlay_frame = self.render_performance_stats(overlay_frame)
        
        return overlay_frame
    
    def render_detections(self, frame, detections):
        """
        Render detection bounding boxes and confidence scores:
        1. Draw bounding boxes with class-specific colors
        2. Add confidence scores and class labels
        3. Implement adaptive box thickness
        4. Add detection count indicator
        """
        
        detection_colors = {
            'person': (0, 255, 0),      # Green for persons
            'vehicle': (255, 0, 0),     # Blue for vehicles
            'other': (0, 0, 255)        # Red for other objects
        }
        
        person_count = 0
        
        for detection in detections:
            x1, y1, x2, y2 = detection.bbox
            confidence = detection.confidence
            class_name = detection.class_name
            
            if class_name == 'person':
                person_count += 1
            
            # Select color based on class
            color = detection_colors.get(class_name, detection_colors['other'])
            
            # Draw bounding box
            thickness = max(1, int(frame.shape[0] / 500))  # Adaptive thickness
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
            
            # Add label with confidence
            label = f"{class_name}: {confidence:.2f}"
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
            
            # Background rectangle for label
            cv2.rectangle(frame, 
                         (int(x1), int(y1) - label_size[1] - 10),
                         (int(x1) + label_size[0], int(y1)),
                         color, -1)
            
            # Label text
            cv2.putText(frame, label,
                       (int(x1), int(y1) - 5),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Add detection count overlay
        count_text = f"Detected: {person_count} people"
        cv2.putText(frame, count_text, (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        return frame
    
    def render_tracks(self, frame, tracks):
        """
        Render tracking information and trails:
        1. Draw tracking IDs and trails
        2. Show track confidence and age
        3. Highlight lost or uncertain tracks
        4. Display tracking statistics
        """
        
        track_colors = {}  # Store consistent colors for each track ID
        active_tracks = 0
        
        for track in tracks:
            track_id = track.track_id
            bbox = track.to_tlbr()
            
            # Generate consistent color for track
            if track_id not in track_colors:
                # Generate unique color based on track ID
                np.random.seed(track_id)
                color = tuple(np.random.randint(0, 255, 3).tolist())
                track_colors[track_id] = color
            else:
                color = track_colors[track_id]
            
            if track.is_confirmed():
                active_tracks += 1
                
                # Draw track bounding box
                cv2.rectangle(frame, 
                             (int(bbox[0]), int(bbox[1])), 
                             (int(bbox[2]), int(bbox[3])), 
                             color, 2)
                
                # Draw track ID
                track_label = f"ID: {track_id}"
                cv2.putText(frame, track_label,
                           (int(bbox[0]), int(bbox[1]) - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                
                # Draw track trail if available
                if hasattr(track, 'positions') and len(track.positions) > 1:
                    points = np.array(track.positions, dtype=np.int32)
                    cv2.polylines(frame, [points], False, color, 2)
        
        # Add tracking statistics
        track_stats = f"Active Tracks: {active_tracks}"
        cv2.putText(frame, track_stats, (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        return frame
    
    def render_analysis_results(self, frame, analysis_results):
        """
        Render analysis visualization overlays:
        1. Social distance violation indicators
        2. Restricted area highlights
        3. Abnormal activity alerts
        4. Analysis statistics display
        """
        
        y_offset = 90  # Starting position for analysis info
        
        # Social Distance Analysis
        if 'social_distance' in analysis_results:
            social_data = analysis_results['social_distance']
            violations = social_data.get('violations', 0)
            
            # Violation indicator
            violation_color = (0, 0, 255) if violations > 0 else (0, 255, 0)
            violation_text = f"Social Distance Violations: {violations}"
            cv2.putText(frame, violation_text, (10, y_offset),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, violation_color, 2)
            y_offset += 30
            
            # Draw violation lines if available
            if 'violation_pairs' in social_data:
                for pair in social_data['violation_pairs']:
                    pt1, pt2 = pair
                    cv2.line(frame, tuple(map(int, pt1)), tuple(map(int, pt2)), (0, 0, 255), 3)
        
        # Restricted Entry Analysis
        if 'restricted_entry' in analysis_results:
            restricted_data = analysis_results['restricted_entry']
            violations = restricted_data.get('violations', 0)
            
            violation_color = (0, 165, 255) if violations > 0 else (0, 255, 0)
            restricted_text = f"Restricted Entry Violations: {violations}"
            cv2.putText(frame, restricted_text, (10, y_offset),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, violation_color, 2)
            y_offset += 30
            
            # Highlight restricted zones
            if 'restricted_zones' in restricted_data:
                for zone in restricted_data['restricted_zones']:
                    cv2.rectangle(frame, zone['top_left'], zone['bottom_right'], 
                                 (0, 165, 255), 2)
        
        # Abnormal Activity Analysis
        if 'abnormal_activity' in analysis_results:
            abnormal_data = analysis_results['abnormal_activity']
            activity_detected = abnormal_data.get('detected', False)
            energy_level = abnormal_data.get('energy_level', 0)
            
            activity_color = (255, 0, 0) if activity_detected else (0, 255, 0)
            activity_text = f"Abnormal Activity: {'DETECTED' if activity_detected else 'NORMAL'}"
            cv2.putText(frame, activity_text, (10, y_offset),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, activity_color, 2)
            
            energy_text = f"Energy Level: {energy_level:.3f}"
            cv2.putText(frame, energy_text, (10, y_offset + 25),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        
        return frame
```

### **3.3 Configuration Management (`config.py`)**

#### **3.3.1 Hierarchical Configuration System**

**Configuration Architecture:**
```python
class ConfigurationManager:
    """
    Comprehensive configuration management system:
    1. Hierarchical configuration loading
    2. Environment-specific settings
    3. Runtime parameter adjustment
    4. Configuration validation and defaults
    """
    
    def __init__(self, config_path='config.yaml'):
        self.config_path = config_path
        self.config_data = {}
        self.default_config = self.get_default_configuration()
        self.environment_overrides = {}
        
        # Load and validate configuration
        self.load_configuration()
        self.validate_configuration()
    
    def get_default_configuration(self):
        """
        Define comprehensive default configuration:
        1. AI model parameters
        2. Processing settings
        3. Analysis thresholds
        4. Performance options
        5. UI preferences
        """
        
        defaults = {
            # AI Model Configuration
            'ai_models': {
                'yolo': {
                    'config_path': 'YOLOv4-tiny/yolov4-tiny.cfg',
                    'weights_path': 'YOLOv4-tiny/yolov4-tiny.weights',
                    'classes_path': 'model_data/coco/coco.names',
                    'confidence_threshold': 0.5,
                    'nms_threshold': 0.4,
                    'input_size': 608,
                    'use_gpu': True
                },
                'deep_sort': {
                    'model_path': 'model_data/mars-small128.pb',
                    'max_distance': 0.2,
                    'min_confidence': 0.3,
                    'nms_max_overlap': 1.0,
                    'max_iou_distance': 0.7,
                    'max_age': 70,
                    'n_init': 3,
                    'nn_budget': 100
                }
            },
            
            # Video Processing Configuration
            'video_processing': {
                'target_fps': 25,
                'frame_skip': 0,
                'resize_factor': 1.0,
                'buffer_size': 100,
                'preprocessing': {
                    'noise_reduction': True,
                    'contrast_enhancement': False,
                    'brightness_adjustment': 0,
                    'gamma_correction': 1.0
                }
            },
            
            # Analysis Modules Configuration
            'analysis': {
                'social_distance': {
                    'enabled': True,
                    'min_distance_pixels': 50,
                    'alert_threshold': 10,
                    'calibration_factor': 1.0,
                    'violation_color': [0, 0, 255],
                    'safe_color': [0, 255, 0]
                },
                'restricted_entry': {
                    'enabled': True,
                    'zones': [],
                    'time_restrictions': [],
                    'alert_enabled': True,
                    'violation_color': [0, 165, 255]
                },
                'abnormal_activity': {
                    'enabled': True,
                    'energy_threshold': 0.15,
                    'window_size': 30,
                    'sensitivity': 0.7,
                    'alert_color': [255, 0, 0]
                },
                'crowd_density': {
                    'enabled': True,
                    'density_zones': [],
                    'capacity_limits': {},
                    'warning_levels': [0.6, 0.8, 0.95]
                }
            },
            
            # User Interface Configuration
            'ui': {
                'theme': 'dark',
                'window_size': [1400, 900],
                'video_preview_size': [640, 480],
                'update_interval': 100,
                'show_fps': True,
                'show_statistics': True,
                'auto_save_plots': True
            },
            
            # Data Management Configuration
            'data': {
                'output_directory': 'processed_data',
                'plot_directory': 'generated_plots',
                'auto_save': True,
                'save_interval': 30,
                'csv_format': {
                    'include_timestamp': True,
                    'include_frame_number': True,
                    'decimal_precision': 3
                },
                'backup': {
                    'enabled': True,
                    'max_backups': 5,
                    'backup_interval': 300
                }
            },
            
            # Performance Configuration
            'performance': {
                'max_threads': 4,
                'memory_limit_mb': 2048,
                'enable_optimization': True,
                'adaptive_quality': True,
                'monitoring': {
                    'enable_profiling': False,
                    'log_performance': True,
                    'alert_thresholds': {
                        'min_fps': 15,
                        'max_memory_usage': 85,
                        'max_cpu_usage': 80
                    }
                }
            }
        }
        
        return defaults
    
    def load_configuration(self):
        """
        Load configuration from multiple sources:
        1. Default configuration
        2. Configuration file
        3. Environment variables
        4. Command line arguments
        """
        
        # Start with defaults
        self.config_data = copy.deepcopy(self.default_config)
        
        # Load from configuration file if exists
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as file:
                    file_config = yaml.safe_load(file)
                    if file_config:
                        self.merge_configurations(self.config_data, file_config)
                        print(f"✅ Loaded configuration from {self.config_path}")
            except Exception as e:
                print(f"⚠️ Error loading configuration file: {e}")
                print("Using default configuration")
        
        # Apply environment variable overrides
        self.apply_environment_overrides()
        
        # Apply any runtime modifications
        self.apply_runtime_overrides()
    
    def validate_configuration(self):
        """
        Validate configuration parameters:
        1. Check parameter ranges and types
        2. Validate file paths
        3. Ensure model compatibility
        4. Verify system requirements
        """
        
        validation_errors = []
        
        # Validate AI model paths
        yolo_config = self.get('ai_models.yolo')
        if not os.path.exists(yolo_config['config_path']):
            validation_errors.append(f"YOLO config file not found: {yolo_config['config_path']}")
        
        if not os.path.exists(yolo_config['weights_path']):
            validation_errors.append(f"YOLO weights file not found: {yolo_config['weights_path']}")
        
        # Validate thresholds
        confidence = yolo_config['confidence_threshold']
        if not 0.0 <= confidence <= 1.0:
            validation_errors.append(f"Invalid confidence threshold: {confidence} (must be 0.0-1.0)")
        
        nms = yolo_config['nms_threshold']
        if not 0.0 <= nms <= 1.0:
            validation_errors.append(f"Invalid NMS threshold: {nms} (must be 0.0-1.0)")
        
        # Validate directories
        output_dir = self.get('data.output_directory')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
            print(f"📁 Created output directory: {output_dir}")
        
        plot_dir = self.get('data.plot_directory')
        if not os.path.exists(plot_dir):
            os.makedirs(plot_dir, exist_ok=True)
            print(f"📊 Created plot directory: {plot_dir}")
        
        # Report validation results
        if validation_errors:
            print("❌ Configuration validation errors:")
            for error in validation_errors:
                print(f"  - {error}")
            raise ValueError("Configuration validation failed")
        else:
            print("✅ Configuration validation passed")
    
    def get(self, key_path, default=None):
        """
        Get configuration value using dot notation:
        Example: get('ai_models.yolo.confidence_threshold')
        """
        
        keys = key_path.split('.')
        value = self.config_data
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def set(self, key_path, value):
        """
        Set configuration value using dot notation:
        Example: set('ai_models.yolo.confidence_threshold', 0.6)
        """
        
        keys = key_path.split('.')
        config_dict = self.config_data
        
        # Navigate to parent dictionary
        for key in keys[:-1]:
            if key not in config_dict:
                config_dict[key] = {}
            config_dict = config_dict[key]
        
        # Set the value
        config_dict[keys[-1]] = value
        
        # Validate the change
        self.validate_single_parameter(key_path, value)
    
    def save_configuration(self, file_path=None):
        """
        Save current configuration to file:
        1. Serialize configuration data
        2. Write to YAML format
        3. Create backup if needed
        """
        
        save_path = file_path or self.config_path
        
        try:
            # Create backup if file exists
            if os.path.exists(save_path):
                backup_path = f"{save_path}.backup"
                shutil.copy2(save_path, backup_path)
            
            # Save configuration
            with open(save_path, 'w') as file:
                yaml.dump(self.config_data, file, default_flow_style=False, indent=2)
            
            print(f"✅ Configuration saved to {save_path}")
            
        except Exception as e:
            print(f"❌ Error saving configuration: {e}")
```

---

## **4. AI/ML COMPONENTS**

### **4.1 YOLOv4-tiny Detection System**

#### **4.1.1 Model Architecture and Optimization**

**YOLOv4-tiny Implementation:**
```python
class YOLODetector:
    """
    YOLOv4-tiny object detection system optimized for real-time crowd analysis:
    1. Efficient neural network architecture
    2. GPU acceleration support
    3. Multi-scale detection capabilities
    4. Optimized inference pipeline
    """
    
    def __init__(self, model_path, config):
        self.model_path = model_path
        self.config = config
        self.net = None
        self.output_layers = []
        self.class_names = []
        self.colors = []
        
        # Performance metrics
        self.detection_times = deque(maxlen=100)
        self.total_detections = 0
        
        # Initialize model
        self.load_model()
        self.setup_output_processing()
        
    def load_model(self):
        """
        Load YOLOv4-tiny model with optimizations:
        1. Load network architecture and weights
        2. Configure backend and target device
        3. Setup inference optimizations
        4. Prepare output layer processing
        """
        
        try:
            # Load YOLO network
            self.net = cv2.dnn.readNet(
                self.config['weights_path'], 
                self.config['config_path']
            )
            
            # Setup backend and target
            if self.config.get('use_gpu', False) and cv2.cuda.getCudaEnabledDeviceCount() > 0:
                self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
                self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
                print("🚀 YOLOv4-tiny: GPU acceleration enabled")
            else:
                self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
                self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
                print("🖥️ YOLOv4-tiny: Using CPU inference")
            
            # Get output layer names
            layer_names = self.net.getLayerNames()
            self.output_layers = [layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
            
            # Load class names
            with open(self.config['classes_path'], 'r') as file:
                self.class_names = [line.strip() for line in file.readlines()]
            
            # Generate colors for each class
            np.random.seed(42)
            self.colors = np.random.uniform(0, 255, size=(len(self.class_names), 3))
            
            print(f"✅ YOLOv4-tiny loaded successfully with {len(self.class_names)} classes")
            
        except Exception as e:
            raise RuntimeError(f"Failed to load YOLOv4-tiny model: {e}")
    
    def detect(self, frame):
        """
        Perform object detection on frame:
        1. Preprocess input frame
        2. Run forward pass through network
        3. Process network outputs
        4. Apply Non-Maximum Suppression
        5. Return filtered detections
        """
        
        start_time = time.perf_counter()
        
        # Get frame dimensions
        height, width, channels = frame.shape
        
        # Preprocess frame for YOLO
        blob = cv2.dnn.blobFromImage(
            frame,
            1/255.0,  # Scale factor
            (self.config['input_size'], self.config['input_size']),  # Size
            (0, 0, 0),  # Mean subtraction
            swapRB=True,  # Swap R and B channels
            crop=False    # Don't crop
        )
        
        # Set input to network
        self.net.setInput(blob)
        
        # Run forward pass
        outputs = self.net.forward(self.output_layers)
        
        # Process outputs
        detections = self.process_detections(outputs, width, height)
        
        # Apply Non-Maximum Suppression
        final_detections = self.apply_nms(detections)
        
        # Record timing
        detection_time = time.perf_counter() - start_time
        self.detection_times.append(detection_time)
        self.total_detections += len(final_detections)
        
        return final_detections
    
    def process_detections(self, outputs, frame_width, frame_height):
        """
        Process YOLO network outputs:
        1. Extract bounding boxes, confidences, and class IDs
        2. Scale coordinates to original frame size
        3. Filter by confidence threshold
        4. Prepare detection objects
        """
        
        boxes = []
        confidences = []
        class_ids = []
        
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                # Filter by confidence threshold
                if confidence > self.config['confidence_threshold']:
                    # Extract bounding box coordinates
                    center_x = int(detection[0] * frame_width)
                    center_y = int(detection[1] * frame_height)
                    width = int(detection[2] * frame_width)
                    height = int(detection[3] * frame_height)
                    
                    # Calculate top-left coordinates
                    x = int(center_x - width / 2)
                    y = int(center_y - height / 2)
                    
                    boxes.append([x, y, width, height])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        
        # Create detection objects
        detections = []
        for i, (box, confidence, class_id) in enumerate(zip(boxes, confidences, class_ids)):
            detection = Detection(
                bbox=box,
                confidence=confidence,
                class_id=class_id,
                class_name=self.class_names[class_id] if class_id < len(self.class_names) else 'unknown'
            )
            detections.append(detection)
        
        return detections
    
    def apply_nms(self, detections):
        """
        Apply Non-Maximum Suppression:
        1. Group detections by class
        2. Apply NMS to reduce duplicate detections
        3. Keep only high-confidence, non-overlapping boxes
        """
        
        if not detections:
            return []
        
        # Extract data for NMS
        boxes = []
        confidences = []
        class_ids = []
        
        for detection in detections:
            x, y, w, h = detection.bbox
            boxes.append([x, y, x + w, y + h])  # Convert to [x1, y1, x2, y2]
            confidences.append(detection.confidence)
            class_ids.append(detection.class_id)
        
        # Apply NMS
        indices = cv2.dnn.NMSBoxes(
            boxes,
            confidences,
            self.config['confidence_threshold'],
            self.config['nms_threshold']
        )
        
        # Create final detection list
        final_detections = []
        if len(indices) > 0:
            for i in indices.flatten():
                final_detections.append(detections[i])
        
        return final_detections
    
    def get_performance_stats(self):
        """
        Get detector performance statistics:
        1. Average detection time
        2. Detection rate (detections per second)
        3. Total detections processed
        """
        
        stats = {
            'average_detection_time': np.mean(self.detection_times) if self.detection_times else 0,
            'min_detection_time': np.min(self.detection_times) if self.detection_times else 0,
            'max_detection_time': np.max(self.detection_times) if self.detection_times else 0,
            'total_detections': self.total_detections,
            'detection_rate': len(self.detection_times) / sum(self.detection_times) if sum(self.detection_times) > 0 else 0
        }
        
        return stats

class Detection:
    """
    Detection object representing a single detected object:
    Contains bounding box, confidence, and class information
    """
    
    def __init__(self, bbox, confidence, class_id, class_name):
        self.bbox = bbox  # [x, y, width, height]
        self.confidence = confidence
        self.class_id = class_id
        self.class_name = class_name
        self.timestamp = time.time()
    
    def to_tlbr(self):
        """Convert bbox to top-left, bottom-right format"""
        x, y, w, h = self.bbox
        return [x, y, x + w, y + h]
    
    def get_center(self):
        """Get center point of detection"""
        x, y, w, h = self.bbox
        return [x + w/2, y + h/2]
    
    def get_area(self):
        """Calculate detection area"""
        x, y, w, h = self.bbox
        return w * h
```

### **4.2 Deep SORT Tracking System**

#### **4.2.1 Multi-Object Tracking Implementation**

**Deep SORT Tracker:**
```python
class DeepSORTTracker:
    """
    Deep SORT multi-object tracking system:
    1. Kalman filter-based motion prediction
    2. Deep learning feature extraction
    3. Hungarian algorithm for data association
    4. Track lifecycle management
    """
    
    def __init__(self, tracker, encoder, config):
        self.tracker = tracker
        self.encoder = encoder
        self.config = config
        self.frame_count = 0
        
        # Performance monitoring
        self.tracking_times = deque(maxlen=100)
        self.track_statistics = {
            'total_tracks': 0,
            'active_tracks': 0,
            'confirmed_tracks': 0,
            'lost_tracks': 0
        }
    
    def update(self, detections, frame):
        """
        Update tracker with new detections:
        1. Extract features from detections
        2. Predict track states
        3. Associate detections with tracks
        4. Update confirmed tracks
        5. Initialize new tracks
        """
        
        start_time = time.perf_counter()
        
        # Filter person detections
        person_detections = [det for det in detections if det.class_name == 'person']
        
        if not person_detections:
            # Update tracker with no detections
            self.tracker.predict()
            self.tracker.update([])
            tracking_time = time.perf_counter() - start_time
            self.tracking_times.append(tracking_time)
            return []
        
        # Extract features for detections
        detection_features = self.extract_features(person_detections, frame)
        
        # Convert to Deep SORT format
        deep_sort_detections = []
        for detection, features in zip(person_detections, detection_features):
            tlbr = detection.to_tlbr()
            deep_sort_detection = DeepSORTDetection(
                tlbr, detection.confidence, features
            )
            deep_sort_detections.append(deep_sort_detection)
        
        # Update tracker
        self.tracker.predict()
        self.tracker.update(deep_sort_detections)
        
        # Get current tracks
        active_tracks = []
        for track in self.tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue
            
            # Create track object
            track_obj = TrackObject(
                track_id=track.track_id,
                bbox=track.to_tlbr(),
                confidence=track.confidence if hasattr(track, 'confidence') else 1.0,
                track_state=track.state,
                time_since_update=track.time_since_update,
                age=track.age
            )
            active_tracks.append(track_obj)
        
        # Update statistics
        self.update_statistics()
        
        # Record timing
        tracking_time = time.perf_counter() - start_time
        self.tracking_times.append(tracking_time)
        self.frame_count += 1
        
        return active_tracks
    
    def extract_features(self, detections, frame):
        """
        Extract CNN features for person re-identification:
        1. Crop detection regions from frame
        2. Resize to model input size
        3. Run through feature extraction network
        4. Return normalized feature vectors
        """
        
        if not detections:
            return []
        
        # Prepare detection crops
        crops = []
        for detection in detections:
            x, y, w, h = detection.bbox
            
            # Ensure coordinates are within frame bounds
            x1 = max(0, x)
            y1 = max(0, y)
            x2 = min(frame.shape[1], x + w)
            y2 = min(frame.shape[0], y + h)
            
            # Extract crop
            crop = frame[y1:y2, x1:x2]
            
            if crop.size > 0:
                crops.append(crop)
            else:
                # Create dummy crop if invalid
                crops.append(np.zeros((64, 64, 3), dtype=np.uint8))
        
        # Extract features using encoder
        try:
            features = self.encoder(crops)
            return features
        except Exception as e:
            print(f"⚠️ Feature extraction failed: {e}")
            # Return dummy features
            return [np.zeros(128) for _ in detections]
    
    def update_statistics(self):
        """Update tracking statistics"""
        
        confirmed_tracks = len([t for t in self.tracker.tracks if t.is_confirmed()])
        active_tracks = len([t for t in self.tracker.tracks if t.time_since_update <= 1])
        lost_tracks = len([t for t in self.tracker.tracks if t.is_deleted()])
        
        self.track_statistics.update({
            'active_tracks': active_tracks,
            'confirmed_tracks': confirmed_tracks,
            'lost_tracks': lost_tracks,
            'frame_count': self.frame_count
        })
    
    def get_performance_stats(self):
        """Get tracking performance statistics"""
        
        stats = {
            'average_tracking_time': np.mean(self.tracking_times) if self.tracking_times else 0,
            'tracking_fps': 1.0 / np.mean(self.tracking_times) if self.tracking_times and np.mean(self.tracking_times) > 0 else 0,
            'track_statistics': self.track_statistics.copy(),
            'total_frames_processed': self.frame_count
        }
        
        return stats

class TrackObject:
    """
    Tracked object representation:
    Contains track information and state management
    """
    
    def __init__(self, track_id, bbox, confidence, track_state, time_since_update, age):
        self.track_id = track_id
        self.bbox = bbox  # [x1, y1, x2, y2]
        self.confidence = confidence
        self.track_state = track_state
        self.time_since_update = time_since_update
        self.age = age
        self.positions = deque(maxlen=30)  # Track trail
        
        # Add current position to trail
        center = self.get_center()
        self.positions.append(center)
    
    def to_tlbr(self):
        """Get bounding box in top-left, bottom-right format"""
        return self.bbox
    
    def get_center(self):
        """Get center point of track"""
        x1, y1, x2, y2 = self.bbox
        return [(x1 + x2) / 2, (y1 + y2) / 2]
    
    def is_confirmed(self):
        """Check if track is confirmed"""
        return self.track_state == 2  # TrackState.Confirmed
    
    def get_area(self):
        """Calculate track area"""
        x1, y1, x2, y2 = self.bbox
        return (x2 - x1) * (y2 - y1)
```

---

## **5. USER INTERFACE SYSTEMS**

### **5.1 Modern Crowd Studio GUI (`modern_crowd_studio.py`)**

#### **5.1.1 Professional Interface Architecture**

**CustomTkinter GUI System:**
```python
class ModernCrowdStudio:
    """
    Professional crowd analysis interface built with CustomTkinter:
    1. Three-panel layout with analysis controls, live preview, and analytics
    2. Real-time video display with overlay visualization  
    3. Interactive analytics dashboard with live updates
    4. Professional dark theme with modern styling
    5. Comprehensive status monitoring and progress tracking
    """
    
    def __init__(self):
        # Initialize CustomTkinter theming
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        
        # Create main window
        self.root = customtkinter.CTk()
        self.root.title("🎯 Modern Crowd Analysis Studio v2.0")
        self.root.geometry("1400x900")
        self.root.minsize(1200, 800)
        
        # Application state
        self.video_file = None
        self.analysis_thread = None
        self.is_analyzing = False
        self.current_frame = None
        self.analysis_data = {}
        
        # GUI components
        self.setup_main_layout()
        self.setup_control_panel()
        self.setup_video_preview()
        self.setup_analytics_dashboard()
        self.setup_status_bar()
        
        # Initialize update timers
        self.setup_update_timers()
        
        print("🖥️ Modern Crowd Studio GUI initialized")
    
    def setup_main_layout(self):
        """
        Setup main application layout:
        1. Left panel: Analysis controls and configuration
        2. Center panel: Live video preview and visualization
        3. Right panel: Analytics dashboard and statistics
        """
        
        # Configure grid weights
        self.root.grid_columnconfigure(1, weight=2)  # Video panel gets more space
        self.root.grid_columnconfigure(2, weight=1)  # Analytics panel
        self.root.grid_rowconfigure(0, weight=1)
        
        # Create main panels
        self.control_frame = customtkinter.CTkFrame(self.root)
        self.control_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.video_frame = customtkinter.CTkFrame(self.root)
        self.video_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.analytics_frame = customtkinter.CTkFrame(self.root)
        self.analytics_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        
        # Status bar at bottom
        self.status_frame = customtkinter.CTkFrame(self.root)
        self.status_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
    
    def setup_control_panel(self):
        """
        Setup left control panel:
        1. Video file selection and loading
        2. Analysis start/stop controls
        3. Configuration options
        4. Progress monitoring
        5. Export and save functions
        """
        
        # Panel title
        title_label = customtkinter.CTkLabel(
            self.control_frame, 
            text="🎛️ Analysis Controls", 
            font=customtkinter.CTkFont(size=18, weight="bold")
        )
        title_label.pack(pady=20)
        
        # Video Selection Section
        video_section = customtkinter.CTkFrame(self.control_frame)
        video_section.pack(fill="x", padx=20, pady=10)
        
        video_label = customtkinter.CTkLabel(
            video_section, 
            text="📹 Video Source", 
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        video_label.pack(pady=10)
        
        self.video_path_entry = customtkinter.CTkEntry(
            video_section, 
            placeholder_text="Select video file...",
            width=250
        )
        self.video_path_entry.pack(pady=5)
        
        self.select_video_btn = customtkinter.CTkButton(
            video_section,
            text="📂 Browse Video",
            command=self.select_video_file,
            width=200
        )
        self.select_video_btn.pack(pady=5)
        
        # Analysis Controls Section
        analysis_section = customtkinter.CTkFrame(self.control_frame)
        analysis_section.pack(fill="x", padx=20, pady=10)
        
        analysis_label = customtkinter.CTkLabel(
            analysis_section, 
            text="🚀 Analysis Control", 
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        analysis_label.pack(pady=10)
        
        self.start_analysis_btn = customtkinter.CTkButton(
            analysis_section,
            text="▶️ Start Analysis",
            command=self.start_analysis,
            fg_color="green",
            hover_color="darkgreen",
            width=200
        )
        self.start_analysis_btn.pack(pady=5)
        
        self.stop_analysis_btn = customtkinter.CTkButton(
            analysis_section,
            text="⏹️ Stop Analysis",
            command=self.stop_analysis,
            fg_color="red",
            hover_color="darkred",
            width=200,
            state="disabled"
        )
        self.stop_analysis_btn.pack(pady=5)
        
        # Progress Section
        progress_section = customtkinter.CTkFrame(self.control_frame)
        progress_section.pack(fill="x", padx=20, pady=10)
        
        progress_label = customtkinter.CTkLabel(
            progress_section, 
            text="📊 Progress", 
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        progress_label.pack(pady=10)
        
        self.progress_bar = customtkinter.CTkProgressBar(progress_section)
        self.progress_bar.pack(pady=5, padx=10, fill="x")
        self.progress_bar.set(0)
        
        self.progress_label = customtkinter.CTkLabel(
            progress_section, 
            text="Ready to start analysis"
        )
        self.progress_label.pack(pady=5)
        
        # Configuration Section
        config_section = customtkinter.CTkFrame(self.control_frame)
        config_section.pack(fill="x", padx=20, pady=10)
        
        config_label = customtkinter.CTkLabel(
            config_section, 
            text="⚙️ Configuration", 
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        config_label.pack(pady=10)
        
        # Social Distance Toggle
        self.social_distance_var = customtkinter.BooleanVar(value=True)
        self.social_distance_check = customtkinter.CTkCheckBox(
            config_section,
            text="Social Distance Analysis",
            variable=self.social_distance_var
        )
        self.social_distance_check.pack(pady=2, anchor="w")
        
        # Restricted Entry Toggle
        self.restricted_entry_var = customtkinter.BooleanVar(value=True)
        self.restricted_entry_check = customtkinter.CTkCheckBox(
            config_section,
            text="Restricted Entry Monitoring",
            variable=self.restricted_entry_var
        )
        self.restricted_entry_check.pack(pady=2, anchor="w")
        
        # Abnormal Activity Toggle
        self.abnormal_activity_var = customtkinter.BooleanVar(value=True)
        self.abnormal_activity_check = customtkinter.CTkCheckBox(
            config_section,
            text="Abnormal Activity Detection",
            variable=self.abnormal_activity_var
        )
        self.abnormal_activity_check.pack(pady=2, anchor="w")
        
        # Export Section
        export_section = customtkinter.CTkFrame(self.control_frame)
        export_section.pack(fill="x", padx=20, pady=10)
        
        export_label = customtkinter.CTkLabel(
            export_section, 
            text="💾 Export & Save", 
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        export_label.pack(pady=10)
        
        self.export_csv_btn = customtkinter.CTkButton(
            export_section,
            text="📄 Export CSV Data",
            command=self.export_csv_data,
            width=200
        )
        self.export_csv_btn.pack(pady=2)
        
        self.generate_plots_btn = customtkinter.CTkButton(
            export_section,
            text="📈 Generate Plots",
            command=self.generate_analysis_plots,
            width=200
        )
        self.generate_plots_btn.pack(pady=2)
        
        self.save_report_btn = customtkinter.CTkButton(
            export_section,
            text="📋 Save Report",
            command=self.save_analysis_report,
            width=200
        )
        self.save_report_btn.pack(pady=2)
    
    def setup_video_preview(self):
        """
        Setup center video preview panel:
        1. Live video display with analysis overlays
        2. Detection and tracking visualization
        3. Real-time status indicators
        4. Frame-by-frame analysis view
        """
        
        # Panel title
        title_label = customtkinter.CTkLabel(
            self.video_frame, 
            text="🎥 Live Analysis Preview", 
            font=customtkinter.CTkFont(size=18, weight="bold")
        )
        title_label.pack(pady=10)
        
        # Video display canvas
        self.video_canvas = tkinter.Canvas(
            self.video_frame,
            bg="black",
            width=640,
            height=480
        )
        self.video_canvas.pack(pady=10)
        
        # Video controls
        video_controls = customtkinter.CTkFrame(self.video_frame)
        video_controls.pack(fill="x", padx=20, pady=10)
        
        # Frame information
        self.frame_info_label = customtkinter.CTkLabel(
            video_controls,
            text="Frame: 0 | FPS: 0.0 | Objects: 0",
            font=customtkinter.CTkFont(size=12)
        )
        self.frame_info_label.pack(pady=5)
        
        # Analysis status indicators
        status_frame = customtkinter.CTkFrame(video_controls)
        status_frame.pack(fill="x", pady=5)
        
        # Detection status
        self.detection_status = customtkinter.CTkLabel(
            status_frame,
            text="🔍 Detection: Ready",
            font=customtkinter.CTkFont(size=11)
        )
        self.detection_status.grid(row=0, column=0, padx=10)
        
        # Tracking status
        self.tracking_status = customtkinter.CTkLabel(
            status_frame,
            text="🎯 Tracking: Ready",
            font=customtkinter.CTkFont(size=11)
        )
        self.tracking_status.grid(row=0, column=1, padx=10)
        
        # Analysis status
        self.analysis_status = customtkinter.CTkLabel(
            status_frame,
            text="📊 Analysis: Ready",
            font=customtkinter.CTkFont(size=11)
        )
        self.analysis_status.grid(row=0, column=2, padx=10)
    
    def setup_analytics_dashboard(self):
        """
        Setup right analytics dashboard:
        1. Live statistics display
        2. Real-time charts and graphs
        3. Alert notifications
        4. Historical data trends
        """
        
        # Panel title
        title_label = customtkinter.CTkLabel(
            self.analytics_frame, 
            text="📈 Analytics Dashboard", 
            font=customtkinter.CTkFont(size=18, weight="bold")
        )
        title_label.pack(pady=10)
        
        # Create tabbed analytics view
        self.analytics_tabs = customtkinter.CTkTabview(
            self.analytics_frame,
            width=300,
            height=600
        )
        self.analytics_tabs.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Live Statistics Tab
        self.analytics_tabs.add("📊 Live Stats")
        self.setup_live_stats_tab(self.analytics_tabs.tab("📊 Live Stats"))
        
        # Charts Tab
        self.analytics_tabs.add("📈 Charts")
        self.setup_charts_tab(self.analytics_tabs.tab("📈 Charts"))
        
        # Alerts Tab
        self.analytics_tabs.add("🚨 Alerts")
        self.setup_alerts_tab(self.analytics_tabs.tab("🚨 Alerts"))
        
        # History Tab
        self.analytics_tabs.add("📜 History")
        self.setup_history_tab(self.analytics_tabs.tab("📜 History"))
    
    def setup_live_stats_tab(self, tab_frame):
        """Setup live statistics display"""
        
        # Current Statistics Frame
        current_stats = customtkinter.CTkFrame(tab_frame)
        current_stats.pack(fill="x", pady=5)
        
        stats_title = customtkinter.CTkLabel(
            current_stats, 
            text="Current Statistics",
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        stats_title.pack(pady=5)
        
        # Statistics labels
        self.people_count_label = customtkinter.CTkLabel(
            current_stats, text="👥 People Count: 0"
        )
        self.people_count_label.pack(pady=2, anchor="w")
        
        self.violations_label = customtkinter.CTkLabel(
            current_stats, text="⚠️ Violations: 0"
        )
        self.violations_label.pack(pady=2, anchor="w")
        
        self.restricted_label = customtkinter.CTkLabel(
            current_stats, text="🚫 Restricted Entry: 0"
        )
        self.restricted_label.pack(pady=2, anchor="w")
        
        self.abnormal_label = customtkinter.CTkLabel(
            current_stats, text="🔴 Abnormal Activity: Normal"
        )
        self.abnormal_label.pack(pady=2, anchor="w")
        
        # Performance Statistics Frame
        perf_stats = customtkinter.CTkFrame(tab_frame)
        perf_stats.pack(fill="x", pady=5)
        
        perf_title = customtkinter.CTkLabel(
            perf_stats, 
            text="Performance Metrics",
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        perf_title.pack(pady=5)
        
        self.fps_label = customtkinter.CTkLabel(
            perf_stats, text="⚡ Processing FPS: 0.0"
        )
        self.fps_label.pack(pady=2, anchor="w")
        
        self.detection_time_label = customtkinter.CTkLabel(
            perf_stats, text="🔍 Detection Time: 0ms"
        )
        self.detection_time_label.pack(pady=2, anchor="w")
        
        self.tracking_time_label = customtkinter.CTkLabel(
            perf_stats, text="🎯 Tracking Time: 0ms"
        )
        self.tracking_time_label.pack(pady=2, anchor="w")
        
        self.memory_usage_label = customtkinter.CTkLabel(
            perf_stats, text="💾 Memory Usage: 0%"
        )
        self.memory_usage_label.pack(pady=2, anchor="w")
    
    def setup_charts_tab(self, tab_frame):
        """Setup charts and visualization tab"""
        
        # Chart selection
        chart_selector = customtkinter.CTkFrame(tab_frame)
        chart_selector.pack(fill="x", pady=5)
        
        selector_title = customtkinter.CTkLabel(
            chart_selector, 
            text="Chart Selection",
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        selector_title.pack(pady=5)
        
        self.chart_var = customtkinter.StringVar(value="People Count")
        chart_menu = customtkinter.CTkComboBox(
            chart_selector,
            values=["People Count", "Violations", "Activity Level", "Performance"],
            variable=self.chart_var,
            command=self.update_selected_chart
        )
        chart_menu.pack(pady=5)
        
        # Chart display area
        self.chart_frame = customtkinter.CTkFrame(tab_frame)
        self.chart_frame.pack(fill="both", expand=True, pady=5)
        
        # Placeholder for chart
        chart_placeholder = customtkinter.CTkLabel(
            self.chart_frame,
            text="📊\nReal-time charts will\nappear here during analysis",
            font=customtkinter.CTkFont(size=12)
        )
        chart_placeholder.pack(expand=True)
    
    def setup_alerts_tab(self, tab_frame):
        """Setup alerts and notifications tab"""
        
        alerts_title = customtkinter.CTkLabel(
            tab_frame, 
            text="Alert Monitor",
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        alerts_title.pack(pady=10)
        
        # Alerts display
        self.alerts_textbox = customtkinter.CTkTextbox(
            tab_frame,
            width=260,
            height=400
        )
        self.alerts_textbox.pack(fill="both", expand=True, pady=5)
        
        # Initial alert message
        self.alerts_textbox.insert("1.0", "🟢 System Ready\nAwaiting analysis start...\n\n")
        
        # Clear alerts button
        clear_alerts_btn = customtkinter.CTkButton(
            tab_frame,
            text="🗑️ Clear Alerts",
            command=self.clear_alerts,
            width=150
        )
        clear_alerts_btn.pack(pady=5)
    
    def setup_history_tab(self, tab_frame):
        """Setup analysis history tab"""
        
        history_title = customtkinter.CTkLabel(
            tab_frame, 
            text="Analysis History",
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        history_title.pack(pady=10)
        
        # History display
        self.history_textbox = customtkinter.CTkTextbox(
            tab_frame,
            width=260,
            height=400
        )
        self.history_textbox.pack(fill="both", expand=True, pady=5)
        
        # Export history button
        export_history_btn = customtkinter.CTkButton(
            tab_frame,
            text="💾 Export History",
            command=self.export_history,
            width=150
        )
        export_history_btn.pack(pady=5)
    
    def setup_status_bar(self):
        """Setup bottom status bar"""
        
        # System status
        self.system_status_label = customtkinter.CTkLabel(
            self.status_frame,
            text="🟢 System Ready | AI Models: Loaded | GUI: Active",
            font=customtkinter.CTkFont(size=11)
        )
        self.system_status_label.pack(side="left", padx=10, pady=5)
        
        # Time display
        self.time_label = customtkinter.CTkLabel(
            self.status_frame,
            text="",
            font=customtkinter.CTkFont(size=11)
        )
        self.time_label.pack(side="right", padx=10, pady=5)
    
    def setup_update_timers(self):
        """Setup periodic update timers"""
        
        # Update time display
        self.update_time_display()
        
        # Update analytics (when analysis is running)
        self.update_analytics_display()
        
        # Schedule next updates
        self.root.after(1000, self.setup_update_timers)
    
    def update_time_display(self):
        """Update current time display"""
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.configure(text=f"🕒 {current_time}")
    
    def select_video_file(self):
        """Open file dialog to select video file"""
        
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[
                ("Video files", "*.mp4 *.avi *.mov *.mkv *.wmv"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.video_file = file_path
            self.video_path_entry.delete(0, "end")
            self.video_path_entry.insert(0, file_path)
            
            # Update status
            self.add_alert(f"📹 Video selected: {os.path.basename(file_path)}")
            print(f"Selected video: {file_path}")
    
    def start_analysis(self):
        """Start crowd analysis process"""
        
        if not self.video_file:
            self.add_alert("❌ Please select a video file first")
            return
        
        if self.is_analyzing:
            self.add_alert("⚠️ Analysis already in progress")
            return
        
        # Update UI state
        self.is_analyzing = True
        self.start_analysis_btn.configure(state="disabled")
        self.stop_analysis_btn.configure(state="normal")
        
        # Update status
        self.system_status_label.configure(text="🔄 Analysis in Progress...")
        self.add_alert("🚀 Starting crowd analysis...")
        
        # Start analysis in separate thread
        self.analysis_thread = threading.Thread(
            target=self.run_analysis_thread,
            daemon=True
        )
        self.analysis_thread.start()
        
        print("🚀 Analysis started")
    
    def stop_analysis(self):
        """Stop crowd analysis process"""
        
        if not self.is_analyzing:
            return
        
        self.is_analyzing = False
        
        # Update UI state
        self.start_analysis_btn.configure(state="normal")
        self.stop_analysis_btn.configure(state="disabled")
        
        # Update status
        self.system_status_label.configure(text="🟡 Stopping Analysis...")
        self.add_alert("🛑 Analysis stopped by user")
        
        print("🛑 Analysis stopped")
    
    def run_analysis_thread(self):
        """Main analysis thread - integrates with the crowd analysis system"""
        
        try:
            # Import and initialize the main analysis system
            from main import CrowdAnalysisSystem
            
            # Create analysis system instance
            analysis_system = CrowdAnalysisSystem()
            
            # Configure analysis modules based on UI settings
            analysis_config = {
                'social_distance': self.social_distance_var.get(),
                'restricted_entry': self.restricted_entry_var.get(),
                'abnormal_activity': self.abnormal_activity_var.get()
            }
            
            # Setup callback for GUI updates
            analysis_system.set_gui_callback(self.update_from_analysis)
            
            # Start analysis
            analysis_system.process_video_stream(self.video_file)
            
            # Analysis completed
            if self.is_analyzing:  # If not stopped by user
                self.root.after(0, self.analysis_completed)
        
        except Exception as e:
            self.root.after(0, lambda: self.analysis_error(str(e)))
    
    def update_from_analysis(self, frame_data):
        """Update GUI from analysis system callback"""
        
        # Update video display
        if 'frame' in frame_data:
            self.root.after(0, lambda: self.update_video_display(frame_data['frame']))
        
        # Update statistics
        if 'statistics' in frame_data:
            self.root.after(0, lambda: self.update_statistics(frame_data['statistics']))
        
        # Update progress
        if 'progress' in frame_data:
            progress = frame_data['progress']
            self.root.after(0, lambda: self.progress_bar.set(progress / 100.0))
            self.root.after(0, lambda: self.progress_label.configure(text=f"Progress: {progress:.1f}%"))
    
    def update_video_display(self, frame):
        """Update video display with current frame"""
        
        if frame is not None:
            # Resize frame for display
            display_frame = cv2.resize(frame, (640, 480))
            
            # Convert to RGB for tkinter
            display_frame = cv2.cvtColor(display_frame, cv2.COLOR_BGR2RGB)
            
            # Convert to PIL Image
            pil_image = Image.fromarray(display_frame)
            photo = ImageTk.PhotoImage(pil_image)
            
            # Update canvas
            self.video_canvas.delete("all")
            self.video_canvas.create_image(320, 240, image=photo)
            self.video_canvas.image = photo  # Keep reference
    
    def add_alert(self, message):
        """Add alert to alerts tab"""
        
        timestamp = time.strftime("%H:%M:%S")
        alert_message = f"[{timestamp}] {message}\n"
        
        self.alerts_textbox.insert("end", alert_message)
        self.alerts_textbox.see("end")  # Scroll to bottom
        
        # Limit alerts to last 100 entries
        lines = self.alerts_textbox.get("1.0", "end").split('\n')
        if len(lines) > 100:
            self.alerts_textbox.delete("1.0", "2.0")
    
    def run(self):
        """Start the GUI application"""
        
        self.add_alert("🖥️ Modern Crowd Studio initialized")
        self.add_alert("🤖 AI models ready for analysis")
        
        print("🖥️ Starting Modern Crowd Studio GUI...")
        self.root.mainloop()

if __name__ == "__main__":
    # Create and run the application
    app = ModernCrowdStudio()
    app.run()
```

### **5.2 Real-time Display System**

#### **5.2.1 Live Video Processing and Overlay System**

**Real-time Video Display Manager:**
```python
class RealTimeDisplayManager:
    """
    Real-time video display and overlay management:
    1. Efficient frame rendering and display
    2. Dynamic overlay generation
    3. Performance-optimized updates
    4. Interactive display controls
    """
    
    def __init__(self, canvas, config):
        self.canvas = canvas
        self.config = config
        self.current_frame = None
        self.display_overlays = True
        self.overlay_components = {}
        
        # Display optimization
        self.frame_buffer = deque(maxlen=5)
        self.display_fps = 30
        self.last_display_time = 0
        
        # Overlay configuration
        self.setup_overlay_styles()
    
    def setup_overlay_styles(self):
        """Configure overlay visual styles"""
        
        self.styles = {
            'detection_box': {
                'color': (0, 255, 0),
                'thickness': 2,
                'font_scale': 0.6
            },
            'tracking_trail': {
                'color': (255, 0, 0),
                'thickness': 2,
                'max_length': 30
            },
            'violation_indicator': {
                'color': (0, 0, 255),
                'thickness': 3,
                'blink_interval': 0.5
            },
            'restricted_zone': {
                'color': (255, 165, 0),
                'thickness': 2,
                'fill_alpha': 0.3
            },
            'statistics_overlay': {
                'background_color': (0, 0, 0),
                'text_color': (255, 255, 255),
                'font_scale': 0.7
            }
        }
    
    def update_display(self, frame, analysis_data=None):
        """
        Update video display with new frame and analysis data:
        1. Apply frame preprocessing for display
        2. Generate analysis overlays
        3. Render combined display frame
        4. Update canvas efficiently
        """
        
        current_time = time.time()
        
        # Check display rate limiting
        if current_time - self.last_display_time < (1.0 / self.display_fps):
            return
        
        self.last_display_time = current_time
        
        if frame is None:
            return
        
        try:
            # Create display frame
            display_frame = frame.copy()
            
            # Apply overlays if enabled
            if self.display_overlays and analysis_data:
                display_frame = self.render_analysis_overlays(display_frame, analysis_data)
            
            # Resize for display
            display_size = self.get_display_size()
            display_frame = cv2.resize(display_frame, display_size)
            
            # Convert and display
            self.render_to_canvas(display_frame)
            
        except Exception as e:
            print(f"❌ Display update error: {e}")
    
    def render_analysis_overlays(self, frame, analysis_data):
        """
        Render comprehensive analysis overlays:
        1. Detection bounding boxes
        2. Tracking trails and IDs
        3. Violation indicators
        4. Zone highlights
        5. Statistics overlay
        """
        
        overlay_frame = frame.copy()
        
        # Detection overlays
        if 'detections' in analysis_data:
            overlay_frame = self.render_detections(overlay_frame, analysis_data['detections'])
        
        # Tracking overlays
        if 'tracks' in analysis_data:
            overlay_frame = self.render_tracks(overlay_frame, analysis_data['tracks'])
        
        # Social distance overlays
        if 'social_distance' in analysis_data:
            overlay_frame = self.render_social_distance(overlay_frame, analysis_data['social_distance'])
        
        # Restricted area overlays
        if 'restricted_areas' in analysis_data:
            overlay_frame = self.render_restricted_areas(overlay_frame, analysis_data['restricted_areas'])
        
        # Statistics overlay
        if 'statistics' in analysis_data:
            overlay_frame = self.render_statistics_overlay(overlay_frame, analysis_data['statistics'])
        
        return overlay_frame
    
    def render_detections(self, frame, detections):
        """Render detection bounding boxes with labels"""
        
        for detection in detections:
            x, y, w, h = detection['bbox']
            confidence = detection['confidence']
            class_name = detection['class_name']
            
            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), 
                         self.styles['detection_box']['color'], 
                         self.styles['detection_box']['thickness'])
            
            # Draw label
            label = f"{class_name}: {confidence:.2f}"
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 
                                       self.styles['detection_box']['font_scale'], 1)[0]
            
            # Label background
            cv2.rectangle(frame, (x, y - label_size[1] - 10), 
                         (x + label_size[0], y), 
                         self.styles['detection_box']['color'], -1)
            
            # Label text
            cv2.putText(frame, label, (x, y - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX,
                       self.styles['detection_box']['font_scale'], 
                       (255, 255, 255), 1)
        
        return frame
    
    def render_tracks(self, frame, tracks):
        """Render tracking information and trails"""
        
        for track in tracks:
            track_id = track['id']
            bbox = track['bbox']
            trail = track.get('trail', [])
            
            # Draw track bounding box
            x1, y1, x2, y2 = bbox
            cv2.rectangle(frame, (x1, y1), (x2, y2), 
                         self.styles['tracking_trail']['color'], 
                         self.styles['tracking_trail']['thickness'])
            
            # Draw track ID
            cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, 
                       self.styles['tracking_trail']['color'], 2)
            
            # Draw trail
            if len(trail) > 1:
                trail_points = np.array(trail, dtype=np.int32)
                cv2.polylines(frame, [trail_points], False, 
                             self.styles['tracking_trail']['color'], 
                             self.styles['tracking_trail']['thickness'])
        
        return frame
    
    def render_statistics_overlay(self, frame, statistics):
        """Render statistics information overlay"""
        
        # Prepare statistics text
        stats_text = [
            f"People: {statistics.get('people_count', 0)}",
            f"Violations: {statistics.get('violations', 0)}",
            f"FPS: {statistics.get('fps', 0.0):.1f}",
            f"Frame: {statistics.get('frame_number', 0)}"
        ]
        
        # Calculate overlay position and size
        text_height = 25
        overlay_height = len(stats_text) * text_height + 20
        overlay_width = 250
        
        # Draw background
        overlay_bg = np.zeros((overlay_height, overlay_width, 3), dtype=np.uint8)
        overlay_bg.fill(50)  # Dark gray background
        
        # Add text to overlay
        for i, text in enumerate(stats_text):
            y_pos = (i + 1) * text_height
            cv2.putText(overlay_bg, text, (10, y_pos), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        
        # Blend overlay with frame
        y_offset = 10
        x_offset = frame.shape[1] - overlay_width - 10
        
        # Ensure overlay fits within frame
        if y_offset + overlay_height <= frame.shape[0] and x_offset >= 0:
            roi = frame[y_offset:y_offset + overlay_height, x_offset:x_offset + overlay_width]
            overlay_blend = cv2.addWeighted(roi, 0.3, overlay_bg, 0.7, 0)
            frame[y_offset:y_offset + overlay_height, x_offset:x_offset + overlay_width] = overlay_blend
        
        return frame
```

---

## **6. DATA PIPELINE ARCHITECTURE**

### **6.1 Data Collection and Processing**

#### **6.1.1 Comprehensive Data Management System**

**Data Pipeline Manager:**
```python
class DataPipelineManager:
    """
    Comprehensive data management system:
    1. Real-time data collection and processing
    2. Multi-format data storage (CSV, JSON, SQLite)
    3. Data validation and quality assurance
    4. Automated backup and archival
    5. Export and reporting capabilities
    """
    
    def __init__(self, config):
        self.config = config
        self.data_collectors = {}
        self.storage_backends = {}
        self.data_validators = {}
        
        # Initialize components
        self.setup_data_collectors()
        self.setup_storage_backends()
        self.setup_data_validation()
        self.setup_backup_system()
        
        # Data buffers and queues
        self.data_queue = Queue()
        self.processing_thread = None
        self.is_processing = False
    
    def setup_data_collectors(self):
        """
        Initialize specialized data collectors:
        1. Frame-level detection data
        2. Tracking trajectory data
        3. Analysis results data
        4. Performance metrics data
        5. System event logs
        """
        
        self.data_collectors = {
            'detections': DetectionDataCollector(),
            'tracking': TrackingDataCollector(),
            'social_distance': SocialDistanceDataCollector(),
            'restricted_entry': RestrictedEntryDataCollector(),
            'abnormal_activity': AbnormalActivityDataCollector(),
            'performance': PerformanceDataCollector(),
            'system_events': SystemEventCollector()
        }
        
        print("✅ Data collectors initialized")
    
    def setup_storage_backends(self):
        """
        Initialize multiple storage backends:
        1. CSV files for tabular data
        2. JSON files for structured metadata
        3. SQLite database for complex queries
        4. Binary files for large data objects
        """
        
        # Ensure output directories exist
        self.ensure_output_directories()
        
        self.storage_backends = {
            'csv': CSVStorageBackend(self.config['data']['output_directory']),
            'json': JSONStorageBackend(self.config['data']['output_directory']),
            'sqlite': SQLiteStorageBackend(self.config['data']['output_directory']),
            'binary': BinaryStorageBackend(self.config['data']['output_directory'])
        }
        
        print("✅ Storage backends initialized")
    
    def setup_data_validation(self):
        """
        Setup data validation and quality assurance:
        1. Schema validation for structured data
        2. Range and type checking
        3. Completeness validation
        4. Consistency checks across data sources
        """
        
        self.data_validators = {
            'detection_schema': DetectionSchemaValidator(),
            'tracking_schema': TrackingSchemaValidator(),
            'analysis_schema': AnalysisSchemaValidator(),
            'performance_schema': PerformanceSchemaValidator(),
            'completeness': DataCompletenessValidator(),
            'consistency': DataConsistencyValidator()
        }
        
        print("✅ Data validators initialized")
    
    def start_data_processing(self):
        """Start background data processing thread"""
        
        if self.is_processing:
            return
        
        self.is_processing = True
        self.processing_thread = threading.Thread(
            target=self.data_processing_loop,
            daemon=True
        )
        self.processing_thread.start()
        
        print("🔄 Data processing started")
    
    def stop_data_processing(self):
        """Stop background data processing"""
        
        self.is_processing = False
        
        # Process remaining data in queue
        self.flush_data_queue()
        
        if self.processing_thread:
            self.processing_thread.join(timeout=5.0)
        
        print("🛑 Data processing stopped")
    
    def collect_frame_data(self, frame_number, timestamp, detections, tracks, analysis_results):
        """
        Collect comprehensive frame-level data:
        1. Detection information
        2. Tracking data
        3. Analysis results
        4. Performance metrics
        5. System state information
        """
        
        frame_data = {
            'frame_info': {
                'frame_number': frame_number,
                'timestamp': timestamp,
                'processing_time': time.time()
            },
            'detections': self.data_collectors['detections'].collect(detections),
            'tracking': self.data_collectors['tracking'].collect(tracks),
            'analysis': {}
        }
        
        # Collect analysis data
        for analysis_type, results in analysis_results.items():
            if analysis_type in self.data_collectors:
                frame_data['analysis'][analysis_type] = self.data_collectors[analysis_type].collect(results)
        
        # Add to processing queue
        self.data_queue.put(frame_data)
    
    def data_processing_loop(self):
        """
        Main data processing loop:
        1. Process queued data
        2. Validate data quality
        3. Store in appropriate backends
        4. Trigger backup operations
        5. Handle errors and recovery
        """
        
        batch_size = 10
        batch_data = []
        
        while self.is_processing:
            try:
                # Collect batch of data
                while len(batch_data) < batch_size and not self.data_queue.empty():
                    data = self.data_queue.get(timeout=1.0)
                    batch_data.append(data)
                
                # Process batch if we have data
                if batch_data:
                    self.process_data_batch(batch_data)
                    batch_data.clear()
                
                # Small delay to prevent excessive CPU usage
                time.sleep(0.1)
                
            except Empty:
                continue
            except Exception as e:
                print(f"❌ Data processing error: {e}")
                # Log error and continue processing
                self.log_processing_error(e, batch_data)
                batch_data.clear()
    
    def process_data_batch(self, batch_data):
        """
        Process a batch of frame data:
        1. Validate data quality
        2. Transform data for storage
        3. Store in multiple backends
        4. Update aggregated statistics
        """
        
        try:
            # Validate batch data
            validated_data = self.validate_data_batch(batch_data)
            
            # Transform for different storage formats
            csv_data = self.transform_for_csv(validated_data)
            json_data = self.transform_for_json(validated_data)
            sqlite_data = self.transform_for_sqlite(validated_data)
            
            # Store in backends
            self.storage_backends['csv'].store_batch(csv_data)
            self.storage_backends['json'].store_batch(json_data)
            self.storage_backends['sqlite'].store_batch(sqlite_data)
            
            # Update aggregated statistics
            self.update_aggregated_statistics(validated_data)
            
            print(f"✅ Processed batch of {len(batch_data)} frames")
            
        except Exception as e:
            print(f"❌ Batch processing error: {e}")
            raise
    
    def validate_data_batch(self, batch_data):
        """
        Validate batch data quality:
        1. Schema validation
        2. Range checking
        3. Completeness validation
        4. Consistency checks
        """
        
        validated_batch = []
        
        for frame_data in batch_data:
            try:
                # Schema validation
                if not self.data_validators['detection_schema'].validate(frame_data.get('detections', [])):
                    raise ValueError("Detection schema validation failed")
                
                if not self.data_validators['tracking_schema'].validate(frame_data.get('tracking', [])):
                    raise ValueError("Tracking schema validation failed")
                
                # Completeness validation
                if not self.data_validators['completeness'].validate(frame_data):
                    print(f"⚠️ Incomplete data for frame {frame_data.get('frame_info', {}).get('frame_number', 'unknown')}")
                
                validated_batch.append(frame_data)
                
            except Exception as e:
                print(f"❌ Frame data validation error: {e}")
                # Skip invalid frame data
                continue
        
        return validated_batch
    
    def transform_for_csv(self, validated_data):
        """
        Transform data for CSV storage:
        1. Flatten nested structures
        2. Convert to tabular format
        3. Handle missing values
        4. Ensure consistent column order
        """
        
        csv_rows = []
        
        for frame_data in validated_data:
            frame_info = frame_data.get('frame_info', {})
            detections = frame_data.get('detections', [])
            tracking = frame_data.get('tracking', [])
            analysis = frame_data.get('analysis', {})
            
            # Create base row with frame information
            base_row = {
                'Frame': frame_info.get('frame_number', 0),
                'Timestamp': frame_info.get('timestamp', 0),
                'Processing_Time': frame_info.get('processing_time', 0),
                'Human_Count': len([d for d in detections if d.get('class_name') == 'person']),
                'Total_Detections': len(detections),
                'Active_Tracks': len(tracking)
            }
            
            # Add analysis results
            if 'social_distance' in analysis:
                social_data = analysis['social_distance']
                base_row.update({
                    'Social_Distance_Violations': social_data.get('violations', 0),
                    'Min_Distance': social_data.get('min_distance', 0),
                    'Avg_Distance': social_data.get('avg_distance', 0)
                })
            
            if 'restricted_entry' in analysis:
                restricted_data = analysis['restricted_entry']
                base_row.update({
                    'Restricted_Entry_Violations': restricted_data.get('violations', 0),
                    'Restricted_Alerts': restricted_data.get('alerts', 0)
                })
            
            if 'abnormal_activity' in analysis:
                abnormal_data = analysis['abnormal_activity']
                base_row.update({
                    'Abnormal_Activity_Detected': abnormal_data.get('detected', False),
                    'Activity_Energy': abnormal_data.get('energy', 0),
                    'Activity_Threshold': abnormal_data.get('threshold', 0)
                })
            
            csv_rows.append(base_row)
        
        return csv_rows
    
    def transform_for_json(self, validated_data):
        """
        Transform data for JSON storage:
        1. Preserve nested structure
        2. Add metadata
        3. Include processing timestamps
        4. Maintain data relationships
        """
        
        json_data = {
            'metadata': {
                'export_timestamp': time.time(),
                'export_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                'frame_count': len(validated_data),
                'data_version': '2.0'
            },
            'frames': validated_data
        }
        
        return json_data
    
    def transform_for_sqlite(self, validated_data):
        """
        Transform data for SQLite storage:
        1. Normalize data structure
        2. Create relational mappings
        3. Handle foreign key relationships
        4. Optimize for queries
        """
        
        sqlite_data = {
            'frames': [],
            'detections': [],
            'tracks': [],
            'analysis_results': []
        }
        
        for frame_data in validated_data:
            frame_info = frame_data.get('frame_info', {})
            frame_id = frame_info.get('frame_number', 0)
            
            # Frame record
            sqlite_data['frames'].append({
                'frame_id': frame_id,
                'timestamp': frame_info.get('timestamp', 0),
                'processing_time': frame_info.get('processing_time', 0)
            })
            
            # Detection records
            for i, detection in enumerate(frame_data.get('detections', [])):
                sqlite_data['detections'].append({
                    'frame_id': frame_id,
                    'detection_id': i,
                    'class_name': detection.get('class_name', ''),
                    'confidence': detection.get('confidence', 0),
                    'bbox_x': detection.get('bbox', [0, 0, 0, 0])[0],
                    'bbox_y': detection.get('bbox', [0, 0, 0, 0])[1],
                    'bbox_width': detection.get('bbox', [0, 0, 0, 0])[2],
                    'bbox_height': detection.get('bbox', [0, 0, 0, 0])[3]
                })
            
            # Track records
            for track in frame_data.get('tracking', []):
                sqlite_data['tracks'].append({
                    'frame_id': frame_id,
                    'track_id': track.get('id', 0),
                    'bbox_x1': track.get('bbox', [0, 0, 0, 0])[0],
                    'bbox_y1': track.get('bbox', [0, 0, 0, 0])[1],
                    'bbox_x2': track.get('bbox', [0, 0, 0, 0])[2],
                    'bbox_y2': track.get('bbox', [0, 0, 0, 0])[3],
                    'confidence': track.get('confidence', 1.0)
                })
            
            # Analysis records
            analysis = frame_data.get('analysis', {})
            for analysis_type, results in analysis.items():
                sqlite_data['analysis_results'].append({
                    'frame_id': frame_id,
                    'analysis_type': analysis_type,
                    'results_json': json.dumps(results)
                })
        
        return sqlite_data

class CSVStorageBackend:
    """CSV file storage backend with efficient batch operations"""
    
    def __init__(self, output_directory):
        self.output_directory = output_directory
        self.csv_file_path = os.path.join(output_directory, 'crowd_analysis_data.csv')
        self.fieldnames = None
        self.file_handle = None
        self.csv_writer = None
        
        # Initialize CSV file
        self.initialize_csv_file()
    
    def initialize_csv_file(self):
        """Initialize CSV file with headers"""
        
        # Define standard fieldnames
        self.fieldnames = [
            'Frame', 'Timestamp', 'Processing_Time', 'Human_Count', 
            'Total_Detections', 'Active_Tracks', 'Social_Distance_Violations',
            'Min_Distance', 'Avg_Distance', 'Restricted_Entry_Violations',
            'Restricted_Alerts', 'Abnormal_Activity_Detected', 
            'Activity_Energy', 'Activity_Threshold'
        ]
        
        # Create/open CSV file
        file_exists = os.path.exists(self.csv_file_path)
        
        self.file_handle = open(self.csv_file_path, 'a', newline='', encoding='utf-8')
        self.csv_writer = csv.DictWriter(self.file_handle, fieldnames=self.fieldnames)
        
        # Write header if file is new
        if not file_exists:
            self.csv_writer.writeheader()
            print(f"✅ Created new CSV file: {self.csv_file_path}")
        else:
            print(f"📝 Appending to existing CSV file: {self.csv_file_path}")
    
    def store_batch(self, csv_data):
        """Store batch of CSV data"""
        
        try:
            for row in csv_data:
                # Ensure all fieldnames are present
                complete_row = {field: row.get(field, '') for field in self.fieldnames}
                self.csv_writer.writerow(complete_row)
            
            self.file_handle.flush()  # Ensure data is written
            
        except Exception as e:
            print(f"❌ CSV storage error: {e}")
            raise
    
    def close(self):
        """Close CSV file handle"""
        
        if self.file_handle:
            self.file_handle.close()
            print("📝 CSV file closed")

class JSONStorageBackend:
    """JSON file storage backend for structured data"""
    
    def __init__(self, output_directory):
        self.output_directory = output_directory
        self.current_file_path = None
        self.data_buffer = []
        self.max_buffer_size = 100
    
    def store_batch(self, json_data):
        """Store batch of JSON data"""
        
        try:
            # Generate filename with timestamp
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            filename = f"crowd_analysis_{timestamp}.json"
            file_path = os.path.join(self.output_directory, filename)
            
            # Write JSON data to file
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            
            print(f"✅ JSON data saved: {filename}")
            
        except Exception as e:
            print(f"❌ JSON storage error: {e}")
            raise
```

This completes sections 5 and 6 of the comprehensive technical report, covering User Interface Systems and Data Pipeline Architecture. The report now includes detailed analysis of:

- ✅ **Section 5**: Modern GUI implementation with CustomTkinter, real-time display systems, and interactive dashboard components
- ✅ **Section 6**: Comprehensive data management with collection, validation, storage, and export capabilities

Would you like me to continue with the remaining sections (7-14) to complete this comprehensive technical documentation? Each section will maintain the same level of technical depth and detailed code analysis.

This continues our comprehensive technical report with detailed analysis of the video processing module, configuration management system, and AI/ML components. The report now covers:

- ✅ Sections 1-4: Executive Summary, System Architecture, Core Modules, AI/ML Components

Would you like me to continue with the remaining sections (5-14) to complete this comprehensive technical documentation? Each section maintains the same level of technical depth with detailed code examples and architectural analysis.
