"""
Logging configuration for Crowd Analysis system
"""
import logging
import logging.handlers
import os
from datetime import datetime


def setup_logger(name: str = 'crowd_analysis', level: str = 'INFO') -> logging.Logger:
    """
    Set up logger with file and console handlers
    
    Args:
        name: Logger name
        level: Logging level ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Create logs directory if it doesn't exist
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )
    
    # File handler with rotation
    log_filename = os.path.join(log_dir, f'crowd_analysis_{datetime.now().strftime("%Y%m%d")}.log')
    file_handler = logging.handlers.RotatingFileHandler(
        log_filename,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, level.upper()))
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


def log_system_info():
    """Log system information at startup"""
    logger = logging.getLogger('crowd_analysis')
    
    logger.info("=" * 50)
    logger.info("CROWD ANALYSIS SYSTEM STARTUP")
    logger.info("=" * 50)
    
    import sys
    import cv2
    import numpy as np
    
    logger.info(f"Python version: {sys.version}")
    logger.info(f"OpenCV version: {cv2.__version__}")
    logger.info(f"NumPy version: {np.__version__}")
    
    try:
        import tensorflow as tf
        logger.info(f"TensorFlow version: {tf.__version__}")
        logger.info(f"GPU available: {tf.config.list_physical_devices('GPU')}")
    except ImportError:
        logger.warning("TensorFlow not available")
    
    logger.info("System initialization complete")
