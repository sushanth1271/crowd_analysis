@echo off
title Crowd Analysis - Windows Setup and Launch
color 0A

echo.
echo     ╔═══════════════════════════════════════════════════════════╗
echo     ║           CROWD ANALYSIS - WINDOWS LAUNCHER               ║
echo     ║                 One-Click Setup and Run                   ║
echo     ╚═══════════════════════════════════════════════════════════╝
echo.

:MENU
echo ┌─────────────────────────────────────────────────────────────┐
echo │                         MAIN MENU                          │
echo ├─────────────────────────────────────────────────────────────┤
echo │  1. 🛠️  First Time Setup (Fix Windows Plot Issues)          │
echo │  2. 🔍 Run Diagnostics (Check System)                      │
echo │  3. 🧪 Test Plot Generation                                 │
echo │  4. 🚀 Launch Crowd Analysis GUI                           │
echo │  5. 📊 View Generated Plots                                │
echo │  6. 🧹 Clean Reset (Nuclear Option)                        │
echo │  7. ❌ Exit                                                 │
echo └─────────────────────────────────────────────────────────────┘
echo.

set /p choice="Enter your choice (1-7): "

if "%choice%"=="1" goto SETUP
if "%choice%"=="2" goto DIAGNOSTIC
if "%choice%"=="3" goto TEST
if "%choice%"=="4" goto LAUNCH
if "%choice%"=="5" goto VIEW_PLOTS
if "%choice%"=="6" goto CLEAN_RESET
if "%choice%"=="7" goto EXIT
goto INVALID

:SETUP
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║                    FIRST TIME SETUP                      ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo This will fix Windows plot update issues by:
echo  • Clearing Mac-generated plot cache
echo  • Setting proper Windows permissions
echo  • Creating fresh directory structure
echo.
echo ⚠️  This requires Administrator privileges!
echo.
pause
echo.
echo Running Windows plot fix...
call fix_windows_plots.bat
echo.
echo ✅ Setup complete! You can now use option 4 to launch the GUI.
echo.
pause
goto MENU

:DIAGNOSTIC
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║                      DIAGNOSTICS                         ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo Running system diagnostics...
call diagnose_windows_plots.bat
echo.
pause
goto MENU

:TEST
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║                    PLOT GENERATION TEST                  ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo Testing plot generation functionality...
python test_windows_plots.py
echo.
pause
goto MENU

:LAUNCH
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║                   LAUNCHING GUI                          ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo Starting Crowd Analysis Studio...
echo.
echo 📝 Note: The GUI now automatically uses Windows-compatible
echo    plot generation. Your plots should update properly!
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python and try again.
    pause
    goto MENU
)

REM Check if GUI file exists
if not exist "modern_crowd_studio.py" (
    echo ❌ GUI file not found! Make sure you're in the correct directory.
    pause
    goto MENU
)

echo 🚀 Launching GUI...
python modern_crowd_studio.py
echo.
echo GUI closed.
pause
goto MENU

:VIEW_PLOTS
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║                    VIEW PLOTS                            ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
if exist "generated_plots" (
    echo 📊 Generated plots:
    echo.
    dir "generated_plots\*.png" /b 2>nul
    if %errorlevel% == 0 (
        echo.
        echo Opening plots folder...
        start explorer "generated_plots"
    ) else (
        echo    No plots found. Run analysis first.
    )
) else (
    echo    No generated_plots folder found.
    echo    Run analysis first or use option 1 for setup.
)
echo.
pause
goto MENU

:CLEAN_RESET
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║                    NUCLEAR RESET                         ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo ⚠️  WARNING: This will completely reset the analysis system!
echo.
echo This will delete:
echo  • All generated plots
echo  • All processed data
echo  • All cache files
echo.
set /p confirm="Are you sure? (Y/N): "
if /i not "%confirm%"=="Y" goto MENU

echo.
echo 🧹 Performing nuclear reset...

REM Remove directories
if exist "generated_plots" (
    rmdir /s /q "generated_plots"
    echo ✅ Removed generated_plots
)

if exist "processed_data" (
    rmdir /s /q "processed_data"  
    echo ✅ Removed processed_data
)

if exist "backup_original_plots" (
    rmdir /s /q "backup_original_plots"
    echo ✅ Removed backup plots
)

if exist "test_plots" (
    rmdir /s /q "test_plots"
    echo ✅ Removed test plots  
)

REM Clear cache
del /s /q "%LocalAppData%\Microsoft\Windows\Explorer\thumbcache_*.db" >nul 2>&1
echo ✅ Cleared Windows cache

echo.
echo 🔄 Now run option 1 (First Time Setup) to reinitialize.
echo.
pause
goto MENU

:INVALID
echo.
echo ❌ Invalid choice. Please enter a number between 1-7.
echo.
pause
goto MENU

:EXIT
echo.
echo 👋 Thank you for using Crowd Analysis!
echo.
echo 💡 Tips for best results:
echo  • Always run setup (option 1) when first using on Windows
echo  • Use diagnostics (option 2) if you encounter issues  
echo  • Close image viewers before running analysis
echo  • Check that plots update after each analysis
echo.
pause
exit /b 0
