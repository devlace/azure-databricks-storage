# Different ways to connect to storage in Azure Databricks

The following is a summary of the various ways to connect to [Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview) and [Azure Data Lake Gen2](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) from [Azure Databricks](https://docs.azuredatabricks.net/index.html).

To download all sample notebooks, [here](notebooks/connect_storage.dbc) is the DBC archive you can import to your workspace. 

|How to connect|Scope of connection|Authentication|Authorization Requirements|Code Sample|Docs/Supported Storage|
|---|---|---|---|---|---|
|**Direct connect**|Typicaly SparkSession*|Storage Key|All rights|[Python](notebooks/directconnect_storagekey_py.py), [SQL](notebooks/directconnect_storagekey_sql.sql)|[Blob](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-storage.html#access-azure-blob-storage-directly)|
|   |   |OAuth via Service Principal (SP)|**SP has correct RBAC role assigned OR ACLs permissions to files/folders in ADLS Gen2| [Python](notebooks/directconnect_oauthsp_py.py), [SQL](notebooks/directconnect_oauthsp_sql.sql) | [ADLS Gen2](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-datalake-gen2.html#access-an-adls-account-directly-with-oauth-2-0-using-the-service-principal)|
|   |   |AD Passthrough|**User has correct RBAC role assigned OR ACLs permissions to files/folders in ADLS Gen2|[Python](notebooks/directconnect_adpassthrough_py.py), [SQL](notebooks/directconnect_adpassthrough_sql.sql)| [ADLS Gen2](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-datalake-gen2.html#access-adls-automatically-with-your-aad-credentials)|
|**Mount on DBFS**|Databricks Workspace|Storage Key|All rights|[Python](notebooks/mount_storagekey_py.py)|[Blob](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-storage.html#mount-azure-blob-storage-containers-with-dbfs), [ADLS Gen2](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-datalake-gen2.html#access-an-adls-account-directly-using-the-storage-account-access-key)|
|   |   |OAuth via Service Principal (SP)|**SP has correct RBAC role assigned OR ACLs permissions to files/folders in ADLS Gen2|[Python](notebooks/mount_oauthsp_py.py)| [ADLS Gen2](https://docs.azuredatabricks.net/spark/latest/data-sources/azure/azure-datalake-gen2.html#mount-an-adls-filesystem-to-dbfs-using-a-service-principal-and-oauth-2-0)|
|---|---|---|---|---|---|


**This will depend on where Spark Configuration is set. This is typically set on the SparkSession of the running notebook and therefore scoped to only that SparkSession.*

****IMPORTANT NOTE on Authorization requirements** 

You need to assign specifically either of the following RBAC roles to the Service Principal or User. See [here](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-rbac-portal) for more information. 
- Storage Blob Data Owner
- Storage Blob Data Contributor
- Storage Blob Data Reader

*NOTE:* Owner/Contributor role is insufficient.

For more granular access control, you can use use [ACLs](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-access-control#access-control-lists-on-files-and-directories) on folders/files in the ADLS Gen2 Filesystem.

## Azure Databricks Secrets
All examples do not make sure of [Azure Databricks secrets](https://docs.azuredatabricks.net/user-guide/secrets/index.html) for simplicity. 

Azure Databricks Secrets is the recommended way to store sensitive information in Azure Databricks. Essentially, you create Secret Scopes where you can store secrets in. Permissions are managed at the Secret Scope level. Users with the correct permission to a particular scope can retrieve secrets within it.

There are two types of Secret Scopes:
- [Databricks-backed Secret Scopes](https://docs.azuredatabricks.net/user-guide/secrets/secret-scopes.html#create-a-databricks-backed-secret-scope)
- [KeyVault-backed Azure Databricks Secret Scope - PREVIEW](https://docs.azuredatabricks.net/user-guide/secrets/secret-scopes.html#create-an-azure-key-vault-backed-secret-scope)