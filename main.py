import asyncio
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

class Time(BaseModel):
    need: bool

app = FastAPI()
counter_lock = asyncio.Lock()
counter = 0

@app.post("/time/")
async def create_time(time:Time):
    global counter
    async with counter_lock:
        counter += 1
    time_dict = time.dict()
    now = datetime.now() 
    if time.need == True:
        date_date_str = now.strftime("%Y-%m-%d")
        time_dict.update({"time_stamp": date_date_str})
    else:
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        time_dict.update({"time_stamp": date_time_str})

    return time_dict

@app.get("/time/")
async def create_counter():
    global counter
    async with counter_lock:
        counter += 1
    return {"Cantidad de Hits": counter}