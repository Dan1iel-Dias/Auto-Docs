@echo off
cd %USERPROFILE%\Downloads\Auto-Docs

:: Abre o Chrome no endereço do Streamlit
start chrome http://localhost:8501

:: Executa o app Streamlit
python -m streamlit run app.py

pause
