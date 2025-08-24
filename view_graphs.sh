#!/bin/bash

# Script to easily view generated graphs
# Usage: ./view_graphs.sh [graph_name]

PLOTS_DIR="/Users/levi/Crowd-Analysis-main/generated_plots"

echo "🖼️  Available Generated Graphs:"
echo "================================"

if [ $# -eq 0 ]; then
    # List all available graphs
    echo "1. analytics_dashboard.png    - Complete analytics dashboard"
    echo "2. crowd_data_analysis.png    - Crowd count and violations over time"
    echo "3. energy_distribution.png    - Movement energy level distribution" 
    echo "4. energy_statistics.png      - Energy statistics summary"
    echo "5. heatmap.png               - Stationary location heatmap"
    echo "6. optical_flow.png          - Movement tracking visualization"
    echo ""
    echo "Usage examples:"
    echo "  ./view_graphs.sh                    # Show this menu"
    echo "  ./view_graphs.sh dashboard          # Open analytics dashboard"
    echo "  ./view_graphs.sh heatmap            # Open heatmap"
    echo "  ./view_graphs.sh all                # Open all graphs"
    echo ""
    echo "Or you can manually open any file from: $PLOTS_DIR"
else
    case "$1" in
        "dashboard"|"analytics")
            echo "Opening analytics dashboard..."
            open "$PLOTS_DIR/analytics_dashboard.png"
            ;;
        "crowd"|"crowd_data")
            echo "Opening crowd data analysis..."
            open "$PLOTS_DIR/crowd_data_analysis.png"
            ;;
        "energy"|"energy_dist")
            echo "Opening energy distribution..."
            open "$PLOTS_DIR/energy_distribution.png"
            ;;
        "energy_stats"|"stats")
            echo "Opening energy statistics..."
            open "$PLOTS_DIR/energy_statistics.png"
            ;;
        "heatmap"|"heat")
            echo "Opening heatmap..."
            open "$PLOTS_DIR/heatmap.png"
            ;;
        "optical"|"flow"|"tracks")
            echo "Opening optical flow..."
            open "$PLOTS_DIR/optical_flow.png"
            ;;
        "all")
            echo "Opening all graphs..."
            open "$PLOTS_DIR"/*.png
            ;;
        *)
            echo "❌ Unknown graph: $1"
            echo "Run './view_graphs.sh' to see available options"
            ;;
    esac
fi
