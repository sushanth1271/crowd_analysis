"""
Enhanced visualization script that saves all graphs to files
This script generates all visualizations and saves them to the 'generated_plots' directory
"""
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to avoid display issues
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.dates as mdates
import csv
import json
import datetime
import numpy as np
import pandas as pd
from pathlib import Path
import cv2
import imutils
from math import ceil, floor
from scipy.spatial.distance import euclidean
from colors import RGB_COLORS, gradient_color_RGB
from config import VIDEO_CONFIG

def create_output_directory():
    """Create output directory for generated plots"""
    output_dir = Path('generated_plots')
    output_dir.mkdir(exist_ok=True)
    return output_dir

def generate_crowd_data_plots(output_dir):
    """Generate crowd data visualization plots"""
    print("📊 Generating crowd data plots...")
    
    try:
        # Load crowd data
        human_count = []
        violate_count = []
        restricted_entry = []
        abnormal_activity = []
        
        with open('processed_data/crowd_data.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)  # Skip header
            for row in reader:
                human_count.append(int(row[1]))
                violate_count.append(int(row[2]))
                restricted_entry.append(bool(int(row[3])))
                abnormal_activity.append(bool(int(row[4])))

        # Load video metadata
        with open('processed_data/video_data.json', 'r') as file:
            data = json.load(file)
            data_record_frame = data["DATA_RECORD_FRAME"]
            is_cam = data["IS_CAM"]
            vid_fps = data["VID_FPS"]
            start_time = data["START_TIME"]

        start_time = datetime.datetime.strptime(start_time, "%d/%m/%Y, %H:%M:%S")
        time_steps = data_record_frame / vid_fps
        data_length = len(human_count)

        # Create time axis
        time_axis = []
        graph_height = max(human_count) if human_count else 10

        fig, ax = plt.subplots(figsize=(12, 8))
        time = start_time
        
        for i in range(data_length):
            time += datetime.timedelta(seconds=time_steps)
            time_axis.append(time)
            next_time = time + datetime.timedelta(seconds=time_steps)
            rect_width = mdates.date2num(next_time) - mdates.date2num(time)
            
            if restricted_entry[i]:
                ax.add_patch(patches.Rectangle((mdates.date2num(time), 0), rect_width, graph_height / 10, facecolor='red', fill=True))
            if abnormal_activity[i]:
                ax.add_patch(patches.Rectangle((mdates.date2num(time), 0), rect_width, graph_height / 20, facecolor='blue', fill=True))

        # Plot lines
        violate_line, = plt.plot(time_axis, violate_count, linewidth=3, label="Violation Count", color='orange')
        crowd_line, = plt.plot(time_axis, human_count, linewidth=3, label="Crowd Count", color='green')
        
        plt.title("Crowd Data Analysis Over Time", fontsize=16, fontweight='bold')
        plt.xlabel("Time", fontsize=12)
        plt.ylabel("Count", fontsize=12)
        
        # Create legend
        re_legend = patches.Patch(color="red", label="Restricted Entry Detected")
        an_legend = patches.Patch(color="blue", label="Abnormal Crowd Activity Detected")
        plt.legend(handles=[crowd_line, violate_line, re_legend, an_legend], loc='upper right')
        
        # Format x-axis
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        ax.xaxis.set_major_locator(mdates.SecondLocator(interval=max(1, int(len(time_axis) / 10))))
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save plot
        crowd_plot_path = output_dir / 'crowd_data_analysis.png'
        plt.savefig(crowd_plot_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"   ✅ Saved: {crowd_plot_path}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error generating crowd data plots: {str(e)}")
        return False

def generate_movement_plots(output_dir):
    """Generate movement data visualizations"""
    print("🚶 Generating movement plots...")
    
    try:
        # Load movement data
        tracks = []
        with open('processed_data/movement_data.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if len(row[3:]) > 4:
                    temp = []
                    data = row[3:]
                    for i in range(0, len(data), 2):
                        if i + 1 < len(data):
                            try:
                                temp.append([int(data[i]), int(data[i+1])])
                            except ValueError:
                                break
                    if len(temp) > 2:
                        tracks.append(temp)

        if not tracks:
            print("   ⚠️ No movement data available")
            return False

        # Load video metadata
        with open('processed_data/video_data.json', 'r') as file:
            data = json.load(file)
            vid_fps = data["VID_FPS"]
            data_record_frame = data["DATA_RECORD_FRAME"]
            frame_size = data["PROCESSED_FRAME_SIZE"]

        # Get a frame from the video for background
        cap = cv2.VideoCapture(VIDEO_CONFIG["VIDEO_CAP"])
        cap.set(1, 100)  # Set to frame 100
        ret, background_frame = cap.read()
        cap.release()
        
        if ret:
            background_frame = imutils.resize(background_frame, width=frame_size)
        else:
            # Create a blank background if video frame not available
            background_frame = np.zeros((int(frame_size * 0.5625), frame_size, 3), dtype=np.uint8)

        # 1. Generate Optical Flow Visualization
        tracks_frame = np.copy(background_frame)
        color1 = (255, 96, 0)
        color2 = (0, 28, 255)
        
        for track in tracks:
            if len(track) > 1:
                for i in range(len(track) - 1):
                    color = gradient_color_RGB(color1, color2, len(track) - 1, i)
                    cv2.line(tracks_frame, tuple(track[i]), tuple(track[i+1]), color, 2)

        # Save optical flow
        optical_flow_path = output_dir / 'optical_flow.png'
        cv2.imwrite(str(optical_flow_path), tracks_frame)
        print(f"   ✅ Saved: {optical_flow_path}")

        # 2. Generate Heatmap Visualization
        stationary_threshold_seconds = 2
        stationary_threshold_frame = round(vid_fps * stationary_threshold_seconds / data_record_frame)
        stationary_distance = frame_size * 0.05

        # Find stationary points
        stationary_points = []
        for track in tracks:
            stationary_count = 1
            last_stationary = track[0] if track else None
            
            for i in range(1, len(track)):
                if last_stationary and euclidean(track[i], last_stationary) < stationary_distance:
                    stationary_count += 1
                else:
                    if stationary_count >= stationary_threshold_frame:
                        stationary_points.append([last_stationary, stationary_count])
                    stationary_count = 1
                    last_stationary = track[i]
            
            # Check final segment
            if stationary_count >= stationary_threshold_frame and last_stationary:
                stationary_points.append([last_stationary, stationary_count])

        # Create heatmap
        heatmap_frame = np.copy(background_frame)
        heatmap = np.zeros((heatmap_frame.shape[0], heatmap_frame.shape[1]), dtype=np.uint8)
        
        max_stationary_time = 120
        blob_layer = 50
        max_blob_size = frame_size * 0.1
        layer_size = max_blob_size / blob_layer
        color_start = 210
        color_steps = int((color_start - 0) / blob_layer)
        scale = 1.5

        def draw_blob(frame, coordinates, time):
            if time >= max_stationary_time:
                layer = blob_layer
            else:
                layer = ceil(time * scale / layer_size)
            for x in reversed(range(layer)):
                color = color_start - (color_steps * x)
                size = x * layer_size
                cv2.circle(frame, coordinates, int(size), (color, color, color), -1)

        for points in stationary_points:
            draw_heatmap = np.zeros((heatmap_frame.shape[0], heatmap_frame.shape[1]), dtype=np.uint8)
            draw_blob(draw_heatmap, tuple(points[0]), points[1])
            heatmap = cv2.add(heatmap, draw_heatmap)

        # Apply colormap
        lo = np.array([color_start])
        hi = np.array([255])
        mask = cv2.inRange(heatmap, lo, hi)
        heatmap[mask > 0] = color_start

        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
        
        # Mask out background
        lo = np.array([128, 0, 0])
        hi = np.array([136, 0, 0])
        mask = cv2.inRange(heatmap, lo, hi)
        heatmap[mask > 0] = (0, 0, 0)

        for row in range(heatmap.shape[0]):
            for col in range(heatmap.shape[1]):
                if (heatmap[row][col] == np.array([0, 0, 0])).all():
                    heatmap[row][col] = heatmap_frame[row][col]

        final_heatmap = cv2.addWeighted(heatmap, 0.75, heatmap_frame, 0.25, 1)

        # Save heatmap
        heatmap_path = output_dir / 'heatmap.png'
        cv2.imwrite(str(heatmap_path), final_heatmap)
        print(f"   ✅ Saved: {heatmap_path}")

        return True

    except Exception as e:
        print(f"   ❌ Error generating movement plots: {str(e)}")
        return False

def generate_energy_analysis_plots(output_dir):
    """Generate energy level analysis plots"""
    print("⚡ Generating energy analysis plots...")
    
    try:
        # Load video metadata
        with open('processed_data/video_data.json', 'r') as file:
            data = json.load(file)
            data_record_frame = data["DATA_RECORD_FRAME"]
            frame_size = data["PROCESSED_FRAME_SIZE"]
            vid_fps = data["VID_FPS"]

        track_max_age = 3
        time_steps = data_record_frame / vid_fps
        stationary_time = ceil(track_max_age / time_steps)
        stationary_distance = frame_size * 0.01

        # Load and process tracks
        tracks = []
        with open('processed_data/movement_data.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if len(row[3:]) > stationary_time * 2:
                    temp = []
                    data = row[3:]
                    for i in range(0, len(data), 2):
                        if i + 1 < len(data):
                            try:
                                temp.append([int(data[i]), int(data[i+1])])
                            except ValueError:
                                break
                    if len(temp) > stationary_time:
                        tracks.append(temp)

        if not tracks:
            print("   ⚠️ No tracking data available for energy analysis")
            return False

        # Process useful tracks and calculate energies
        useful_tracks = []
        for movement in tracks:
            check_index = stationary_time
            start_point = 0
            track = movement[:check_index]
            
            while check_index < len(movement):
                for i in movement[check_index:]:
                    if euclidean(movement[start_point], i) > stationary_distance:
                        track.append(i)
                        start_point += 1
                        check_index += 1
                    else:
                        start_point += 1
                        check_index += 1
                        break
                if len(track) > 1:
                    useful_tracks.append(track)
                track = movement[start_point:check_index]

        # Calculate energies
        energies = []
        for movement in useful_tracks:
            for i in range(len(movement) - 1):
                speed = round(euclidean(movement[i], movement[i+1]) / time_steps, 2)
                energy = int(0.5 * speed ** 2)
                energies.append(energy)

        if not energies:
            print("   ⚠️ No energy data calculated")
            return False

        # Create energy distribution plot
        energies_series = pd.Series(energies)
        df = pd.DataFrame({'Energy': energies_series})

        plt.figure(figsize=(12, 8))
        bins = np.linspace(int(min(energies)), int(max(energies)), 50)
        plt.hist(energies, bins=bins, alpha=0.7, color='skyblue', edgecolor='black')
        plt.title('Distribution of Movement Energy Levels', fontsize=16, fontweight='bold')
        plt.xlabel('Energy Level', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        
        # Add statistics text
        mean_energy = df.Energy.mean()
        std_energy = df.Energy.std()
        acceptable_level = int(mean_energy ** 1.05)
        
        plt.axvline(mean_energy, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_energy:.0f}')
        plt.axvline(acceptable_level, color='orange', linestyle='--', linewidth=2, label=f'Acceptable Level: {acceptable_level}')
        
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Save plot
        energy_plot_path = output_dir / 'energy_distribution.png'
        plt.savefig(energy_plot_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"   ✅ Saved: {energy_plot_path}")
        
        # Create summary statistics plot
        plt.figure(figsize=(10, 6))
        stats_data = df.describe()
        
        plt.bar(range(len(stats_data)), stats_data['Energy'], color='lightcoral', alpha=0.7)
        plt.xticks(range(len(stats_data)), stats_data.index, rotation=45)
        plt.title('Energy Level Statistics Summary', fontsize=16, fontweight='bold')
        plt.ylabel('Energy Value', fontsize=12)
        plt.yscale('log')  # Log scale due to wide range
        plt.tight_layout()
        
        stats_plot_path = output_dir / 'energy_statistics.png'
        plt.savefig(stats_plot_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"   ✅ Saved: {stats_plot_path}")
        
        return True

    except Exception as e:
        print(f"   ❌ Error generating energy analysis plots: {str(e)}")
        return False

def generate_analytics_summary_plot(output_dir):
    """Generate a comprehensive analytics summary plot"""
    print("📈 Generating analytics summary plot...")
    
    try:
        from utils.analytics import CrowdDataAnalyzer
        
        analyzer = CrowdDataAnalyzer('processed_data')
        
        # Get analytics data
        crowd_analysis = analyzer.analyze_crowd_density()
        social_analysis = analyzer.analyze_social_distancing()
        abnormal_analysis = analyzer.analyze_abnormal_activity()
        
        # Create a comprehensive dashboard
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Crowd Analysis Dashboard', fontsize=20, fontweight='bold')
        
        # 1. Crowd size over time
        if analyzer.crowd_data is not None:
            ax1.plot(analyzer.crowd_data['Human Count'], color='blue', linewidth=2)
            ax1.set_title('Crowd Size Over Time', fontsize=14, fontweight='bold')
            ax1.set_xlabel('Frame')
            ax1.set_ylabel('Number of People')
            ax1.grid(True, alpha=0.3)
            
            # 2. Social distance violations
            ax2.plot(analyzer.crowd_data['Social Distance violate'], color='red', linewidth=2)
            ax2.set_title('Social Distance Violations', fontsize=14, fontweight='bold')
            ax2.set_xlabel('Frame')
            ax2.set_ylabel('Violation Count')
            ax2.grid(True, alpha=0.3)
            
            # 3. Summary statistics pie chart
            violation_frames = (analyzer.crowd_data['Social Distance violate'] > 0).sum()
            normal_frames = len(analyzer.crowd_data) - violation_frames
            
            ax3.pie([normal_frames, violation_frames], 
                   labels=['Normal', 'Violations'], 
                   colors=['green', 'red'],
                   autopct='%1.1f%%')
            ax3.set_title('Frame Distribution', fontsize=14, fontweight='bold')
            
            # 4. Key metrics table
            ax4.axis('off')
            metrics = [
                ['Metric', 'Value'],
                ['Avg Crowd Size', f"{crowd_analysis.get('avg_crowd_size', 0):.1f}"],
                ['Peak Crowd Size', f"{crowd_analysis.get('max_crowd_size', 0)}"],
                ['Violation Rate', f"{social_analysis.get('violation_rate', 0):.1%}"],
                ['Total Violations', f"{social_analysis.get('total_violations', 0)}"],
                ['Abnormal Rate', f"{abnormal_analysis.get('abnormal_rate', 0):.1%}"],
            ]
            
            table = ax4.table(cellText=metrics[1:], 
                             colLabels=metrics[0],
                             cellLoc='center',
                             loc='center')
            table.auto_set_font_size(False)
            table.set_fontsize(12)
            table.scale(1.2, 2)
            ax4.set_title('Key Metrics', fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        
        # Save dashboard
        dashboard_path = output_dir / 'analytics_dashboard.png'
        plt.savefig(dashboard_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"   ✅ Saved: {dashboard_path}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error generating analytics summary: {str(e)}")
        return False

def main():
    """Main function to generate all visualizations"""
    print("🎨 Enhanced Visualization Generator")
    print("=" * 50)
    
    # Create output directory
    output_dir = create_output_directory()
    print(f"📁 Output directory: {output_dir}")
    print()
    
    # Generate all plots
    results = []
    results.append(generate_crowd_data_plots(output_dir))
    results.append(generate_movement_plots(output_dir))
    results.append(generate_energy_analysis_plots(output_dir))
    results.append(generate_analytics_summary_plot(output_dir))
    
    # Summary
    print()
    print("📊 Generation Summary:")
    print(f"   ✅ Successful: {sum(results)}")
    print(f"   ❌ Failed: {len(results) - sum(results)}")
    print()
    print(f"🎯 All generated plots are saved in: {output_dir}")
    print("   You can view them with any image viewer!")

if __name__ == "__main__":
    main()
