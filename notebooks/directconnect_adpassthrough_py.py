# Databricks notebook source
# MAGIC %md
# MAGIC ## Azure DataLake Gen2
# MAGIC 
# MAGIC 1. Azure Databricks Premium Plan.
# MAGIC 2. Azure Data Lake Storage Gen2: Databricks Runtime 5.3 or above.
# MAGIC 3. High concurrency clusters, which support only Python and SQL. [Enabled AD Passthrough checkbox under Advanced Options](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/adls-passthrough.html#enable-passthrough-for-a-cluster)
# MAGIC 4. User needs to have [Storage Data Blob Owner/Contributor/Reader role](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-rbac-portal#rbac-roles-for-blobs-and-queues) OR [appropriate ACL permissions (R/W/E) on ADLA Gen2](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-access-control#access-control-lists-on-files-and-directories) is granted

# COMMAND ----------

# Try to access file
# You'll need data.csv at root of container/filesystem
df = spark.read.csv("abfss://<STORAGE_CONTAINER>@<STORAGE_ACCOUNT>.dfs.core.windows.net/data.csv")
display(df)