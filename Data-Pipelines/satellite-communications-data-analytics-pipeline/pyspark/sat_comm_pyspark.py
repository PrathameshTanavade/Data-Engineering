import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI=os.environ["MONGODB_URI"]
MONGODB_DATABASE=os.environ["MONGODB_DATABASE"]
MONGODB_COLLECTION=os.environ["MONGODB_COLLECTION"]

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, IntergerType, StringType
from pyspark.sql.functions import *



spark=SparkSession.builder\
        .appName("Satellite Communication Data Pipeline")\
        .config("spark.jars.packages","org.mongodb.spark:mongo-spark-connector:10.0.5,org.postgresql:postgresql:42.6.0")\
        .getOrCreate()

lines=spark\
        .readStream\
        .format







dataStreamWriter=transformation.writeStream\
        .format("mongodb")\
        .option("checkpointlocation","/tmp/pyspark")\
        .option("forceDeleteTempCheckpointLocation","true")\
        .option("connection.uri", MONGODB_URI)\
        .option("database",MONGODB_DATABASE)\
        .option("collection",MONGODB_PROCESSED_COLLECTION)\
        .trigger(continuous="20 second")\
        .outputMode("append")\
        .start()

dataStreamWriter.awaitTermination()

