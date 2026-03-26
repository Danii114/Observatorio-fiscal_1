import requests
import pandas as pd
from datetime import datetime, timedelta

# 🔹 URL API SECOP
URL = "https://www.datos.gov.co/resource/f789-7hwg.json"

# 🔹 calcular últimos 3 meses (90 días)
hoy = datetime.today()
hace_tres_meses = hoy - timedelta(days=90)

fecha_inicio = hace_tres_meses.strftime('%Y-%m-%dT%H:%M:%S')

print(f"📅 Descargando desde: {fecha_inicio}")

# 🔹 paginación (muy importante)
limit = 50000
offset = 0
all_data = []

while True:
    params = {
        "$where": f"fecha_de_cargue_en_el_secop >= '{fecha_inicio}'",
        "$limit": limit,
        "$offset": offset
    }

    response = requests.get(URL, params=params)

    if response.status_code != 200:
        raise Exception(f"❌ Error API: {response.status_code}")

    data = response.json()

    if not data:
        break

    all_data.extend(data)
    print(f"📦 Registros descargados: {len(all_data)}")

    offset += limit

# 🔹 convertir a DataFrame
df = pd.DataFrame(all_data)

# 🔹 resumen rápido
print("\n📊 RESUMEN")
print("Filas:", df.shape[0])
print("Columnas:", df.shape[1])

# 🔹 guardar parquet
mes = datetime.today().strftime("%Y-%m")
df.to_parquet(f"secop_{mes}.parquet", engine="pyarrow")

print("💾 Archivo guardado: secop_3_meses.parquet")

