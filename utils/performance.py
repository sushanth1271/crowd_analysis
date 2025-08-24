"""
Performance monitoring and optimization utilities
"""
import time
import psutil
import threading
from typing import Dict, List, Optional
from dataclasses import dataclass
from collections import defaultdict, deque
import logging


@dataclass
class PerformanceMetrics:
    """Performance metrics data class"""
    cpu_percent: float
    memory_percent: float
    memory_usage_mb: float
    fps: float
    processing_time: float
    frame_count: int
    timestamp: float


class PerformanceMonitor:
    """Performance monitoring and optimization"""
    
    def __init__(self, max_history: int = 1000):
        self.max_history = max_history
        self.metrics_history: deque = deque(maxlen=max_history)
        self.timers: Dict[str, float] = {}
        self.counters: Dict[str, int] = defaultdict(int)
        self.is_monitoring = False
        self.monitor_thread = None
        self.logger = logging.getLogger('crowd_analysis.performance')
        
        # Frame processing metrics
        self.frame_times: deque = deque(maxlen=100)
        self.last_frame_time = time.time()
        
    def start_monitoring(self, interval: float = 5.0):
        """Start performance monitoring in background thread"""
        if self.is_monitoring:
            return
        
        self.is_monitoring = True
        self.monitor_thread = threading.Thread(
            target=self._monitor_loop,
            args=(interval,),
            daemon=True
        )
        self.monitor_thread.start()
        self.logger.info("Performance monitoring started")
    
    def stop_monitoring(self):
        """Stop performance monitoring"""
        self.is_monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=1.0)
        self.logger.info("Performance monitoring stopped")
    
    def _monitor_loop(self, interval: float):
        """Background monitoring loop"""
        while self.is_monitoring:
            try:
                metrics = self._collect_metrics()
                self.metrics_history.append(metrics)
                
                # Log performance warnings
                self._check_performance_warnings(metrics)
                
                time.sleep(interval)
            except Exception as e:
                self.logger.error(f"Error in performance monitoring: {e}")
    
    def _collect_metrics(self) -> PerformanceMetrics:
        """Collect current performance metrics"""
        process = psutil.Process()
        
        # System metrics
        cpu_percent = psutil.cpu_percent()
        memory_info = process.memory_info()
        memory_percent = process.memory_percent()
        memory_usage_mb = memory_info.rss / 1024 / 1024
        
        # FPS calculation
        fps = self.get_current_fps()
        
        # Processing time
        avg_processing_time = sum(self.frame_times) / len(self.frame_times) if self.frame_times else 0
        
        return PerformanceMetrics(
            cpu_percent=cpu_percent,
            memory_percent=memory_percent,
            memory_usage_mb=memory_usage_mb,
            fps=fps,
            processing_time=avg_processing_time,
            frame_count=self.counters['frames_processed'],
            timestamp=time.time()
        )
    
    def _check_performance_warnings(self, metrics: PerformanceMetrics):
        """Check for performance warnings"""
        if metrics.cpu_percent > 90:
            self.logger.warning(f"High CPU usage: {metrics.cpu_percent:.1f}%")
        
        if metrics.memory_percent > 80:
            self.logger.warning(f"High memory usage: {metrics.memory_percent:.1f}% ({metrics.memory_usage_mb:.1f} MB)")
        
        if metrics.fps > 0 and metrics.fps < 10:
            self.logger.warning(f"Low FPS: {metrics.fps:.1f}")
    
    def start_timer(self, name: str):
        """Start a named timer"""
        self.timers[name] = time.time()
    
    def end_timer(self, name: str) -> Optional[float]:
        """End a named timer and return elapsed time"""
        if name not in self.timers:
            return None
        
        elapsed = time.time() - self.timers[name]
        del self.timers[name]
        return elapsed
    
    def record_frame_processing(self):
        """Record frame processing time"""
        current_time = time.time()
        frame_time = current_time - self.last_frame_time
        self.frame_times.append(frame_time)
        self.last_frame_time = current_time
        self.counters['frames_processed'] += 1
    
    def get_current_fps(self) -> float:
        """Calculate current FPS"""
        if len(self.frame_times) < 2:
            return 0.0
        
        avg_frame_time = sum(self.frame_times) / len(self.frame_times)
        return 1.0 / avg_frame_time if avg_frame_time > 0 else 0.0
    
    def get_performance_summary(self) -> Dict:
        """Get performance summary"""
        if not self.metrics_history:
            return {}
        
        recent_metrics = list(self.metrics_history)[-10:]  # Last 10 measurements
        
        return {
            'avg_cpu_percent': sum(m.cpu_percent for m in recent_metrics) / len(recent_metrics),
            'avg_memory_usage_mb': sum(m.memory_usage_mb for m in recent_metrics) / len(recent_metrics),
            'current_fps': self.get_current_fps(),
            'total_frames_processed': self.counters['frames_processed'],
            'avg_processing_time': sum(self.frame_times) / len(self.frame_times) if self.frame_times else 0,
        }
    
    def log_performance_summary(self):
        """Log current performance summary"""
        summary = self.get_performance_summary()
        if summary:
            self.logger.info(
                f"Performance Summary - "
                f"CPU: {summary['avg_cpu_percent']:.1f}%, "
                f"Memory: {summary['avg_memory_usage_mb']:.1f}MB, "
                f"FPS: {summary['current_fps']:.1f}, "
                f"Frames: {summary['total_frames_processed']}, "
                f"Avg Time: {summary['avg_processing_time']:.3f}s"
            )


class OptimizationManager:
    """Manages performance optimizations"""
    
    def __init__(self):
        self.logger = logging.getLogger('crowd_analysis.optimization')
        self.optimizations_enabled = set()
    
    def optimize_opencv(self):
        """Apply OpenCV optimizations"""
        import cv2
        
        # Enable optimizations
        cv2.setUseOptimized(True)
        cv2.setNumThreads(psutil.cpu_count())
        
        self.optimizations_enabled.add('opencv')
        self.logger.info("OpenCV optimizations enabled")
    
    def check_gpu_availability(self) -> bool:
        """Check if GPU is available for processing"""
        try:
            import cv2
            
            # Check for CUDA support
            if cv2.cuda.getCudaEnabledDeviceCount() > 0:
                self.logger.info("CUDA GPU detected and available")
                return True
            
        except AttributeError:
            pass
        
        try:
            # Check for TensorFlow GPU
            import tensorflow as tf
            if tf.config.list_physical_devices('GPU'):
                self.logger.info("TensorFlow GPU detected")
                return True
        except ImportError:
            pass
        
        self.logger.info("No GPU acceleration available")
        return False
    
    def enable_gpu_acceleration(self, net):
        """Enable GPU acceleration for YOLO if available"""
        try:
            import cv2
            
            if cv2.cuda.getCudaEnabledDeviceCount() > 0:
                net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
                net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
                
                self.optimizations_enabled.add('gpu')
                self.logger.info("GPU acceleration enabled for YOLO")
                return True
                
        except Exception as e:
            self.logger.warning(f"Failed to enable GPU acceleration: {e}")
        
        return False
    
    def optimize_frame_processing(self, frame_skip: int = 1) -> int:
        """Optimize frame processing by skipping frames if performance is low"""
        # This could be dynamically adjusted based on performance
        return max(1, frame_skip)
    
    def apply_all_optimizations(self, net=None):
        """Apply all available optimizations"""
        self.optimize_opencv()
        
        if net is not None:
            self.enable_gpu_acceleration(net)
        
        self.check_gpu_availability()
        
        self.logger.info(f"Optimizations applied: {', '.join(self.optimizations_enabled)}")


# Global performance monitor instance
performance_monitor = PerformanceMonitor()
optimization_manager = OptimizationManager()
