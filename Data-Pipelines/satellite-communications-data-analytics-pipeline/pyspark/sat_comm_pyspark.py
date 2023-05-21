import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI=os.environ["MONGODB_URI"]
MONGODB_DATABASE=os.environ["MONGODB_DATABASE"]
MONGODB_COLLECTION=os.environ["MONGODB_COLLECTION"]

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, IntergerType, StringType, TimestampType
from pyspark.sql.functions import *



spark=SparkSession.builder\
        .appName("Satellite Communication Data Pipeline")\
        .config("spark.jars.packages","org.mongodb.spark:mongo-spark-connector:10.0.5")\
        .getOrCreate()

schema= StructType()\
        .add("datetime", TimestampType())\
        .add("remoteId", StringType())\
        .add("beamId", IntegerType())\
        .add("beamName", StringType())\
        .add("satLong", IntegerType())\
        .add("fwdModCodId", StringType())\
        .add("fwdSNR", IntegerType())\
        .add("packetsLost", IntegerType())\
        .add("latitude", IntegerType())\
        .add("longitude", IntegerType())\
        .add("rxFreq", IntegerType())\
        .add("txFreq", IntegerType())\
        .add("fwdBitRate", IntegerType())\
        




lines=spark\
        .readStream\
        .format("mongodb")\
        .option("connection.uri",MONGODB_URI)
        .option("database",MONGODB_DATABASE)
        .option("collection",MONGODB_RAW_COLLECTION)\
        .schema(schema)
        .load()






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

