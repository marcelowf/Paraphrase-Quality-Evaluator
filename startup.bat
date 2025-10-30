@echo off
set PYTHON_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python313\python.exe

"%PYTHON_PATH%" --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python 3.13 nao encontrado
    pause
    exit /b 1
)

echo ✅ Python 3.13 encontrado
"%PYTHON_PATH%" -m pip install --upgrade pip >nul 2>&1
"%PYTHON_PATH%" -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Erro ao instalar dependencias
    pause
    exit /b 1
)

echo ✅ Dependencias instaladas
"%PYTHON_PATH%" -c "import pandas, numpy, bert_score, sentence_transformers" >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Algumas bibliotecas podem ter problemas de conexao
) else (
    echo ✅ Sistema configurado com sucesso
)
pause
