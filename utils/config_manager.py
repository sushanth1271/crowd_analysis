"""
Enhanced configuration management with validation and environment support
"""
import os
import yaml
import json
import datetime
from typing import Dict, Any, Union
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class VideoConfig:
    """Video input configuration"""
    video_cap: str = "video/7.mp4"
    is_cam: bool = False
    cam_approx_fps: int = 3
    high_cam: bool = True
    start_time: datetime.datetime = datetime.datetime(2020, 11, 5, 0, 0, 0, 0)


@dataclass  
class YOLOConfig:
    """YOLO model configuration"""
    weights_path: str = "YOLOv4-tiny/yolov4-tiny.weights"
    config_path: str = "YOLOv4-tiny/yolov4-tiny.cfg"
    min_conf: float = 0.3
    nms_thresh: float = 0.2


@dataclass
class DetectionConfig:
    """Detection and processing configuration"""
    show_processing_output: bool = True
    show_detect: bool = True
    show_tracking_id: bool = True
    frame_size: int = 1080
    data_record: bool = True
    data_record_rate: int = 5


@dataclass
class SocialDistanceConfig:
    """Social distance monitoring configuration"""
    enabled: bool = True
    show_violation_count: bool = True
    social_distance: int = 50


@dataclass
class RestrictedEntryConfig:
    """Restricted entry monitoring configuration"""
    enabled: bool = True
    start_time: datetime.time = datetime.time(9, 0, 0)
    end_time: datetime.time = datetime.time(17, 0, 0)


@dataclass
class AbnormalActivityConfig:
    """Abnormal activity detection configuration"""
    enabled: bool = True
    min_people: int = 5
    energy_threshold: int = 1866
    activity_threshold: float = 0.66


@dataclass
class TrackingConfig:
    """Object tracking configuration"""
    max_age: int = 3
    max_cosine_distance: float = 0.7
    nn_budget: int = None


@dataclass
class Config:
    """Main configuration class"""
    video: VideoConfig = None
    yolo: YOLOConfig = None
    detection: DetectionConfig = None
    social_distance: SocialDistanceConfig = None
    restricted_entry: RestrictedEntryConfig = None
    abnormal_activity: AbnormalActivityConfig = None
    tracking: TrackingConfig = None
    
    def __post_init__(self):
        if self.video is None:
            self.video = VideoConfig()
        if self.yolo is None:
            self.yolo = YOLOConfig()
        if self.detection is None:
            self.detection = DetectionConfig()
        if self.social_distance is None:
            self.social_distance = SocialDistanceConfig()
        if self.restricted_entry is None:
            self.restricted_entry = RestrictedEntryConfig()
        if self.abnormal_activity is None:
            self.abnormal_activity = AbnormalActivityConfig()
        if self.tracking is None:
            self.tracking = TrackingConfig()


class ConfigManager:
    """Configuration manager with validation and environment support"""
    
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = Path(config_path)
        self.config = Config()
        
    def load_config(self) -> Config:
        """Load configuration from file"""
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                if self.config_path.suffix == '.yaml':
                    data = yaml.safe_load(f)
                else:
                    data = json.load(f)
            
            # Update config with loaded data
            self._update_config_from_dict(data)
        else:
            # Create default config file
            self.save_config()
            
        self._load_environment_variables()
        self._validate_config()
        
        return self.config
    
    def save_config(self):
        """Save current configuration to file"""
        config_dict = asdict(self.config)
        
        # Convert datetime objects to strings
        config_dict['video']['start_time'] = self.config.video.start_time.isoformat()
        config_dict['restricted_entry']['start_time'] = self.config.restricted_entry.start_time.strftime('%H:%M:%S')
        config_dict['restricted_entry']['end_time'] = self.config.restricted_entry.end_time.strftime('%H:%M:%S')
        
        with open(self.config_path, 'w') as f:
            if self.config_path.suffix == '.yaml':
                yaml.dump(config_dict, f, default_flow_style=False, indent=2)
            else:
                json.dump(config_dict, f, indent=2)
    
    def _update_config_from_dict(self, data: Dict[str, Any]):
        """Update configuration from dictionary"""
        for section_name, section_data in data.items():
            if hasattr(self.config, section_name):
                section = getattr(self.config, section_name)
                for key, value in section_data.items():
                    if hasattr(section, key):
                        # Handle datetime parsing
                        if key == 'start_time' and section_name == 'video':
                            value = datetime.datetime.fromisoformat(value)
                        elif key in ['start_time', 'end_time'] and section_name == 'restricted_entry':
                            value = datetime.time.fromisoformat(value)
                        
                        setattr(section, key, value)
    
    def _load_environment_variables(self):
        """Load configuration from environment variables"""
        env_mapping = {
            'VIDEO_CAP': ('video', 'video_cap'),
            'IS_CAM': ('video', 'is_cam'),
            'FRAME_SIZE': ('detection', 'frame_size'),
            'MIN_CONF': ('yolo', 'min_conf'),
            'SOCIAL_DISTANCE': ('social_distance', 'social_distance'),
            'ABNORMAL_ENERGY': ('abnormal_activity', 'energy_threshold'),
        }
        
        for env_var, (section_name, attr_name) in env_mapping.items():
            env_value = os.getenv(env_var)
            if env_value is not None:
                section = getattr(self.config, section_name)
                # Convert to appropriate type
                if attr_name in ['is_cam']:
                    env_value = env_value.lower() in ('true', '1', 'yes')
                elif attr_name in ['frame_size', 'social_distance', 'energy_threshold']:
                    env_value = int(env_value)
                elif attr_name in ['min_conf']:
                    env_value = float(env_value)
                
                setattr(section, attr_name, env_value)
    
    def _validate_config(self):
        """Validate configuration values"""
        errors = []
        
        # Validate frame size
        if not 480 <= self.config.detection.frame_size <= 1920:
            errors.append("Frame size must be between 480 and 1920")
        
        # Validate confidence thresholds
        if not 0.0 <= self.config.yolo.min_conf <= 1.0:
            errors.append("MIN_CONF must be between 0.0 and 1.0")
        
        if not 0.0 <= self.config.yolo.nms_thresh <= 1.0:
            errors.append("NMS_THRESH must be between 0.0 and 1.0")
        
        # Validate social distance threshold
        if self.config.social_distance.social_distance <= 0:
            errors.append("Social distance must be positive")
        
        # Validate abnormal activity threshold
        if not 0.0 <= self.config.abnormal_activity.activity_threshold <= 1.0:
            errors.append("Abnormal activity threshold must be between 0.0 and 1.0")
        
        # Check if video file exists (for non-camera input)
        if not self.config.video.is_cam:
            video_path = Path(self.config.video.video_cap)
            if not video_path.exists():
                errors.append(f"Video file not found: {video_path}")
        
        # Check if YOLO files exist
        if not Path(self.config.yolo.weights_path).exists():
            errors.append(f"YOLO weights file not found: {self.config.yolo.weights_path}")
        
        if not Path(self.config.yolo.config_path).exists():
            errors.append(f"YOLO config file not found: {self.config.yolo.config_path}")
        
        if errors:
            raise ValueError("Configuration validation failed:\n" + "\n".join(f"- {error}" for error in errors))
    
    def get_legacy_config(self) -> Dict[str, Any]:
        """Get configuration in legacy format for backward compatibility"""
        return {
            'VIDEO_CONFIG': {
                'VIDEO_CAP': self.config.video.video_cap,
                'IS_CAM': self.config.video.is_cam,
                'CAM_APPROX_FPS': self.config.video.cam_approx_fps,
                'HIGH_CAM': self.config.video.high_cam,
                'START_TIME': self.config.video.start_time,
            },
            'YOLO_CONFIG': {
                'WEIGHTS_PATH': self.config.yolo.weights_path,
                'CONFIG_PATH': self.config.yolo.config_path,
            },
            'SHOW_PROCESSING_OUTPUT': self.config.detection.show_processing_output,
            'SHOW_DETECT': self.config.detection.show_detect,
            'SHOW_TRACKING_ID': self.config.detection.show_tracking_id,
            'DATA_RECORD': self.config.detection.data_record,
            'DATA_RECORD_RATE': self.config.detection.data_record_rate,
            'FRAME_SIZE': self.config.detection.frame_size,
            'RE_CHECK': self.config.restricted_entry.enabled,
            'RE_START_TIME': self.config.restricted_entry.start_time,
            'RE_END_TIME': self.config.restricted_entry.end_time,
            'SD_CHECK': self.config.social_distance.enabled,
            'SHOW_VIOLATION_COUNT': self.config.social_distance.show_violation_count,
            'SOCIAL_DISTANCE': self.config.social_distance.social_distance,
            'ABNORMAL_CHECK': self.config.abnormal_activity.enabled,
            'ABNORMAL_MIN_PEOPLE': self.config.abnormal_activity.min_people,
            'ABNORMAL_ENERGY': self.config.abnormal_activity.energy_threshold,
            'ABNORMAL_THRESH': self.config.abnormal_activity.activity_threshold,
            'MIN_CONF': self.config.yolo.min_conf,
            'NMS_THRESH': self.config.yolo.nms_thresh,
            'TRACK_MAX_AGE': self.config.tracking.max_age,
        }


# Global config manager instance
config_manager = ConfigManager()
