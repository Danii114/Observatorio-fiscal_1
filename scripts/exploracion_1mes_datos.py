import pandas as pd

# 🔹 Cargar datos
df = pd.read_parquet("secop_ultimo_mes.parquet")
df['cuantia_contrato'] = pd.to_numeric(df['cuantia_contrato'], errors='coerce')

print("🚀 INICIANDO EXPLORACIÓN DE DATOS\n")

# =========================================================
# 📊 1. VISIÓN GENERAL
# =========================================================
print("📊 DIMENSIÓN DEL DATASET")
print(df.shape)

print("\n📋 COLUMNAS")
print(df.columns)

print("\n🔎 TIPOS DE DATOS")
print(df.dtypes)


# =========================================================
# ❗ 2. CALIDAD DE DATOS
# =========================================================
print("\n❗ VALORES NULOS (TOP 20)")
nulos = df.isnull().sum().sort_values(ascending=False)
print(nulos.head(20))

print("\n📊 PORCENTAJE DE NULOS")
porcentaje_nulos = (df.isnull().sum() / len(df)) * 100
print(porcentaje_nulos.sort_values(ascending=False).head(10))

# 🔥 IMPORTANTE: usar UID para duplicados
print("\n🆔 DUPLICADOS POR UID")
print(df['uid'].duplicated().sum())


# =========================================================
# 🧪 3. VARIABLES CATEGÓRICAS
# =========================================================
print("\n📊 MODALIDAD DE CONTRATACIÓN")
print(df['modalidad_de_contratacion'].value_counts())

print("\n📊 ESTADO DEL PROCESO")
print(df['estado_del_proceso'].value_counts())

print("\n📊 TIPO DE CONTRATO")
print(df['tipo_de_contrato'].value_counts().head(10))


# =========================================================
# 💰 4. VARIABLES NUMÉRICAS
# =========================================================
print("\n📈 ESTADÍSTICAS DE CUANTÍA")
print(df['cuantia_contrato'].describe())

print("\n💰 TOP 10 CONTRATOS MÁS ALTOS")
print(df[['nombre_entidad', 'cuantia_contrato']]
      .sort_values(by='cuantia_contrato', ascending=False)
      .head(10))

print("\n⚠️ CONTRATOS CON VALOR 0")
print((df['cuantia_contrato'] == 0).sum())


# =========================================================
# 🗺️ 5. ANÁLISIS GEOGRÁFICO
# =========================================================
print("\n📍 TOP DEPARTAMENTOS")
print(df['departamento_entidad'].value_counts().head(10))

print("\n🏙️ TOP MUNICIPIOS")
print(df['municipio_entidad'].value_counts().head(10))


# =========================================================
# 🏛️ 6. ENTIDADES
# =========================================================
print("\n🏛️ ENTIDADES CON MÁS CONTRATOS")
print(df['nombre_entidad'].value_counts().head(10))

print("\n💰 ENTIDADES CON MAYOR VALOR CONTRATADO")
print(df.groupby('nombre_entidad')['cuantia_contrato']
      .sum()
      .sort_values(ascending=False)
      .head(10))


# =========================================================
# 🧠 7. CONCENTRACIÓN DEL GASTO
# =========================================================
total = df['cuantia_contrato'].sum()

top10 = df.groupby('nombre_entidad')['cuantia_contrato']\
          .sum().sort_values(ascending=False).head(10).sum()

print("\n📊 CONCENTRACIÓN DEL GASTO")
print("Top 10 entidades concentran:", (top10 / total) * 100, "%")


# =========================================================
# ⚠️ 8. DETECCIÓN DE PROBLEMAS
# =========================================================
print("\n📅 FECHAS FALTANTES")
print(df[['fecha_de_firma_del_contrato',
          'fecha_ini_ejec_contrato',
          'fecha_fin_ejec_contrato']].isnull().sum())

print("\n🔤 VALORES ÚNICOS EN MODALIDAD (detección de errores)")
print(df['modalidad_de_contratacion'].unique())

print("\n💸 VALORES NULOS EN CUANTÍA")
print(df['cuantia_contrato'].isnull().sum())


# =========================================================
# 📊 9. ANÁLISIS TEMPORAL
# =========================================================
df['fecha'] = pd.to_datetime(df['fecha_de_cargue_en_el_secop'], errors='coerce')

print("\n📅 RANGO DE FECHAS")
print("Desde:", df['fecha'].min())
print("Hasta:", df['fecha'].max())

print("\n📊 CONTRATOS POR DÍA")
print(df['fecha'].dt.date.value_counts().sort_index())


print("\n🎯 EXPLORACIÓN FINALIZADA")