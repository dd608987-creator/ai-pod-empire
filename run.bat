@echo off
echo ================================
echo   AI POD EMPIRE - RUN SCRIPT
echo ================================
echo.

REM 1) تفعيل البيئة الافتراضية
echo Activating virtual environment...
call venv\Scripts\activate

REM 2) تثبيت المتطلبات (مرة واحدة فقط)
if exist requirements.txt (
    echo Installing requirements...
    pip install -r requirements.txt
)

REM 3) تشغيل السيرفر
echo Starting AI POD Empire...
start http://127.0.0.1:8000
uvicorn api.main:app --reload

pause
