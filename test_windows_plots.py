"""
Quick Windows Plot Generation Test
Tests if the plotting system works correctly
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import os
import time

def test_basic_plot_creation():
    """Test basic plot creation and saving"""
    print("🧪 Testing basic plot creation...")
    
    # Create test directory
    test_dir = Path("test_plots")
    test_dir.mkdir(exist_ok=True)
    
    try:
        # Create simple test plot
        plt.figure(figsize=(10, 6))
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.plot(x, y, 'b-', linewidth=2, label='Test Data')
        plt.title('Windows Compatibility Test Plot')
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Save plot
        test_path = test_dir / "test_plot.png"
        plt.savefig(str(test_path), dpi=300, bbox_inches='tight')
        plt.close()
        
        # Verify creation
        if test_path.exists():
            size = test_path.stat().st_size
            print(f"✅ Basic plot test: SUCCESS ({size} bytes)")
            return True
        else:
            print("❌ Basic plot test: FAILED (file not created)")
            return False
            
    except Exception as e:
        print(f"❌ Basic plot test: FAILED ({e})")
        return False

def test_data_based_plot():
    """Test plot generation with dummy data"""
    print("📊 Testing data-based plotting...")
    
    try:
        # Create dummy data similar to crowd analysis
        data = {
            'Human Count': np.random.randint(15, 35, 50),
            'Social Distance violate': np.random.randint(0, 8, 50),
        }
        df = pd.DataFrame(data)
        
        # Create plot
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # Plot 1: Human count
        ax1.plot(df.index, df['Human Count'], 'g-', linewidth=2, marker='o', markersize=3)
        ax1.set_title('Dummy Human Count Over Time')
        ax1.set_ylabel('Number of People')
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Violations
        ax2.plot(df.index, df['Social Distance violate'], 'r-', linewidth=2, marker='s', markersize=3)
        ax2.set_title('Dummy Violations Over Time')
        ax2.set_xlabel('Time (frames)')
        ax2.set_ylabel('Violations')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save plot
        test_dir = Path("test_plots")
        test_path = test_dir / "data_test_plot.png"
        plt.savefig(str(test_path), dpi=300, bbox_inches='tight')
        plt.close()
        
        if test_path.exists():
            size = test_path.stat().st_size
            print(f"✅ Data plot test: SUCCESS ({size} bytes)")
            return True
        else:
            print("❌ Data plot test: FAILED (file not created)")
            return False
            
    except Exception as e:
        print(f"❌ Data plot test: FAILED ({e})")
        return False

def test_file_overwrite():
    """Test file overwriting capability"""
    print("🔄 Testing file overwrite capability...")
    
    try:
        test_dir = Path("test_plots")
        test_path = test_dir / "overwrite_test.png"
        
        # Create first plot
        plt.figure(figsize=(8, 6))
        plt.plot([1, 2, 3], [1, 2, 3], 'r-', linewidth=3)
        plt.title('First Plot - Should be Overwritten')
        plt.savefig(str(test_path), dpi=300, bbox_inches='tight')
        plt.close()
        
        if not test_path.exists():
            print("❌ Overwrite test: FAILED (first file not created)")
            return False
            
        first_time = test_path.stat().st_mtime
        time.sleep(1)  # Ensure different timestamps
        
        # Create second plot (overwrite)
        plt.figure(figsize=(8, 6))
        plt.plot([1, 2, 3], [3, 2, 1], 'b-', linewidth=3)
        plt.title('Second Plot - Should Replace First')
        plt.savefig(str(test_path), dpi=300, bbox_inches='tight')
        plt.close()
        
        if test_path.exists():
            second_time = test_path.stat().st_mtime
            if second_time > first_time:
                print("✅ Overwrite test: SUCCESS (file updated)")
                return True
            else:
                print("❌ Overwrite test: FAILED (file not updated)")
                return False
        else:
            print("❌ Overwrite test: FAILED (second file not created)")
            return False
            
    except Exception as e:
        print(f"❌ Overwrite test: FAILED ({e})")
        return False

def test_generated_plots_directory():
    """Test the actual generated_plots directory"""
    print("📁 Testing generated_plots directory...")
    
    try:
        plots_dir = Path("generated_plots")
        plots_dir.mkdir(exist_ok=True)
        
        # Test write permission
        test_file = plots_dir / "permission_test.txt"
        with open(test_file, 'w') as f:
            f.write("Permission test")
        
        if test_file.exists():
            test_file.unlink()  # Clean up
            print("✅ Directory test: SUCCESS (write permissions OK)")
            return True
        else:
            print("❌ Directory test: FAILED (no write permissions)")
            return False
            
    except Exception as e:
        print(f"❌ Directory test: FAILED ({e})")
        return False

def cleanup_test_files():
    """Clean up test files"""
    try:
        import shutil
        test_dir = Path("test_plots")
        if test_dir.exists():
            shutil.rmtree(test_dir)
            print("🧹 Test files cleaned up")
    except Exception as e:
        print(f"⚠️ Cleanup warning: {e}")

def main():
    """Run all tests"""
    print("=" * 50)
    print("   WINDOWS PLOT GENERATION TESTS")
    print("=" * 50)
    print()
    
    tests = [
        ("Basic Plot Creation", test_basic_plot_creation),
        ("Data-Based Plotting", test_data_based_plot),
        ("File Overwrite", test_file_overwrite),
        ("Directory Permissions", test_generated_plots_directory)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"Running: {test_name}")
        result = test_func()
        results.append(result)
        print()
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print("=" * 50)
    print(f"   TEST RESULTS: {passed}/{total} PASSED")
    print("=" * 50)
    
    if passed == total:
        print("🎉 ALL TESTS PASSED!")
        print("✅ Your Windows system is ready for plot generation")
        print("💡 You can now run crowd analysis with confidence")
    else:
        print("⚠️ SOME TESTS FAILED")
        print("💡 Issues detected:")
        
        if not results[0]:
            print("  • Basic plotting failed - check matplotlib installation")
        if not results[1]:
            print("  • Data plotting failed - check pandas/numpy")
        if not results[2]:
            print("  • File overwriting failed - check permissions")
        if not results[3]:
            print("  • Directory access failed - run fix_windows_plots.bat")
    
    print()
    cleanup_test_files()
    
    return passed == total

if __name__ == "__main__":
    success = main()
    print(f"Final result: {'SUCCESS' if success else 'NEEDS ATTENTION'}")
    input("Press Enter to exit...")
