
import subprocess
import time
import webbrowser
import os
import urllib.request

# Caminho do projeto
projeto_path = os.path.join(os.path.expanduser("~"), "Downloads", "Auto-Docs-main", "Auto-Docs-main")
os.chdir(projeto_path)

# Inicia o Streamlit
print("▶️ Iniciando Streamlit...")
subprocess.Popen(["python", "-m", "streamlit", "run", "app.py"], shell=True)

# Verifica quando o servidor estiver online
url = "http://localhost:8501"
print("⏳ Aguardando servidor iniciar...")
for _ in range(30):
    try:
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print("✅ Servidor online! Abrindo navegador...")
            webbrowser.open(url)
            break
    except:
        time.sleep(1)
else:
    print("❌ Streamlit não respondeu após 30 segundos.")
