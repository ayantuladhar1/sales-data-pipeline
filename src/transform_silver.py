from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from constants import BRONZE_PATH, SILVER_PATH

spark = SparkSession.builder.enableHiveSupport().getOrCreate()

df = spark.read.parquet(BRONZE_PATH)

clean_df = df.withColumn("quantity", col("quantity").cast("int")) \
             .withColumn("price", col("price").cast("double"))

clean_df.write.mode("overwrite") \
    .format("parquet") \
    .save(SILVER_PATH)