import subprocess
import time
import webbrowser
import os

# Caminho relativo: assume que a pasta "Auto-Docs-main" está em Downloads
base = os.path.expanduser("~")  # C:\Users\NOME
projeto_path = os.path.join(base, "Downloads", "Auto-Docs-main", "Auto-Docs-main")

# Troca de diretório
os.chdir(projeto_path)

# Inicia o Streamlit
subprocess.Popen(["python", "-m", "streamlit", "run", "app.py", "--server.headless", "true"], shell=True)

# Aguarda e abre no navegador
time.sleep(4)
webbrowser.open("http://localhost:8501", new=2)
