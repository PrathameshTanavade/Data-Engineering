import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI=os.environ["MONGODB_URI"]
MONGODB_DATABASE=os.environ["MONGODB_DATABASE"]
MONGODB_COLLECTION=os.environ["MONGODB_COLLECTION"]



import datetime
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse
import motor.motor_asyncio




app=FastAPI()
client=motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URI"])
db=client['trending_twitter_hashtag']



async def get_city_table(city):

    timestamp_cursor = db['trending_hashtags'].find({'city':city },{'window.end':1, "_id":0}).sort('window.end',-1).limit(1)
    async for document in timestamp_cursor:
        timestamp=document

    trending_hashtag=[]
    cursor =  db['trending_hashtags'].find({ 'window.end': timestamp['window']['end'] , "city":city},{"_id":0,"hashtag":1,"count":1}).sort('count',-1)


    async for document in cursor:
        trending_hashtag.append(document)

    return trending_hashtag
    
    
    

@app.get("/city/")
async def city(city:str):
    response= await get_city_table(city)
    return response
    




