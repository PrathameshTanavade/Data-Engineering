import os
import glob
from dotenv import load_dotenv
import pandas as pd

from pymongo import MongoClient
from pymongo.server_api import ServerApi


# Connecting to Database --------------------------
load_dotenv()
MONGODB_URI=os.environ['MONGODB_URI']
client=MongoClient(MONGODB_URI)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client.PORTFOLIO_PROJECTS
account_collection=db["python- csv to mongodb"]
# --------------------------------------------------------------

# Extracting Data---------------------------

# Defining csv file extraction
def extract_listing_csv(filename):
    df_listing_01=pd.read_csv(filename,quotechar='"',parse_dates=['last_scraped','host_since','calendar_updated','first_review','last_review'])
    return df_listing_01

def extract_review_csv(filename):
    df_reviews_01=pd.read_csv(filename, quotechar='"', parse_dates=['date'])
    return df_reviews_01

df_listings=pd.DataFrame()
df_reviews=pd.DataFrame()


for listingfile in glob.glob("data/listings/*/*.csv"):
    df=extract_listing_csv(listingfile)
    df_listings=pd.concat([df_listings,df],ignore_index=True)

for reviewfile in glob.glob("data/reviews/*/*.csv"):
    df=extract_review_csv(reviewfile)
    df_reviews=pd.concat([df_reviews,extract_review_csv(reviewfile)],ignore_index=True)
#-------------------------------------------------------------------------


# Transfroming data--- Cleaning 'price' column -->  Merging dataframes --> Renaming Columns --> Droping Columns

data=df_listings.merge(df_reviews , left_on='id', right_on='listing_id')
data.rename(columns={'id_x':'id', 'id_y':'review_id'},inplace=True)
data.drop(columns='listing_id',inplace=True)
data['price']=data['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

column_list=['last_scraped','host_since','calendar_updated','first_review','last_review','date']
for x in column_list:
    data[x]=data[x].fillna("0000-00-00")

data=data.head(10000)
data_dict=data.to_dict('records')


# --------------------------------------------------------------------------


# Loading data onto MongoDB ------------------------------------------------
try:
    result=account_collection.insert_many(data_dict)
    document_id=result.inserted_ids
    print("# of documents inserted:" + str(len(document_id)))

except Exception as e:
    print(e)
# ---------------------------------------------------------------------------

client.close()
