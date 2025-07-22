import subprocess
import time
import webbrowser
import os

# Caminho completo para a pasta Auto-Docs em Documentos
caminho = os.path.join(os.path.expanduser("~"), "Documents", "Auto-Docs")
os.chdir(caminho)

# Inicia o Streamlit
subprocess.Popen(["python", "-m", "streamlit", "run", "app.py"], shell=True)

# Aguarda o servidor iniciar
time.sleep(4)

# Abre o navegador
webbrowser.open("http://localhost:8501", new=2)
