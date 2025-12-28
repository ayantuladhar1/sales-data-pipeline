from pyspark.sql import SparkSession
from constants import BRONZE_PATH

spark = SparkSession.builder \
    .appName("Bronze Ingestion") \
    .enableHiveSupport() \
    .getOrCreate()

df = spark.read.option("header", True).csv("data/raw/sales.csv")

df.write.mode("overwrite") \
    .format("parquet") \
    .save(BRONZE_PATH)