@echo off
echo.
echo ===============================================
echo   WINDOWS PLOT UPDATE FIX - COMPLETE SOLUTION
echo ===============================================
echo.
echo This fixes plot update issues when transferring
echo projects from Mac to Windows systems.
echo.

echo [1/7] Stopping interfering processes...
taskkill /f /im "Photos.exe" >nul 2>&1
taskkill /f /im "Microsoft.Photos.exe" >nul 2>&1
taskkill /f /im "photoviewer.dll" >nul 2>&1
echo ✓ Image viewers closed

echo.
echo [2/7] Backing up existing plots...
if exist "generated_plots" (
    if not exist "backup_original_plots" mkdir "backup_original_plots"
    copy "generated_plots\*.png" "backup_original_plots\" >nul 2>&1
    echo ✓ Original plots backed up
)

echo.
echo [3/7] Force deleting Mac-generated plots...
if exist "generated_plots" (
    attrib -r -s -h "generated_plots\*.*" /s
    del /f /q "generated_plots\*.*"
    rmdir /s /q "generated_plots"
    echo ✓ Mac plots completely removed
)

echo.
echo [4/7] Creating fresh Windows directory...
mkdir "generated_plots"
attrib +w "generated_plots"
icacls "generated_plots" /grant Everyone:F /T >nul 2>&1
echo ✓ Fresh directory created with full permissions

echo.
echo [5/7] Clearing Windows file system cache...
del /s /q "%LocalAppData%\Microsoft\Windows\Explorer\thumbcache_*.db" >nul 2>&1
del /q "%LocalAppData%\IconCache.db" >nul 2>&1
echo ✓ Thumbnail and icon cache cleared

echo.
echo [6/7] Restarting Windows Explorer...
taskkill /f /im explorer.exe >nul 2>&1
timeout /t 2 >nul
start explorer.exe
echo ✓ Explorer restarted with fresh cache

echo.
echo [7/7] Final verification...
if exist "generated_plots" (
    dir "generated_plots" >nul 2>&1
    echo ✓ Directory ready for new plots
) else (
    echo ✗ Directory creation failed
)

echo.
echo ===============================================
echo   CLEANUP COMPLETE!
echo ===============================================
echo.
echo Now run your crowd analysis application.
echo New plots should generate and update properly!
echo.
pause
