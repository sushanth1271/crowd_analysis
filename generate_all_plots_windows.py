"""
Windows-Compatible Plot Generator
Fixes cross-platform file handling issues
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for Windows
import matplotlib.pyplot as plt
import sys
import os
# Ensure stdout/stderr use UTF-8 to avoid UnicodeEncodeError on Windows consoles
try:
    # Also set env so any subprocesses inherit UTF-8 if needed
    os.environ.setdefault('PYTHONIOENCODING', 'utf-8')
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass
import pandas as pd
import numpy as np
import seaborn as sns
from pathlib import Path
import os
import time
import sys
from datetime import datetime, timedelta
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
        
        # Try to set permissive permissions. os.chmod may be limited on Windows; use icacls as fallback.
        try:
            os.chmod(output_dir, 0o777)
        except Exception:
            try:
                # Grant Everyone full control (silent)
                os.system(f'icacls "{str(output_dir)}" /grant Everyone:F /T >nul 2>&1')
            except Exception:
                pass

        print(f"📁 Directory ready: {output_dir}")
        return True
    except Exception as e:
        print(f"❌ Directory error: {e}")
        return False

def safe_plot_save(plt_obj, file_path, plot_name):
    """Windows-safe plot saving with verification"""
    try:
        file_path = Path(file_path)

        # Create a temp filename that preserves the original image suffix so
        # matplotlib can infer the correct format (e.g., name.tmp.png)
        tmp_name = f"{file_path.stem}.tmp{file_path.suffix}"
        tmp_path = file_path.parent / tmp_name

        # Ensure parent exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Try saving to a temp file then atomically replace the target
        max_attempts = 5
        attempt = 0
        while attempt < max_attempts:
            try:
                # Remove any existing temp file
                if tmp_path.exists():
                    try:
                        tmp_path.unlink()
                    except Exception:
                        pass

                plt_obj.savefig(str(tmp_path), dpi=300, bbox_inches='tight',
                                facecolor='white', edgecolor='none')

                # Small delay for filesystem sync
                time.sleep(0.05)

                # Atomically replace
                try:
                    os.replace(str(tmp_path), str(file_path))
                except Exception:
                    # On some systems os.replace may fail if file locked; try copy+remove
                    try:
                        if file_path.exists():
                            file_path.unlink()
                        tmp_path.replace(file_path)
                    except Exception:
                        pass

                # Verify creation
                if file_path.exists():
                    size = file_path.stat().st_size
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    print(f"✅ [{timestamp}] Created: {plot_name} ({size} bytes)")
                    return True

            except Exception as e:
                # Retry on failure
                import traceback
                print(f"⚠️ Attempt {attempt+1} save error for {plot_name}: {e}")
                traceback.print_exc()
                time.sleep(0.1 * (attempt + 1))
                attempt += 1

        print(f"❌ Failed to create: {plot_name} after {max_attempts} attempts")
        return False

    except Exception as e:
        import traceback
        print(f"⛔ Save error for {plot_name}: {e}")
        traceback.print_exc()
        return False
    finally:
        try:
            plt_obj.close()
        except Exception:
            pass

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

        # Load video metadata (support multiple key formats)
        with open('processed_data/video_data.json', 'r') as file:
            video_data = json.load(file)

        # Normalize keys and provide sensible defaults
        start_time = video_data.get('start_time') or video_data.get('START_TIME') or video_data.get('Start_Time')
        data_record_frame = video_data.get('data_record_frame') or video_data.get('DATA_RECORD_FRAME') or 1
        vid_fps = video_data.get('vid_fps') or video_data.get('VID_FPS') or 30

        # Parse start_time string if present, otherwise use now
        if start_time:
            try:
                start_time = datetime.strptime(start_time, "%d/%m/%Y, %H:%M:%S")
            except Exception:
                try:
                    start_time = datetime.fromisoformat(start_time)
                except Exception:
                    start_time = datetime.now()
        else:
            start_time = datetime.now()

        # Build time axis
        try:
            time_steps = float(data_record_frame) / float(vid_fps) if float(vid_fps) != 0 else 1.0
        except Exception:
            time_steps = 1.0

        data_length = len(human_count)
        time_axis = []
        time_cursor = start_time
        for i in range(data_length):
            time_axis.append(time_cursor)
            time_cursor = time_cursor + timedelta(seconds=time_steps)

        graph_height = max(human_count) if human_count else 10

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

        # Movement CSV format can differ: some runs store the full track as a single
        # space-separated string in column 3, while others place coords as separate
        # CSV columns starting at index 3. Normalize by joining all columns from
        # index 3 onward and splitting on whitespace and commas.
        with open('processed_data/movement_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 4:
                    temp = []
                    # Join all remaining columns and replace commas with spaces,
                    # then split into tokens.
                    raw = ' '.join(row[3:])
                    raw = raw.replace(',', ' ')
                    data = raw.split()
                    # Build (x,y) pairs
                    for i in range(0, len(data)-1, 2):
                        try:
                            x = int(float(data[i]))
                            y = int(float(data[i+1]))
                        except Exception:
                            continue
                        temp.append([x, y])
                    if len(temp) > 2:
                        tracks.append(temp)

        # Load video metadata
        with open('processed_data/video_data.json', 'r') as file:
            video_data = json.load(file)
            frame_width = video_data.get('frame_width') or video_data.get('FRAME_WIDTH') or video_data.get('PROCESSED_FRAME_SIZE') or video_data.get('processed_frame_size')
            frame_height = video_data.get('frame_height') or video_data.get('FRAME_HEIGHT')
            if frame_width and not frame_height:
                # Assume 16:9 aspect ratio if only width provided
                try:
                    frame_width = int(frame_width)
                    frame_height = int(frame_width * 9 / 16)
                except Exception:
                    frame_width = int(frame_width or 1280)
                    frame_height = int(frame_height or 720)
            if not frame_width:
                frame_width = 1280
                frame_height = 720

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
            frame_width = video_data.get('frame_width') or video_data.get('FRAME_WIDTH') or video_data.get('PROCESSED_FRAME_SIZE') or video_data.get('processed_frame_size')
            frame_height = video_data.get('frame_height') or video_data.get('FRAME_HEIGHT')
            if frame_width and not frame_height:
                # Assume 16:9 aspect ratio if only width provided
                try:
                    frame_width = int(frame_width)
                    frame_height = int(frame_width * 9 / 16)
                except Exception:
                    frame_width = int(frame_width or 1280)
                    frame_height = int(frame_height or 720)
            if not frame_width:
                frame_width = 1280
                frame_height = 720

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

        # Create dashboard with two top plots and a large bottom summary
        fig = plt.figure(figsize=(15, 12))
        fig.suptitle('Complete Analytics Dashboard', fontsize=16, fontweight='bold')
        gs = fig.add_gridspec(2, 2, height_ratios=[1, 0.8])

        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[0, 1])
        ax_summary = fig.add_subplot(gs[1, :])

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

        # Summary statistics (large bottom area)
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

        ax_summary.text(0.02, 0.98, stats_text, fontsize=12, verticalalignment='top',
                        bbox=dict(boxstyle="round,pad=0.8", facecolor="lightyellow", alpha=0.95),
                        transform=ax_summary.transAxes, fontfamily='monospace')
        ax_summary.set_xlim(0, 1)
        ax_summary.set_ylim(0, 1)
        ax_summary.axis('off')

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
