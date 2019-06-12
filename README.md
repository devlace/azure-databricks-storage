# Different ways to connect to storage in Azure Databricks

The following is a summary of the various ways to connect to Blob Storage and Azure Data Lake Gen2 from Azure Databricks.

|How to connect|Scope of connection|Authentication|Authorization Requirements|Supported Storage|Samples|Doc Link
|---|---|---|---|---|---|---|
|**Direct connect**|Typicaly SparkSession*|Storage Key|All rights|Blob Storage, ADLS Gen2|[Python](notebooks/directconnect_storagekey_py.py), [SQL](notebooks/directconnect_storagekey_sql.sql)|[Blob](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-storage.html#access-azure-blob-storage-directly)
|   |   |OAuth via Service Principal (SP)|SP must have **Storage Data Owner/Contributor/Reader** role OR **ACLs permissions** to files/folders|ADLS Gen2|Python, SQL| [ADLS Gen2](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-datalake-gen2.html#access-an-adls-account-directly-with-oauth-2-0-using-the-service-principal)
|   |   |AD Passthrough|SP must have **Storage Data Owner/Contributor/Reader** role OR **ACLs permissions** to files/folders|ADLS Gen2|Python, SQL| [ADLS Gen2](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-datalake-gen2.html#access-adls-automatically-with-your-aad-credentials)
|**Mount on DBFS**|Databricks Workspace|Storage Key|All rights|Blob Storage, ADLS Gen2|Python|[Blob](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-storage.html#mount-azure-blob-storage-containers-with-dbfs), [ADLS Gen2](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-datalake-gen2.html#access-an-adls-account-directly-using-the-storage-account-access-key)
|   |   |OAuth via Service Principal (SP)|SP must have **Storage Data Owner/Contributor/Reader** role OR **ACLs permissions** to files/folders|ADLS Gen2|Python, SQL| [ADLS Gen2](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-datalake-gen2.html#mount-an-adls-filesystem-to-dbfs-using-a-service-principal-and-oauth-2-0)
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |

**This will depend on where Spark Configuration is set. This is typically set on the SparkSession of the running notebook and therefore scoped to only that specific SparkSession.*