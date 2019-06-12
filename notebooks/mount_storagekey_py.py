# Databricks notebook source
# MAGIC %md
# MAGIC ## Azure DataLake Gen2

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://<STORAGE_CONTAINER_FILESYSTEM>@<STORAGE_ACCOUNT>.dfs.core.windows.net",
  mount_point = "/mnt/my_adls_gen2_mount_path/",
  extra_configs = {"fs.azure.account.key.<STORAGE_ACCOUNT>.dfs.core.windows.net": "<STORAGE_KEY>"})

# Refresh mounts
dbutils.fs.refreshMounts()

# COMMAND ----------

# Sample code to try to access file
# You'll need data.csv at root of container/filesystem
df = spark.read.csv("/mnt/my_adls_gen2_mount_path/data.csv")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Blob storage

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://<STORAGE_CONTAINER_FILESYSTEM>@<STORAGE_ACCOUNT>.blob.core.windows.net",
  mount_point = "/mnt/my_blob_mount_path/",
  extra_configs = {"fs.azure.account.key.<STORAGE_ACCOUNT>.blob.core.windows.net": "<STORAGE_KEY>"})

# Refresh mounts
dbutils.fs.refreshMounts()

# COMMAND ----------

# Sample code to try to access file
# You'll need data.csv at root of container/filesystem
df = spark.read.csv("/mnt/my_blob_mount_path/data.csv")
display(df)