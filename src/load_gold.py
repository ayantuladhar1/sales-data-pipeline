from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
from constants import SILVER_PATH, GOLD_PATH

spark = SparkSession.builder.enableHiveSupport().getOrCreate()

df = spark.read.parquet(SILVER_PATH)

agg_df = df.groupBy("product_name") \
           .agg(sum("price").alias("total_revenue"))

agg_df.write.mode("overwrite") \
    .format("parquet") \
    .save(GOLD_PATH)