"""
Windows-Compatible Plot Generator
Fixes cross-platform file handling issues
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for Windows
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pathlib import Path
import os
import time
import sys
from datetime import datetime
import json
import csv

def force_delete_existing_plots(output_dir):
    """Force delete existing plots - Windows specific"""
    try:
        output_dir = Path(output_dir)
        if output_dir.exists():
            for plot_file in output_dir.glob('*.png'):
                try:
                    plot_file.unlink()
                    print(f"🗑️ Deleted: {plot_file.name}")
                except PermissionError:
                    # Try alternative deletion method
                    os.chmod(plot_file, 0o777)
                    plot_file.unlink()
                    print(f"🔓 Force deleted: {plot_file.name}")
        return True
    except Exception as e:
        print(f"❌ Deletion error: {e}")
        return False

def create_windows_directory(output_dir):
    """Create directory with Windows-specific permissions"""
    try:
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
        
        # Set Windows permissions
        os.chmod(output_dir, 0o777)
        print(f"📁 Directory ready: {output_dir}")
        return True
    except Exception as e:
        print(f"❌ Directory error: {e}")
        return False

def safe_plot_save(plt_obj, file_path, plot_name):
    """Windows-safe plot saving with verification"""
    try:
        file_path = Path(file_path)
        
        # Delete existing file
        if file_path.exists():
            file_path.unlink()
        
        # Save plot
        plt_obj.savefig(str(file_path), dpi=300, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
        
        # Add small delay for Windows file system
        time.sleep(0.1)
        
        # Verify creation
        if file_path.exists():
            size = file_path.stat().st_size
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"✅ [{timestamp}] Created: {plot_name} ({size} bytes)")
            return True
        else:
            print(f"❌ Failed to create: {plot_name}")
            return False
            
    except Exception as e:
        print(f"❌ Save error for {plot_name}: {e}")
        return False
    finally:
        plt_obj.close()

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
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 5:
                    human_count.append(int(row[1]))
                    violate_count.append(int(row[2]))
                    restricted_entry.append(int(row[3]))
                    abnormal_activity.append(int(row[4]))

        # Load video metadata
        with open('processed_data/video_data.json', 'r') as file:
            video_data = json.load(file)
            
        start_time = video_data['start_time']
        data_record_frame = video_data['data_record_frame']
        vid_fps = video_data['vid_fps']

        start_time = datetime.strptime(start_time, "%d/%m/%Y, %H:%M:%S")
        time_steps = data_record_frame / vid_fps
        data_length = len(human_count)

        # Create time axis
        time_axis = []
        graph_height = max(human_count) if human_count else 10

        fig, ax = plt.subplots(figsize=(12, 8))
        time = start_time
        
        for i in range(data_length):
            time_axis.append(time)
            time = time + pd.Timedelta(seconds=time_steps)

        # Plot lines
        violate_line, = plt.plot(time_axis, violate_count, linewidth=3, label="Violation Count", color='orange')
        crowd_line, = plt.plot(time_axis, human_count, linewidth=3, label="Crowd Count", color='green')
        
        plt.title("Crowd Data Analysis Over Time", fontsize=16, fontweight='bold')
        plt.xlabel("Time", fontsize=12)
        plt.ylabel("Count", fontsize=12)
        
        # Create legend
        plt.legend()
        
        # Add grid
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Save plot
        crowd_plot_path = output_dir / 'crowd_data_analysis.png'
        return safe_plot_save(plt, crowd_plot_path, "Crowd Data Analysis")
        
    except Exception as e:
        print(f"   ❌ Error generating crowd data plots: {str(e)}")
        return False

def generate_movement_plots(output_dir):
    """Generate movement data visualizations"""
    print("🚶 Generating movement plots...")
    
    try:
        tracks = []
        
        with open('processed_data/movement_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 4:
                    temp = []
                    data = row[3].split()
                    for i in range(0, len(data)-1, 2):
                        if i+1 < len(data):
                            try:
                                temp.append([int(data[i]), int(data[i+1])])
                            except ValueError:
                                continue
                    if len(temp) > 2:
                        tracks.append(temp)

        # Load video metadata
        with open('processed_data/video_data.json', 'r') as file:
            video_data = json.load(file)
            frame_width = video_data['frame_width']
            frame_height = video_data['frame_height']

        # Generate optical flow plot
        fig, ax = plt.subplots(figsize=(12, 8))
        
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
        
        for i, track in enumerate(tracks[:50]):  # Limit to 50 tracks for clarity
            track = np.array(track)
            color = colors[i % len(colors)]
            ax.plot(track[:, 0], track[:, 1], color=color, linewidth=2, alpha=0.7)
            ax.plot(track[0, 0], track[0, 1], 'o', color=color, markersize=8, alpha=0.8)
        
        ax.set_xlim(0, frame_width)
        ax.set_ylim(frame_height, 0)  # Invert y-axis for image coordinates
        ax.set_title("Movement Tracking - Optical Flow", fontsize=16, fontweight='bold')
        ax.set_xlabel("X Position", fontsize=12)
        ax.set_ylabel("Y Position", fontsize=12)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save optical flow
        optical_flow_path = output_dir / 'optical_flow.png'
        success1 = safe_plot_save(plt, optical_flow_path, "Optical Flow")
        
        # Generate heatmap
        if tracks:
            fig, ax = plt.subplots(figsize=(12, 8))
            
            # Extract all points
            all_points = []
            for track in tracks:
                all_points.extend(track)
            
            if all_points:
                all_points = np.array(all_points)
                
                # Create 2D histogram for heatmap
                heatmap, xedges, yedges = np.histogram2d(all_points[:, 0], all_points[:, 1], 
                                                       bins=50, range=[[0, frame_width], [0, frame_height]])
                
                # Display heatmap
                im = ax.imshow(heatmap.T, origin='lower', extent=[0, frame_width, 0, frame_height], 
                             cmap='hot', interpolation='gaussian')
                ax.set_title("Activity Heatmap", fontsize=16, fontweight='bold')
                ax.set_xlabel("X Position", fontsize=12)
                ax.set_ylabel("Y Position", fontsize=12)
                plt.colorbar(im, ax=ax, label='Activity Density')
                
                plt.tight_layout()
                
                # Save heatmap
                heatmap_path = output_dir / 'heatmap.png'
                success2 = safe_plot_save(plt, heatmap_path, "Activity Heatmap")
                
                return success1 and success2
        
        return success1
        
    except Exception as e:
        print(f"   ❌ Error generating movement plots: {str(e)}")
        return False

def generate_energy_analysis_plots(output_dir):
    """Generate energy level analysis plots"""
    print("⚡ Generating energy analysis plots...")
    
    try:
        # Load video metadata
        with open('processed_data/video_data.json', 'r') as file:
            video_data = json.load(file)
            frame_width = video_data['frame_width']
            frame_height = video_data['frame_height']

        # Load movement data and calculate energy
        tracks = []
        with open('processed_data/movement_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 4:
                    temp = []
                    data = row[3].split()
                    for i in range(0, len(data)-1, 2):
                        if i+1 < len(data):
                            try:
                                temp.append([int(data[i]), int(data[i+1])])
                            except ValueError:
                                continue
                    if len(temp) > 5:  # Need sufficient points for energy calculation
                        tracks.append(temp)

        if not tracks:
            print("   ❌ No sufficient tracking data for energy analysis")
            return False

        # Calculate movement energy for each track
        energies = []
        for track in tracks:
            track = np.array(track)
            distances = np.sqrt(np.sum(np.diff(track, axis=0)**2, axis=1))
            total_energy = np.sum(distances)
            energies.append(total_energy)

        if not energies:
            print("   ❌ No energy data calculated")
            return False

        # Create energy distribution plot
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle("Movement Energy Analysis", fontsize=16, fontweight='bold')

        # Energy distribution histogram
        ax1.hist(energies, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
        ax1.set_title('Energy Level Distribution')
        ax1.set_xlabel('Movement Energy')
        ax1.set_ylabel('Frequency')
        ax1.grid(True, alpha=0.3)

        # Energy vs Track length
        track_lengths = [len(track) for track in tracks]
        ax2.scatter(track_lengths, energies, alpha=0.6, s=30)
        ax2.set_title('Energy vs Track Duration')
        ax2.set_xlabel('Track Length (frames)')
        ax2.set_ylabel('Movement Energy')
        ax2.grid(True, alpha=0.3)

        # Box plot of energy levels
        ax3.boxplot(energies)
        ax3.set_title('Energy Level Statistics')
        ax3.set_ylabel('Movement Energy')
        ax3.grid(True, alpha=0.3)

        # Energy over time (if we have timestamps)
        ax4.plot(range(len(energies)), sorted(energies), 'g-', linewidth=2)
        ax4.set_title('Energy Levels (Sorted)')
        ax4.set_xlabel('Track Index')
        ax4.set_ylabel('Movement Energy')
        ax4.grid(True, alpha=0.3)

        plt.tight_layout()

        # Save plot
        energy_plot_path = output_dir / 'energy_distribution.png'
        success1 = safe_plot_save(plt, energy_plot_path, "Energy Distribution")

        # Generate energy statistics summary
        fig, ax = plt.subplots(figsize=(10, 8))
        
        stats_text = f"""
MOVEMENT ENERGY ANALYSIS SUMMARY

Total Tracks Analyzed: {len(tracks)}
Average Energy: {np.mean(energies):.2f}
Maximum Energy: {np.max(energies):.2f}
Minimum Energy: {np.min(energies):.2f}
Standard Deviation: {np.std(energies):.2f}

Energy Quartiles:
Q1 (25%): {np.percentile(energies, 25):.2f}
Q2 (50%): {np.percentile(energies, 50):.2f}
Q3 (75%): {np.percentile(energies, 75):.2f}

High Energy Tracks: {sum(1 for e in energies if e > np.percentile(energies, 75))}
Low Energy Tracks: {sum(1 for e in energies if e < np.percentile(energies, 25))}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        ax.text(0.1, 0.9, stats_text, fontsize=12, verticalalignment='top',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgreen", alpha=0.8),
                transform=ax.transAxes, fontfamily='monospace')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.set_title('Energy Analysis Statistics', fontsize=16, fontweight='bold', pad=20)

        stats_plot_path = output_dir / 'energy_statistics.png'
        success2 = safe_plot_save(plt, stats_plot_path, "Energy Statistics")
        
        return success1 and success2
        
    except Exception as e:
        print(f"   ❌ Error generating energy analysis plots: {str(e)}")
        return False

def generate_analytics_summary_plot(output_dir):
    """Generate a comprehensive analytics summary plot"""
    print("📈 Generating analytics summary plot...")
    
    try:
        # Load all data
        crowd_df = pd.read_csv('processed_data/crowd_data.csv')
        
        # Create comprehensive dashboard
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Complete Analytics Dashboard', fontsize=16, fontweight='bold')

        # Time series of crowd data
        ax1.plot(crowd_df.index, crowd_df['Human Count'], 'b-', linewidth=2, label='People Count')
        ax1_twin = ax1.twinx()
        ax1_twin.plot(crowd_df.index, crowd_df['Social Distance violate'], 'r-', linewidth=2, label='Violations')
        ax1.set_title('Crowd Analysis Over Time')
        ax1.set_xlabel('Time (frames)')
        ax1.set_ylabel('People Count', color='blue')
        ax1_twin.set_ylabel('Violations', color='red')
        ax1.legend(loc='upper left')
        ax1_twin.legend(loc='upper right')
        ax1.grid(True, alpha=0.3)

        # Distribution plots
        ax2.hist(crowd_df['Human Count'], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
        ax2.set_title('People Count Distribution')
        ax2.set_xlabel('Number of People')
        ax2.set_ylabel('Frequency')
        ax2.grid(True, alpha=0.3)

        # Correlation analysis
        correlation = crowd_df[['Human Count', 'Social Distance violate']].corr()
        im = ax3.imshow(correlation, cmap='coolwarm', vmin=-1, vmax=1)
        ax3.set_title('Data Correlation Matrix')
        ax3.set_xticks(range(len(correlation.columns)))
        ax3.set_yticks(range(len(correlation.columns)))
        ax3.set_xticklabels(['People', 'Violations'], rotation=45)
        ax3.set_yticklabels(['People', 'Violations'])
        
        # Add correlation values
        for i in range(len(correlation.columns)):
            for j in range(len(correlation.columns)):
                ax3.text(j, i, f'{correlation.iloc[i, j]:.2f}', 
                        ha='center', va='center', fontweight='bold')

        # Summary statistics
        stats_text = f"""ANALYSIS SUMMARY

Max People: {crowd_df['Human Count'].max()}
Avg People: {crowd_df['Human Count'].mean():.1f}
Min People: {crowd_df['Human Count'].min()}

Max Violations: {crowd_df['Social Distance violate'].max()}
Avg Violations: {crowd_df['Social Distance violate'].mean():.1f}
Total Violations: {crowd_df['Social Distance violate'].sum()}

Data Points: {len(crowd_df)}
Duration: {len(crowd_df)} frames

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""

        ax4.text(0.05, 0.95, stats_text, fontsize=11, verticalalignment='top',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8),
                transform=ax4.transAxes, fontfamily='monospace')
        ax4.set_xlim(0, 1)
        ax4.set_ylim(0, 1)
        ax4.axis('off')

        plt.tight_layout()

        # Save analytics dashboard
        dashboard_path = output_dir / 'analytics_dashboard.png'
        return safe_plot_save(plt, dashboard_path, "Analytics Dashboard")
        
    except Exception as e:
        print(f"   ❌ Error generating analytics summary plot: {str(e)}")
        return False

def main():
    """Main plot generation with Windows compatibility"""
    print("=" * 60)
    print("   WINDOWS-COMPATIBLE PLOT GENERATION")
    print("=" * 60)
    
    # Setup output directory
    output_dir = Path("generated_plots")
    
    print("🧹 Step 1: Cleaning existing plots...")
    force_delete_existing_plots(output_dir)
    
    print("📁 Step 2: Creating fresh directory...")
    if not create_windows_directory(output_dir):
        return False
    
    # Check for data
    data_file = Path("processed_data/crowd_data.csv")
    if not data_file.exists():
        print("❌ Data file not found: processed_data/crowd_data.csv")
        print("💡 Run analysis first to generate data")
        return False
    
    print(f"📊 Step 3: Data verification complete")
    
    # Set matplotlib style
    plt.style.use('default')
    plt.rcParams.update({'font.size': 10})
    
    plots_created = 0
    total_plots = 4
    
    print(f"📈 Step 4: Generating {total_plots} visualization plots...")
    
    # Generate all plots
    results = []
    results.append(generate_crowd_data_plots(output_dir))
    results.append(generate_movement_plots(output_dir))
    results.append(generate_energy_analysis_plots(output_dir))
    results.append(generate_analytics_summary_plot(output_dir))
    
    successful_plots = sum(results)
    
    # Final summary
    print("=" * 60)
    print(f"   PLOT GENERATION COMPLETE")
    print(f"   Successfully created: {successful_plots}/{total_plots} plots")
    print(f"   Location: {output_dir.absolute()}")
    print("=" * 60)
    
    if successful_plots > 0:
        print(f"✅ SUCCESS: {successful_plots} plots generated and saved!")
        
        # List created files
        print("\n📋 Generated files:")
        for plot_file in sorted(output_dir.glob('*.png')):
            size = plot_file.stat().st_size
            mtime = datetime.fromtimestamp(plot_file.stat().st_mtime).strftime('%H:%M:%S')
            print(f"   📊 {plot_file.name} ({size} bytes, created {mtime})")
        
        return True
    else:
        print("❌ FAILURE: No plots were created!")
        return False

if __name__ == "__main__":
    success = main()
    print(f"\n{'✅ All plots generated successfully!' if success else '❌ Plot generation failed!'}")
    print("💡 Check the generated_plots folder for your visualization files.")
