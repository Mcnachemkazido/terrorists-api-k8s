import uvicorn
from fastapi import FastAPI ,HTTPException
from fastapi import UploadFile
import pandas as pd
from models import Terrorist
from db import insert_to_db

import os
from dotenv import load_dotenv
load_dotenv()
MONGO_HOST=os.getenv("MONGO_HOST")
MONGO_PORT=os.getenv("MONGO_PORT")
MONGO_DB=os.getenv("MONGO_DB")
app = FastAPI()


@app.post("/top-threats")
def top_threats(file: UploadFile):
    df = pd.read_csv(file.file)
    df_sort =df.sort_values(["danger_rate"],ascending=False)
    top_df = df_sort.head(5)
    top_df_dict = top_df.to_dict("records")
    data = []
    data_2 = []
    for t in top_df_dict:
        new_t = Terrorist(name=t["name"],location=t["location"],danger_rate = t["danger_rate"])
        data.append(new_t.model_dump())
        data_2.append(new_t)
    insert_to_db(data)
    return {"count":str(len(data)),"top":data_2}

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)




