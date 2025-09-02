@echo off
echo.
echo ===============================================
echo   PLOT GENERATION DIAGNOSTIC TOOL
echo ===============================================
echo.

echo [1] Testing Python environment...
python --version
if %errorlevel% neq 0 (
    echo [✗] Python not found in PATH
    echo [!] Install Python or add to PATH
    pause
    exit /b 1
) else (
    echo [✓] Python is available
)

echo.
echo [2] Testing required Python packages...
python -c "import matplotlib; print('✓ matplotlib:', matplotlib.__version__)" 2>nul
if %errorlevel% neq 0 (
    echo [✗] matplotlib not found
    echo [!] Run: pip install matplotlib
)

python -c "import pandas; print('✓ pandas:', pandas.__version__)" 2>nul
if %errorlevel% neq 0 (
    echo [✗] pandas not found
    echo [!] Run: pip install pandas
)

python -c "import numpy; print('✓ numpy:', numpy.__version__)" 2>nul
if %errorlevel% neq 0 (
    echo [✗] numpy not found
    echo [!] Run: pip install numpy
)

python -c "import seaborn; print('✓ seaborn:', seaborn.__version__)" 2>nul
if %errorlevel% neq 0 (
    echo [✗] seaborn not found
    echo [!] Run: pip install seaborn
)

echo.
echo [3] Checking project files...
if exist "generate_all_plots_windows.py" (
    echo [✓] generate_all_plots_windows.py exists
) else (
    echo [✗] generate_all_plots_windows.py not found
    echo [!] Make sure you have the Windows-compatible generator
)

if exist "modern_crowd_studio.py" (
    echo [✓] modern_crowd_studio.py exists
) else (
    echo [✗] modern_crowd_studio.py not found
)

echo.
echo [4] Checking generated_plots directory...
if exist "generated_plots" (
    echo [✓] generated_plots directory exists
    echo [!] Contents:
    dir "generated_plots" /b 2>nul
    if %errorlevel% neq 0 (
        echo    (Directory is empty)
    )
) else (
    echo [✗] generated_plots directory not found
    echo [!] Creating directory...
    mkdir "generated_plots"
    if %errorlevel% == 0 (
        echo [✓] Directory created
    ) else (
        echo [✗] Failed to create directory
    )
)

echo.
echo [5] Checking data files...
if exist "processed_data" (
    echo [✓] processed_data directory exists
    if exist "processed_data\crowd_data.csv" (
        echo [✓] crowd_data.csv found
        for %%A in ("processed_data\crowd_data.csv") do echo    Size: %%~zA bytes
    ) else (
        echo [✗] crowd_data.csv not found
        echo [!] Run analysis first to generate data
    )
    
    if exist "processed_data\movement_data.csv" (
        echo [✓] movement_data.csv found
    ) else (
        echo [!] movement_data.csv not found
    )
    
    if exist "processed_data\video_data.json" (
        echo [✓] video_data.json found
    ) else (
        echo [!] video_data.json not found
    )
) else (
    echo [✗] processed_data directory not found
    echo [!] Run analysis first to generate data
)

echo.
echo [6] Testing plot generation...
if exist "processed_data\crowd_data.csv" (
    echo [!] Testing Windows plot generator...
    python generate_all_plots_windows.py
    if %errorlevel% == 0 (
        echo [✓] Plot generation test successful
    ) else (
        echo [✗] Plot generation test failed
        echo [!] Check error messages above
    )
) else (
    echo [!] Cannot test plot generation - no data files
)

echo.
echo [7] Permissions check...
echo [!] Checking write permissions...
echo test > "generated_plots\test_write.txt" 2>nul
if exist "generated_plots\test_write.txt" (
    echo [✓] Write permissions OK
    del "generated_plots\test_write.txt" >nul 2>&1
) else (
    echo [✗] No write permissions
    echo [!] Run fix_windows_plots.bat as administrator
)

echo.
echo ===============================================
echo   DIAGNOSTIC COMPLETE
echo ===============================================
echo.
echo Summary:
echo - If all checks pass: Run your analysis normally
echo - If Python packages missing: Run "pip install -r requirements.txt"
echo - If permission issues: Run "fix_windows_plots.bat" as admin
echo - If data files missing: Run full crowd analysis first
echo.
pause
