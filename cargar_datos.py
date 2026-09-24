# Databricks notebook source
# MAGIC %md
# MAGIC # Cargar tus datos — Seguros del Pichincha
# MAGIC Córrelo **una vez** en tu workspace (trial) para crear tu catálogo y tus tablas a partir
# MAGIC de los Parquet de `datos/`.
# MAGIC
# MAGIC **Requisito:** este repo debe estar como **Git folder** en tu workspace (Workspace →
# MAGIC Create → Git folder → pega la URL del repo). Así los archivos de `datos/` quedan junto a
# MAGIC este notebook.
# MAGIC
# MAGIC Después de correrlo, tu equipo arma el **Clean Room** y comparte estas tablas.

# COMMAND ----------

dbutils.widgets.text("catalog", "seguros", "Catálogo")
dbutils.widgets.text("schema", "clean_room", "Schema")
CAT = dbutils.widgets.get("catalog")
SCH = dbutils.widgets.get("schema")

# COMMAND ----------

import os, pandas as pd

# Carpeta 'datos/' junto a este notebook (en el Git folder). Si tu ruta difiere, ajústala.
BASE = os.path.join(os.getcwd(), "datos")
print("Leyendo Parquet desde:", BASE)

spark.sql(f"CREATE CATALOG IF NOT EXISTS {CAT}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CAT}.{SCH}")

TABLAS = {"clientes_seguros": "clientes_seguros.parquet", "dim_documento": "dim_documento.parquet", "fact_produccion_individual": "fact_produccion_individual.parquet"}

for tabla, archivo in TABLAS.items():
    pdf = pd.read_parquet(os.path.join(BASE, archivo))
    (spark.createDataFrame(pdf)
        .write.mode("overwrite").option("overwriteSchema", "true")
        .saveAsTable(f"{CAT}.{SCH}.{tabla}"))
    print("OK:", f"{CAT}.{SCH}.{tabla}", "→", spark.table(f"{CAT}.{SCH}.{tabla}").count(), "filas")

# COMMAND ----------

# MAGIC %md
# MAGIC ✅ Listo. Tus tablas están en `{CAT}.{SCH}`. Ahora **tu equipo descubre cómo crear el
# MAGIC Clean Room** e invitar a las otras empresas para cruzar por `id_cliente_hash`.
