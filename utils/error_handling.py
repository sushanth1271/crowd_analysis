"""
Error handling and exception utilities for Crowd Analysis system
"""
import traceback
import sys
from typing import Optional, Callable, Any
from functools import wraps
import logging


class CrowdAnalysisError(Exception):
    """Base exception for Crowd Analysis system"""
    pass


class VideoProcessingError(CrowdAnalysisError):
    """Exception raised for video processing errors"""
    pass


class DetectionError(CrowdAnalysisError):
    """Exception raised for detection/tracking errors"""
    pass


class ConfigurationError(CrowdAnalysisError):
    """Exception raised for configuration errors"""
    pass


class DataProcessingError(CrowdAnalysisError):
    """Exception raised for data processing errors"""
    pass


def handle_exceptions(logger_name: str = 'crowd_analysis', reraise: bool = True):
    """
    Decorator for exception handling with logging
    
    Args:
        logger_name: Name of the logger to use
        reraise: Whether to reraise the exception after logging
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            logger = logging.getLogger(logger_name)
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Exception in {func.__name__}: {str(e)}")
                logger.error(f"Traceback: {traceback.format_exc()}")
                
                if reraise:
                    raise
                return None
        return wrapper
    return decorator


def safe_execute(func: Callable, *args, default_return=None, logger_name: str = 'crowd_analysis', **kwargs) -> Any:
    """
    Safely execute a function with exception handling
    
    Args:
        func: Function to execute
        *args: Positional arguments for the function
        default_return: Value to return if exception occurs
        logger_name: Logger name for error logging
        **kwargs: Keyword arguments for the function
        
    Returns:
        Function result or default_return if exception occurs
    """
    logger = logging.getLogger(logger_name)
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.error(f"Exception in {func.__name__}: {str(e)}")
        logger.debug(f"Traceback: {traceback.format_exc()}")
        return default_return


def validate_video_source(video_path: str) -> bool:
    """
    Validate video source is accessible
    
    Args:
        video_path: Path to video file or camera index
        
    Returns:
        True if video source is valid
        
    Raises:
        VideoProcessingError: If video source is invalid
    """
    import cv2
    from pathlib import Path
    
    logger = logging.getLogger('crowd_analysis')
    
    try:
        # Check if it's a file path
        if not video_path.isdigit():
            video_file = Path(video_path)
            if not video_file.exists():
                raise VideoProcessingError(f"Video file not found: {video_path}")
            
            if not video_file.is_file():
                raise VideoProcessingError(f"Path is not a file: {video_path}")
        
        # Test video capture
        cap = cv2.VideoCapture(video_path if video_path.isdigit() else str(video_path))
        if not cap.isOpened():
            raise VideoProcessingError(f"Cannot open video source: {video_path}")
        
        # Test reading a frame
        ret, frame = cap.read()
        if not ret:
            raise VideoProcessingError(f"Cannot read from video source: {video_path}")
        
        cap.release()
        logger.info(f"Video source validated: {video_path}")
        return True
        
    except Exception as e:
        logger.error(f"Video source validation failed: {str(e)}")
        raise VideoProcessingError(f"Invalid video source: {video_path}") from e


def validate_model_files(weights_path: str, config_path: str) -> bool:
    """
    Validate YOLO model files exist
    
    Args:
        weights_path: Path to YOLO weights file
        config_path: Path to YOLO config file
        
    Returns:
        True if all files exist
        
    Raises:
        ConfigurationError: If model files are missing
    """
    from pathlib import Path
    
    logger = logging.getLogger('crowd_analysis')
    
    weights_file = Path(weights_path)
    config_file = Path(config_path)
    
    if not weights_file.exists():
        raise ConfigurationError(f"YOLO weights file not found: {weights_path}")
    
    if not config_file.exists():
        raise ConfigurationError(f"YOLO config file not found: {config_path}")
    
    logger.info(f"Model files validated: {weights_path}, {config_path}")
    return True


def setup_error_handling():
    """Setup global error handling"""
    def handle_exception(exc_type, exc_value, exc_traceback):
        """Handle uncaught exceptions"""
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        
        logger = logging.getLogger('crowd_analysis')
        logger.critical(
            "Uncaught exception", 
            exc_info=(exc_type, exc_value, exc_traceback)
        )
    
    sys.excepthook = handle_exception


class ProgressReporter:
    """Progress reporting utility"""
    
    def __init__(self, total_steps: int, logger_name: str = 'crowd_analysis'):
        self.total_steps = total_steps
        self.current_step = 0
        self.logger = logging.getLogger(logger_name)
        
    def update(self, step: Optional[int] = None, message: str = ""):
        """Update progress"""
        if step is not None:
            self.current_step = step
        else:
            self.current_step += 1
        
        percentage = (self.current_step / self.total_steps) * 100
        progress_msg = f"Progress: {self.current_step}/{self.total_steps} ({percentage:.1f}%)"
        
        if message:
            progress_msg += f" - {message}"
        
        self.logger.info(progress_msg)
        
        # Also print to console for immediate feedback
        print(f"\r{progress_msg}", end="", flush=True)
        
        if self.current_step >= self.total_steps:
            print()  # New line when complete
    
    def finish(self, message: str = "Complete"):
        """Mark progress as finished"""
        self.current_step = self.total_steps
        self.update(message=message)
