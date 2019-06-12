-- Databricks notebook source
-- MAGIC %md
-- MAGIC ## Azure DataLake Gen2

-- COMMAND ----------

SET fs.azure.account.key.<STORAGE_ACCOUNT>.dfs.core.windows.net=<STORAGE_KEY>

-- COMMAND ----------

-- Create a table over a CSV file in ADLS Gen2
-- You'll need data.csv at root of container/filesystem
CREATE TABLE MyTable
USING CSV
OPTIONS ('header'='true')
LOCATION 'abfss://<STORAGE_CONTAINER>@<STORAGE_ACCOUNT>.dfs.core.windows.net/data.csv';

-- COMMAND ----------

SELECT * FROM MyTable;