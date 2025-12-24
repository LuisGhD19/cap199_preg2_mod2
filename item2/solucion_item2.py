# Solución ítem 2
import pandas as pd
import zipfile
import io
import requests

# URL directa al ZIP (raw)
url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/raw/master/Cancer_Pulmon.zip"

# Descargar el archivo ZIP
response = requests.get(url)
response.raise_for_status()

# Abrir el ZIP en memoria y cargar el CSV
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    df = pd.read_csv(z.open(z.namelist()[0]))

# Verificar carga
df.head()
