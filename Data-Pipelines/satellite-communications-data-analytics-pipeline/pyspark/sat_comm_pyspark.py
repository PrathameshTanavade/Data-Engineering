import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI=os.environ["MONGODB_URI"]
MONGODB_DATABASE=os.environ["MONGODB_DATABASE"]
MONGODB_RAW_COLLECTION=os.environ["MONGODB_RAW_COLLECTION"]
MONGODB_PROCESSED_COLLECTION=os.environ["MONGODB_PROCESSED_COLLECTION"]

from pyspark.sql import SparkSession
from pyspark.sql.functions import *






def sat_comm(spark: SparkSession) -> None:

    data=spark\
        .read\
        .format("mongodb")\
        .option("connection.uri",MONGODB_URI)\
        .option("database",MONGODB_DATABASE)\
        .option("collection",MONGODB_RAW_COLLECTION)\
    	.option("spark.mongodb.change.stream.publish.full.document.only", "true")\
        .load()\
        .select('*').where("remoteId like 'C%'")\
        .write\
        .format("mongodb")\
        .option("checkpointlocation","checkpoints")\
        .option("connection.uri", MONGODB_URI)\
        .option("database",MONGODB_DATABASE)\
        .option("collection",MONGODB_PROCESSED_COLLECTION)\
        .mode("append")\
        .save()


if __name__ == "__main__":
    spark=SparkSession.builder\
            .appName("Satellite Communication Data Pipeline")\
            .config("spark.jars.packages","org.mongodb.spark:mongo-spark-connector:10.0.5")\
            .getOrCreate()

    sat_comm(spark)


    spark.stop()


