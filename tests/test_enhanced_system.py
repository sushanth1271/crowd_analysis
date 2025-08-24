"""
Unit tests for the enhanced crowd analysis system
"""
import pytest
import numpy as np
import tempfile
import json
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.config_manager import ConfigManager, Config
from utils.error_handling import CrowdAnalysisError, validate_video_source, ProgressReporter
from utils.logger import setup_logger


class TestConfigManager:
    """Tests for configuration management"""
    
    def test_default_config(self):
        """Test default configuration loading"""
        config = Config()
        assert config.video.video_cap == "video/7.mp4"
        assert config.video.is_cam == False
        assert config.yolo.min_conf == 0.3
        assert config.detection.frame_size == 1080
    
    def test_config_validation_frame_size(self):
        """Test frame size validation"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("""
detection:
  frame_size: 100
""")
            temp_path = f.name
        
        try:
            config_manager = ConfigManager(temp_path)
            with pytest.raises(ValueError, match="Frame size must be between"):
                config_manager.load_config()
        finally:
            os.unlink(temp_path)
    
    def test_config_validation_confidence(self):
        """Test confidence threshold validation"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("""
yolo:
  min_conf: 1.5
""")
            temp_path = f.name
        
        try:
            config_manager = ConfigManager(temp_path)
            with pytest.raises(ValueError, match="MIN_CONF must be between"):
                config_manager.load_config()
        finally:
            os.unlink(temp_path)
    
    def test_environment_variable_override(self):
        """Test environment variable configuration override"""
        with patch.dict(os.environ, {'FRAME_SIZE': '720', 'MIN_CONF': '0.5'}):
            config_manager = ConfigManager('nonexistent.yaml')
            config = config_manager.load_config()
            
            assert config.detection.frame_size == 720
            assert config.yolo.min_conf == 0.5
    
    def test_legacy_config_compatibility(self):
        """Test legacy configuration format compatibility"""
        config_manager = ConfigManager('nonexistent.yaml')
        config = config_manager.load_config()
        legacy = config_manager.get_legacy_config()
        
        assert 'VIDEO_CONFIG' in legacy
        assert 'YOLO_CONFIG' in legacy
        assert legacy['VIDEO_CONFIG']['VIDEO_CAP'] == config.video.video_cap
        assert legacy['YOLO_CONFIG']['WEIGHTS_PATH'] == config.yolo.weights_path


class TestErrorHandling:
    """Tests for error handling utilities"""
    
    def test_custom_exceptions(self):
        """Test custom exception hierarchy"""
        with pytest.raises(CrowdAnalysisError):
            raise CrowdAnalysisError("Test error")
    
    def test_video_validation_invalid_file(self):
        """Test video source validation with invalid file"""
        with pytest.raises(Exception):  # VideoProcessingError would be raised
            validate_video_source("nonexistent_video.mp4")
    
    @patch('cv2.VideoCapture')
    def test_video_validation_valid_file(self, mock_cap_class):
        """Test video source validation with valid file"""
        # Create a temporary video file
        with tempfile.NamedTemporaryFile(suffix='.mp4') as f:
            # Mock successful video capture
            mock_cap = Mock()
            mock_cap.isOpened.return_value = True
            mock_cap.read.return_value = (True, np.zeros((480, 640, 3), dtype=np.uint8))
            mock_cap_class.return_value = mock_cap
            
            # Should not raise exception
            result = validate_video_source(f.name)
            assert result == True
    
    def test_progress_reporter(self):
        """Test progress reporting functionality"""
        reporter = ProgressReporter(100)
        
        # Test normal update
        reporter.update(50, "Half way")
        assert reporter.current_step == 50
        
        # Test increment
        reporter.update()
        assert reporter.current_step == 51
        
        # Test finish
        reporter.finish("Done")
        assert reporter.current_step == 100


class TestLogging:
    """Tests for logging configuration"""
    
    def test_logger_setup(self):
        """Test logger setup and configuration"""
        logger = setup_logger('test_logger', level='DEBUG')
        
        assert logger.name == 'test_logger'
        assert logger.level == 10  # DEBUG level
        assert len(logger.handlers) >= 2  # File and console handlers
    
    def test_logger_file_creation(self):
        """Test that log files are created"""
        logger = setup_logger('test_file_logger')
        logger.info("Test message")
        
        # Check if logs directory exists
        logs_dir = Path('logs')
        assert logs_dir.exists()
        
        # Check if log files exist
        log_files = list(logs_dir.glob('crowd_analysis_*.log'))
        assert len(log_files) > 0


class TestAnalytics:
    """Tests for analytics functionality"""
    
    @pytest.fixture
    def sample_crowd_data(self):
        """Create sample crowd data for testing"""
        data = {
            'Time': list(range(100)),
            'Human Count': np.random.randint(1, 20, 100),
            'Social Distance violate': np.random.randint(0, 5, 100),
            'Restricted Entry': [0] * 90 + [1] * 10,  # 10% restricted
            'Abnormal Activity': [0] * 95 + [1] * 5   # 5% abnormal
        }
        return data
    
    @pytest.fixture
    def sample_movement_data(self):
        """Create sample movement data for testing"""
        data = []
        for i in range(10):
            # Create random movement track
            track = [i, '00:00:00', '00:01:00']
            for j in range(20):  # 10 position pairs
                track.extend([
                    np.random.randint(0, 1920),  # x
                    np.random.randint(0, 1080)   # y
                ])
            data.append(track)
        return data
    
    def test_crowd_density_analysis(self, sample_crowd_data, tmp_path):
        """Test crowd density analysis"""
        from utils.analytics import CrowdDataAnalyzer
        import pandas as pd
        
        # Create temporary CSV file
        csv_file = tmp_path / "crowd_data.csv"
        df = pd.DataFrame(sample_crowd_data)
        df.to_csv(csv_file, index=False)
        
        # Test analysis
        analyzer = CrowdDataAnalyzer(str(tmp_path))
        analysis = analyzer.analyze_crowd_density()
        
        assert 'avg_crowd_size' in analysis
        assert 'max_crowd_size' in analysis
        assert 'total_frames' in analysis
        assert analysis['total_frames'] == 100
    
    def test_social_distancing_analysis(self, sample_crowd_data, tmp_path):
        """Test social distancing analysis"""
        from utils.analytics import CrowdDataAnalyzer
        import pandas as pd
        
        # Create temporary CSV file
        csv_file = tmp_path / "crowd_data.csv"
        df = pd.DataFrame(sample_crowd_data)
        df.to_csv(csv_file, index=False)
        
        # Test analysis
        analyzer = CrowdDataAnalyzer(str(tmp_path))
        analysis = analyzer.analyze_social_distancing()
        
        assert 'total_violations' in analysis
        assert 'violation_rate' in analysis
        assert 'crowd_size_correlation' in analysis


class TestPerformanceMonitoring:
    """Tests for performance monitoring"""
    
    def test_performance_metrics_collection(self):
        """Test performance metrics data structure"""
        from utils.performance import PerformanceMetrics
        
        metrics = PerformanceMetrics(
            cpu_percent=50.0,
            memory_percent=60.0,
            memory_usage_mb=1024.0,
            fps=30.0,
            processing_time=0.033,
            frame_count=1000,
            timestamp=1234567890.0
        )
        
        assert metrics.cpu_percent == 50.0
        assert metrics.memory_percent == 60.0
        assert metrics.fps == 30.0
    
    @patch('psutil.cpu_percent')
    @patch('psutil.Process')
    def test_performance_monitor_collection(self, mock_process_class, mock_cpu_percent):
        """Test performance monitor metrics collection"""
        from utils.performance import PerformanceMonitor
        
        # Mock system metrics
        mock_cpu_percent.return_value = 45.0
        mock_process = Mock()
        mock_process.memory_percent.return_value = 30.0
        mock_process.memory_info.return_value.rss = 1024 * 1024 * 512  # 512 MB
        mock_process_class.return_value = mock_process
        
        monitor = PerformanceMonitor()
        
        # Add some frame times
        monitor.frame_times.extend([0.033, 0.034, 0.032])
        
        metrics = monitor._collect_metrics()
        
        assert metrics.cpu_percent == 45.0
        assert metrics.memory_percent == 30.0
        assert metrics.memory_usage_mb == 512.0


class TestIntegration:
    """Integration tests for the complete system"""
    
    @patch('cv2.VideoCapture')
    @patch('cv2.dnn.readNetFromDarknet')
    def test_system_initialization(self, mock_net, mock_cap):
        """Test complete system initialization"""
        # Mock video capture
        mock_cap_instance = Mock()
        mock_cap_instance.isOpened.return_value = True
        mock_cap_instance.read.return_value = (True, np.zeros((480, 640, 3)))
        mock_cap.return_value = mock_cap_instance
        
        # Mock YOLO network
        mock_net_instance = Mock()
        mock_net_instance.getLayerNames.return_value = ['layer1', 'layer2', 'layer3']
        mock_net_instance.getUnconnectedOutLayers.return_value = [[1], [2], [3]]
        mock_net.return_value = mock_net_instance
        
        # Create temporary config
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("""
video:
  video_cap: "0"
  is_cam: true
yolo:
  weights_path: "test_weights.weights"
  config_path: "test_config.cfg"
detection:
  frame_size: 720
""")
            config_path = f.name
        
        try:
            from main_improved import CrowdAnalysisSystem
            
            # This should not raise exceptions with proper mocking
            with patch('pathlib.Path.exists', return_value=True):
                with patch('utils.error_handling.validate_video_source', return_value=True):
                    with patch('utils.error_handling.validate_model_files', return_value=True):
                        system = CrowdAnalysisSystem(config_path)
                        
                        # Test individual component setup
                        cap = system.setup_video_capture()
                        assert cap is not None
                        
                        net = system.setup_yolo_model()
                        assert net is not None
                        
                        tracker = system.setup_tracker()
                        assert tracker is not None
                        
        finally:
            os.unlink(config_path)


# Fixtures and test runners
if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__, "-v"])
