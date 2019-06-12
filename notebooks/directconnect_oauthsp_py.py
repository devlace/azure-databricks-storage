# Databricks notebook source
# MAGIC %md
# MAGIC ## Azure DataLake Gen2
# MAGIC 
# MAGIC Pre-requisites:
# MAGIC 1. [Create Service Principle](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal)
# MAGIC 1. Service Principle has [Storage Data Blob Owner/Contributor/Reader role](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-rbac-portal#rbac-roles-for-blobs-and-queues) OR [appropriate ACL permissions (R/W/E) on ADLA Gen2](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-access-control#access-control-lists-on-files-and-directories) is granted
# MAGIC 2. **Databricks Runtime 5.2** or above
# MAGIC 3. ADLS Gen2 storage account in the **same region** as your Azure Databricks workspace

# COMMAND ----------

# Set spark configuration
spark.conf.set("fs.azure.account.auth.type", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id", "<SERVICE_PRINCIPLE_CLIENT_ID>")
spark.conf.set("fs.azure.account.oauth2.client.secret", "<SERVICE_PRINCIPLE_SECRET>")
spark.conf.set("fs.azure.account.oauth2.client.endpoint", "https://login.microsoftonline.com/<DIRECTORY_TENANT_ID>/oauth2/token")

# COMMAND ----------

# Try to access file
# You'll need data.csv at root of container/filesystem
df = spark.read.csv("abfss://<STORAGE_CONTAINER>@<STORAGE_ACCOUNT>.dfs.core.windows.net/data.csv")
display(df)