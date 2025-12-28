CREATE DATABASE IF NOT EXISTS sales_db;
USE sales_db;

CREATE EXTERNAL TABLE bronze_sales
STORED AS PARQUET
LOCATION '/warehouse/tablespace/managed/hive/bronze_sales';

CREATE EXTERNAL TABLE silver_sales
STORED AS PARQUET
LOCATION '/warehouse/tablespace/managed/hive/silver_sales';

CREATE EXTERNAL TABLE fact_sales
STORED AS PARQUET
LOCATION '/warehouse/tablespace/managed/hive/fact_sales';