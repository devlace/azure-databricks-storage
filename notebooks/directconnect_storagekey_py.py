# Databricks notebook source
# MAGIC %md 
# MAGIC ## Azure DataLake Gen2

# COMMAND ----------

# Set spark configuration
spark.conf.set("fs.azure.account.key.<STORAGE_ACCOUNT>.dfs.core.windows.net", "<STORAGE_KEY>")

# Try to access file
# You'll need data.csv at root of container/filesystem
df = spark.read.csv("abfss://<STORAGE_CONTAINER>@<STORAGE_ACCOUNT>.dfs.core.windows.net/data.csv")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Blob storage

# COMMAND ----------

# Set spark configuration
spark.conf.set("fs.azure.account.key.<STORAGE_ACCOUNT>.blob.core.windows.net", "<STORAGE_KEY>")

# Try to access file
# You'll need data.csv at root of container/filesystem
df = spark.read.csv("abfss://<STORAGE_CONTAINER>@<STORAGE_ACCOUNT>.dfs.core.windows.net/data.csv")
display(df)