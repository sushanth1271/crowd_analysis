"""
Advanced data analytics and insights for crowd analysis
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from pathlib import Path
import json
import logging
from datetime import datetime, timedelta
from scipy import stats
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


class CrowdDataAnalyzer:
    """Advanced analytics for crowd behavior data"""
    
    def __init__(self, data_dir: str = "processed_data"):
        self.data_dir = Path(data_dir)
        self.logger = logging.getLogger('crowd_analysis.analytics')
        
        # Load data
        self.crowd_data = None
        self.movement_data = None
        self.video_metadata = None
        
        self._load_data()
    
    def _load_data(self):
        """Load processed data files"""
        try:
            # Load crowd data
            crowd_file = self.data_dir / "crowd_data.csv"
            if crowd_file.exists():
                self.crowd_data = pd.read_csv(crowd_file)
                self.logger.info(f"Loaded crowd data: {len(self.crowd_data)} records")
            
            # Load movement data  
            movement_file = self.data_dir / "movement_data.csv"
            if movement_file.exists():
                self.movement_data = pd.read_csv(movement_file)
                self.logger.info(f"Loaded movement data: {len(self.movement_data)} records")
            
            # Load video metadata
            metadata_file = self.data_dir / "video_data.json"
            if metadata_file.exists():
                with open(metadata_file, 'r') as f:
                    self.video_metadata = json.load(f)
                self.logger.info("Loaded video metadata")
            
        except Exception as e:
            self.logger.error(f"Error loading data: {str(e)}")
    
    def analyze_crowd_density(self) -> Dict:
        """Analyze crowd density patterns"""
        if self.crowd_data is None:
            return {}
        
        analysis = {
            'total_frames': len(self.crowd_data),
            'avg_crowd_size': self.crowd_data['Human Count'].mean(),
            'max_crowd_size': self.crowd_data['Human Count'].max(),
            'min_crowd_size': self.crowd_data['Human Count'].min(),
            'std_crowd_size': self.crowd_data['Human Count'].std(),
            'density_distribution': self.crowd_data['Human Count'].value_counts().to_dict()
        }
        
        # Peak hours analysis
        if 'Time' in self.crowd_data.columns:
            crowd_by_hour = self._analyze_by_time_periods()
            analysis.update(crowd_by_hour)
        
        self.logger.info(f"Crowd density analysis completed - Avg size: {analysis['avg_crowd_size']:.1f}")
        return analysis
    
    def analyze_social_distancing(self) -> Dict:
        """Analyze social distancing violations"""
        if self.crowd_data is None:
            return {}
        
        total_violations = self.crowd_data['Social Distance violate'].sum()
        violation_rate = (self.crowd_data['Social Distance violate'] > 0).mean()
        
        analysis = {
            'total_violations': int(total_violations),
            'violation_rate': float(violation_rate),
            'avg_violations_per_frame': self.crowd_data['Social Distance violate'].mean(),
            'max_violations_per_frame': self.crowd_data['Social Distance violate'].max(),
        }
        
        # Correlation with crowd size
        if len(self.crowd_data) > 1:
            correlation = self.crowd_data['Human Count'].corr(self.crowd_data['Social Distance violate'])
            analysis['crowd_size_correlation'] = float(correlation) if not np.isnan(correlation) else 0.0
        
        self.logger.info(f"Social distancing analysis - Violation rate: {violation_rate:.1%}")
        return analysis
    
    def analyze_movement_patterns(self) -> Dict:
        """Analyze movement and tracking patterns"""
        if self.movement_data is None:
            return {}
        
        # Calculate track durations and distances
        track_stats = []
        for _, row in self.movement_data.iterrows():
            # Parse movement tracks
            positions = self._parse_positions(row)
            if len(positions) > 1:
                duration = len(positions)
                total_distance = self._calculate_path_distance(positions)
                avg_speed = total_distance / duration if duration > 0 else 0
                
                track_stats.append({
                    'track_id': row['Track ID'],
                    'duration': duration,
                    'total_distance': total_distance,
                    'avg_speed': avg_speed,
                    'positions': positions
                })
        
        if not track_stats:
            return {}
        
        df_tracks = pd.DataFrame(track_stats)
        
        analysis = {
            'total_tracks': len(track_stats),
            'avg_track_duration': float(df_tracks['duration'].mean()),
            'avg_total_distance': float(df_tracks['total_distance'].mean()),
            'avg_speed': float(df_tracks['avg_speed'].mean()),
            'track_duration_distribution': df_tracks['duration'].describe().to_dict()
        }
        
        # Clustering analysis for movement patterns
        clustering_results = self._cluster_movement_patterns(track_stats)
        analysis.update(clustering_results)
        
        self.logger.info(f"Movement analysis - {len(track_stats)} tracks analyzed")
        return analysis
    
    def analyze_abnormal_activity(self) -> Dict:
        """Analyze abnormal activity patterns"""
        if self.crowd_data is None:
            return {}
        
        abnormal_frames = self.crowd_data['Abnormal Activity'].sum()
        abnormal_rate = (self.crowd_data['Abnormal Activity'] > 0).mean()
        
        analysis = {
            'abnormal_frames': int(abnormal_frames),
            'abnormal_rate': float(abnormal_rate),
            'total_frames_analyzed': len(self.crowd_data)
        }
        
        # Time-based analysis
        if abnormal_frames > 0:
            abnormal_periods = self._identify_abnormal_periods()
            analysis['abnormal_periods'] = abnormal_periods
        
        self.logger.info(f"Abnormal activity analysis - Rate: {abnormal_rate:.1%}")
        return analysis
    
    def generate_insights(self) -> Dict:
        """Generate comprehensive insights from all analyses"""
        insights = {
            'crowd_density': self.analyze_crowd_density(),
            'social_distancing': self.analyze_social_distancing(), 
            'movement_patterns': self.analyze_movement_patterns(),
            'abnormal_activity': self.analyze_abnormal_activity(),
            'summary': {}
        }
        
        # Generate summary insights
        summary = {}
        
        if insights['crowd_density']:
            avg_crowd = insights['crowd_density']['avg_crowd_size']
            max_crowd = insights['crowd_density']['max_crowd_size']
            summary['crowd_summary'] = f"Average crowd size: {avg_crowd:.1f}, Peak: {max_crowd}"
        
        if insights['social_distancing']:
            violation_rate = insights['social_distancing']['violation_rate']
            summary['safety_summary'] = f"Social distancing violation rate: {violation_rate:.1%}"
        
        if insights['movement_patterns']:
            total_tracks = insights['movement_patterns']['total_tracks']
            summary['activity_summary'] = f"Total unique individuals tracked: {total_tracks}"
        
        if insights['abnormal_activity']:
            abnormal_rate = insights['abnormal_activity']['abnormal_rate']
            summary['security_summary'] = f"Abnormal activity detected in {abnormal_rate:.1%} of frames"
        
        insights['summary'] = summary
        
        # Save insights to file
        self._save_insights(insights)
        
        return insights
    
    def _parse_positions(self, row) -> List[Tuple[int, int]]:
        """Parse position data from movement row"""
        positions = []
        movement_data = row.iloc[3:].dropna()  # Skip first 3 columns
        
        for i in range(0, len(movement_data), 2):
            if i + 1 < len(movement_data):
                try:
                    x, y = int(movement_data.iloc[i]), int(movement_data.iloc[i + 1])
                    positions.append((x, y))
                except (ValueError, TypeError):
                    break
        
        return positions
    
    def _calculate_path_distance(self, positions: List[Tuple[int, int]]) -> float:
        """Calculate total path distance"""
        if len(positions) < 2:
            return 0.0
        
        total_distance = 0.0
        for i in range(1, len(positions)):
            dx = positions[i][0] - positions[i-1][0]
            dy = positions[i][1] - positions[i-1][1]
            distance = np.sqrt(dx*dx + dy*dy)
            total_distance += distance
        
        return total_distance
    
    def _cluster_movement_patterns(self, track_stats: List[Dict]) -> Dict:
        """Cluster movement patterns using DBSCAN"""
        if len(track_stats) < 5:
            return {'movement_clusters': 0}
        
        # Create features for clustering (duration, distance, speed)
        features = np.array([[
            track['duration'],
            track['total_distance'],
            track['avg_speed']
        ] for track in track_stats])
        
        # Normalize features
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)
        
        # Apply DBSCAN clustering
        clustering = DBSCAN(eps=0.5, min_samples=3)
        cluster_labels = clustering.fit_predict(features_scaled)
        
        n_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
        n_noise = list(cluster_labels).count(-1)
        
        return {
            'movement_clusters': n_clusters,
            'noise_tracks': n_noise,
            'cluster_distribution': pd.Series(cluster_labels).value_counts().to_dict()
        }
    
    def _analyze_by_time_periods(self) -> Dict:
        """Analyze data by time periods (hours, days, etc.)"""
        # This would need proper timestamp parsing
        # For now, return placeholder
        return {
            'peak_hours_analysis': 'Time-based analysis requires proper timestamp data'
        }
    
    def _identify_abnormal_periods(self) -> List[Dict]:
        """Identify periods of abnormal activity"""
        abnormal_frames = self.crowd_data[self.crowd_data['Abnormal Activity'] > 0]
        
        periods = []
        current_period_start = None
        current_period_end = None
        
        for idx, row in abnormal_frames.iterrows():
            if current_period_start is None:
                current_period_start = idx
                current_period_end = idx
            elif idx == current_period_end + 1:
                current_period_end = idx
            else:
                # End of current period
                periods.append({
                    'start_frame': current_period_start,
                    'end_frame': current_period_end,
                    'duration': current_period_end - current_period_start + 1
                })
                current_period_start = idx
                current_period_end = idx
        
        # Add final period
        if current_period_start is not None:
            periods.append({
                'start_frame': current_period_start,
                'end_frame': current_period_end,
                'duration': current_period_end - current_period_start + 1
            })
        
        return periods
    
    def _save_insights(self, insights: Dict):
        """Save insights to JSON file"""
        insights_file = self.data_dir / "analytics_insights.json"
        
        # Convert numpy types to native Python types for JSON serialization
        def convert_numpy(obj):
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, dict):
                return {key: convert_numpy(value) for key, value in obj.items()}
            elif isinstance(obj, list):
                return [convert_numpy(item) for item in obj]
            else:
                return obj
        
        insights_serializable = convert_numpy(insights)
        
        with open(insights_file, 'w') as f:
            json.dump(insights_serializable, f, indent=2)
        
        self.logger.info(f"Analytics insights saved to {insights_file}")


def generate_analytics_report(data_dir: str = "processed_data") -> Dict:
    """Generate comprehensive analytics report"""
    analyzer = CrowdDataAnalyzer(data_dir)
    return analyzer.generate_insights()
