import requests
import pandas as pd
from datetime import datetime, timedelta

URL = "https://www.datos.gov.co/resource/f789-7hwg.json"

# 🔹 calcular último mes
hoy = datetime.today()
hace_un_mes = hoy - timedelta(days=30)

fecha_inicio = hace_un_mes.strftime('%Y-%m-%dT%H:%M:%S')

params = {
    "$where": f"fecha_de_cargue_en_el_secop >= '{fecha_inicio}'",
    "$limit": 50000
}

response = requests.get(URL, params=params)
data = response.json()

df = pd.DataFrame(data)
print("Filas descargadas:", df.shape[0])
print("Columnas:", df.shape[1])
print("Fecha mínima:", df["fecha_de_cargue_en_el_secop"].min())
print("Fecha máxima:", df["fecha_de_cargue_en_el_secop"].max())

df.to_parquet("secop_ultimo_mes.parquet", engine="pyarrow")

print("✅ Último mes descargado")


df = pd.read_parquet("secop_ultimo_mes.parquet")

print(df.head())
print(df.shape)
df.to_csv("secop_ultimo_mes.csv", index=False)
