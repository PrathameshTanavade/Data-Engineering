import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI=os.environ["MONGODB_URI"]
MONGODB_DATABASE=os.environ["MONGODB_DATABASE"]
MONGODB_COLLECTION=os.environ["MONGODB_COLLECTION"]


from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark= SparkSession\
        .builder\
        .appName("Trending Twitter Hashtag")\
        .config("spark.jars.packages","org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0,org.mongodb.spark:mongo-spark-connector:10.0.5")\
        .getOrCreate()

schema_major=StructType()\
        .add("created_at",StringType())\
        .add("id_str", IntegerType())\
        .add("text", StringType())\
        .add("user", StringType())\
        .add("entities",StructType()\
                            .add("hashtags",ArrayType(StructType()\
                                                     .add("text",StringType())\
                                                     .add("indices",StringType()))))\
        .add("place", StructType()\
                .add("place_type",StringType())\
                .add("country_code",StringType())\
                .add("country",StringType())\
                .add("name",StringType())
        )

df=spark\
    .readStream\
    .format("kafka")\
    .option("kafka.bootstrap.servers","localhost:9092")\
    .option("subscribe","tweet")\
    .load()\
    .selectExpr("CAST(key AS STRING)","CAST(value AS STRING)")\
    .select("value")\
    .select(from_json(col("value"),schema_major).alias("json"))\
    .select(split("json.created_at"," ").getItem(3).cast("timestamp").alias("created_timestamp"),\
            explode(col("json.entities.hashtags.text")).alias("hashtag"),\
            col("json.place.name").alias("city")
           )\
    .groupby(window(df.created_timestamp, "60 seconds" , "60 seconds"),df.hashtag,df.city).count().orderBy('window')\
    .writeStream\
        .format("mongodb")\
        .option("checkpointlocation","/tmp/pyspark")\
        .option("forceDeleteTempCheckpointLocation","true")\
        .option("connection.uri", MONGODB_URI)\
        .option("database",MONGODB_DATABASE)\
        .option("collection",MONGODB_COLLECTION)\
        .trigger(processingTime="100 seconds")\
        .outputMode("complete")\
        .start()