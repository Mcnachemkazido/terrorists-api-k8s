import os
from dotenv import load_dotenv
import pymongo
load_dotenv()


MONGO_HOST=os.getenv("MONGO_HOST")
MONGO_PORT=os.getenv("MONGO_PORT")
MONGO_DB=os.getenv("MONGO_DB")




def insert_to_db(data):
    client = pymongo.MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
    mydb = client[MONGO_DB]
    col = mydb["top_threats"]
    col.insert_many(data)




