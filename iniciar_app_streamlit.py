import subprocess
import time
import re
import webbrowser
import threading

# Expressão para encontrar qualquer URL válida do streamlit
url_pattern = re.compile(r"(http://(?:localhost|127\.0\.0\.1|10(?:\.\d+){3}):\d+)")

def abrir_url_quando_disponivel(proc):
    for line in iter(proc.stdout.readline, b''):
        texto = line.decode('utf-8', errors='ignore').strip()
        print(texto)  # (opcional: para depuração)
        match = url_pattern.search(texto)
        if match:
            url = match.group(1)
            print(f"\n✅ URL detectada: {url}\n")
            webbrowser.open(url)
            break

# Comando do Streamlit
comando = ["python", "-m", "streamlit", "run", "app.py"]

# Inicia o processo com saída capturável
processo = subprocess.Popen(
    comando,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    bufsize=1
)

# Roda leitor da URL em outra thread
thread = threading.Thread(target=abrir_url_quando_disponivel, args=(processo,))
thread.start()
