from fastapi import FastAPI, Query,  HTTPException
from server import get_status_count
from client import publish_message

import datetime
import asyncio


app = FastAPI()

# startup event to run publish message concurrently
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(publish_message())

# Data Retrieval Endpoint
@app.get("/status_count")
async def retriev_status(
    start_time: datetime.datetime = Query(...),
    end_time: datetime.datetime = Query(...)):
    try:
        count = get_status_count(start_time,end_time)
        return count
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    