@echo off
set PYTHON_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python313\python.exe

"%PYTHON_PATH%" --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python 3.13 nao encontrado - Execute startup.bat primeiro
    pause
    exit /b 1
)

"%PYTHON_PATH%" -c "import pandas, numpy, bert_score" >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Dependencias nao instaladas - Execute startup.bat primeiro
    pause
    exit /b 1
)

"%PYTHON_PATH%" src\main.py

echo.
echo Arquivos gerados:
if exist "resultados\resultados_detalhados.csv" echo ✅ resultados\resultados_detalhados.csv
if exist "resultados\resumo_estatistico.csv" echo ✅ resultados\resumo_estatistico.csv  
if exist "dados\frases_parafraseadas.txt" echo ✅ dados\frases_parafraseadas.txt
pause
