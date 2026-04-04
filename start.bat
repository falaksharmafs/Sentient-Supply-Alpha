@echo off
color 0B
echo ========================================================
echo        SENTIENT SUPPLY ALPHA - STARTUP SCRIPT
echo ========================================================
echo.

echo [1/2] Booting Python FastAPI Backend (Port 8000)...
start "Sentient Supply Backend" cmd /k "cd api && .\venv\Scripts\python.exe main.py"
timeout /t 2 /nobreak > nul

echo [2/2] Booting React UI Dashboard (Port 5173)...
start "Sentient Supply Frontend" cmd /k "cd ui && npm run dev"

echo.
echo ========================================================
echo All systems online! 
echo Open your browser to: http://localhost:5173/
echo ========================================================
pause
