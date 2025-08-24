#!/usr/bin/env python3
"""
Crowd Analysis Studio - Professional UI
Step 1: Basic Window Structure and Layout
"""

import tkinter as tk
from tkinter import ttk
import sys

class CrowdAnalysisStudio:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_styles()
        self.setup_layout()
    
    def setup_window(self):
        """Configure main window"""
        self.root.title("🎬 Crowd Analysis Studio")
        self.root.geometry("1400x900")
        self.root.configure(bg='#2b2b2b')
        self.root.resizable(True, True)
        
        # Center window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (900 // 2)
        self.root.geometry(f"1400x900+{x}+{y}")
    
    def setup_styles(self):
        """Configure dark theme styles"""
        style = ttk.Style()
        
        # Configure dark theme colors
        style.theme_use('clam')
        
        # Main frame styles
        style.configure('Dark.TFrame', 
                       background='#2b2b2b',
                       borderwidth=0)
        
        style.configure('Panel.TFrame',
                       background='#3c3c3c',
                       relief='raised',
                       borderwidth=1)
        
        # Label styles
        style.configure('Title.TLabel',
                       background='#2b2b2b',
                       foreground='#ffffff',
                       font=('Arial', 16, 'bold'))
        
        style.configure('Subtitle.TLabel',
                       background='#2b2b2b',
                       foreground='#888888',
                       font=('Arial', 10))
        
        style.configure('Panel.TLabel',
                       background='#3c3c3c',
                       foreground='#ffffff',
                       font=('Arial', 11))
        
        style.configure('PanelTitle.TLabel',
                       background='#3c3c3c',
                       foreground='#ffffff',
                       font=('Arial', 12, 'bold'))
    
    def setup_layout(self):
        """Create main layout structure"""
        # Main container
        main_frame = ttk.Frame(self.root, style='Dark.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title section
        self.create_title_section(main_frame)
        
        # Content area with three panels
        content_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        content_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Configure grid weights for responsive layout
        content_frame.columnconfigure(0, weight=1)  # Analysis Controls
        content_frame.columnconfigure(1, weight=2)  # Live Video Preview  
        content_frame.columnconfigure(2, weight=1)  # Analytics Dashboard
        content_frame.rowconfigure(0, weight=1)
        
        # Create three main panels
        self.create_analysis_controls_panel(content_frame)
        self.create_video_preview_panel(content_frame)
        self.create_analytics_dashboard_panel(content_frame)
        
    def create_title_section(self, parent):
        """Create title and subtitle"""
        title_frame = ttk.Frame(parent, style='Dark.TFrame')
        title_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Main title
        title_label = ttk.Label(title_frame, 
                               text="🎬 Crowd Analysis Studio",
                               style='Title.TLabel')
        title_label.pack()
        
        # Subtitle
        subtitle_label = ttk.Label(title_frame,
                                  text="Professional AI-Powered Video Analytics",
                                  style='Subtitle.TLabel')
        subtitle_label.pack(pady=(5, 0))
    
    def create_analysis_controls_panel(self, parent):
        """Create left panel - Analysis Controls"""
        controls_frame = ttk.Frame(parent, style='Panel.TFrame')
        controls_frame.grid(row=0, column=0, sticky='nsew', padx=(0, 5))
        
        # Panel header
        header_frame = ttk.Frame(controls_frame, style='Panel.TFrame')
        header_frame.pack(fill=tk.X, padx=15, pady=(15, 10))
        
        ttk.Label(header_frame,
                 text="🎛️ Analysis Controls",
                 style='PanelTitle.TLabel').pack(anchor='w')
        
        # Placeholder content
        content_frame = ttk.Frame(controls_frame, style='Panel.TFrame')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        ttk.Label(content_frame,
                 text="Video Selection\nAnalysis Options\nControls will go here...",
                 style='Panel.TLabel',
                 justify='left').pack(anchor='w', pady=10)
    
    def create_video_preview_panel(self, parent):
        """Create center panel - Live Video Preview"""
        preview_frame = ttk.Frame(parent, style='Panel.TFrame')
        preview_frame.grid(row=0, column=1, sticky='nsew', padx=5)
        
        # Panel header
        header_frame = ttk.Frame(preview_frame, style='Panel.TFrame')
        header_frame.pack(fill=tk.X, padx=15, pady=(15, 10))
        
        header_left = ttk.Frame(header_frame, style='Panel.TFrame')
        header_left.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Label(header_left,
                 text="📺 Live Video Preview",
                 style='PanelTitle.TLabel').pack(anchor='w')
        
        # Fullscreen button (right side)
        header_right = ttk.Frame(header_frame, style='Panel.TFrame')
        header_right.pack(side=tk.RIGHT)
        
        fullscreen_btn = tk.Button(header_right,
                                  text="⛶ Fullscreen",
                                  bg='#4a90e2',
                                  fg='white',
                                  border=0,
                                  padx=10,
                                  pady=5,
                                  font=('Arial', 9))
        fullscreen_btn.pack()
        
        # Video preview area
        video_frame = ttk.Frame(preview_frame, style='Panel.TFrame')
        video_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        # Preview placeholder
        preview_area = tk.Frame(video_frame, bg='#1a1a1a', relief='sunken', bd=2)
        preview_area.pack(fill=tk.BOTH, expand=True)
        
        preview_label = tk.Label(preview_area,
                               text="Real-time processing view\nSelect a video and start analysis",
                               bg='#1a1a1a',
                               fg='#666666',
                               font=('Arial', 14))
        preview_label.place(relx=0.5, rely=0.5, anchor='center')
    
    def create_analytics_dashboard_panel(self, parent):
        """Create right panel - Analytics Dashboard"""
        analytics_frame = ttk.Frame(parent, style='Panel.TFrame')
        analytics_frame.grid(row=0, column=2, sticky='nsew', padx=(5, 0))
        
        # Panel header with tabs
        header_frame = ttk.Frame(analytics_frame, style='Panel.TFrame')
        header_frame.pack(fill=tk.X, padx=15, pady=(15, 10))
        
        ttk.Label(header_frame,
                 text="📊 Analytics Dashboard",
                 style='PanelTitle.TLabel').pack(anchor='w')
        
        # Tab-like buttons
        tab_frame = ttk.Frame(analytics_frame, style='Panel.TFrame')
        tab_frame.pack(fill=tk.X, padx=15, pady=(5, 10))
        
        self.create_tab_button(tab_frame, "📈 Real-time Charts", True)
        self.create_tab_button(tab_frame, "📋 Summary Stats", False)
        self.create_tab_button(tab_frame, "📊 Generated Plots", False)
        
        # Analytics content area
        content_frame = ttk.Frame(analytics_frame, style='Panel.TFrame')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        # Placeholder content
        ttk.Label(content_frame,
                 text="Live analytics charts will appear here\nduring video processing",
                 style='Panel.TLabel',
                 justify='center').place(relx=0.5, rely=0.5, anchor='center')
    
    def create_tab_button(self, parent, text, active=False):
        """Create tab-style button"""
        bg_color = '#4a90e2' if active else '#555555'
        fg_color = 'white'
        
        btn = tk.Button(parent,
                       text=text,
                       bg=bg_color,
                       fg=fg_color,
                       border=0,
                       padx=8,
                       pady=3,
                       font=('Arial', 9))
        btn.pack(side=tk.LEFT, padx=(0, 5))
        return btn

def main():
    """Main function"""
    print("🎬 Starting Crowd Analysis Studio - Step 1: Basic Layout")
    
    root = tk.Tk()
    app = CrowdAnalysisStudio(root)
    root.mainloop()

if __name__ == "__main__":
    main()
