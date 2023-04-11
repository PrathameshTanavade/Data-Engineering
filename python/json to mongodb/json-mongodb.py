import os
import sys
import datetime
from dotenv import load_dotenv

from pymongo import MongoClient


import pandas as pd


# Connecting to Database--------------
load_dotenv()
MONGODB_URI=os.environ["MONGODB_URI"]
client=MongoClient(MONGODB_URI)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client.PORTFOLIO_PROJECTS
account_collection=db["python-json to mongodb"]
# --------------------------------------


# Extracting and transforming  data from json files-----------

filename=sys.argv[1]
df=pd.read_json(filename,lines=True)
df['price']=df['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
df.rename(columns={'neighbourhood_cleansed':'neighbourhood'},inplace=True)

data=df.to_dict('records')
# --------------------------------------------------------


#Loading data onto MongoDB Database---------------------------
result=account_collection.insert_many(data)
document_id=result.inserted_ids
print("# of documents inserted: " + str(len(document_id)))
#---------------------------------------------------------------

client.close()

