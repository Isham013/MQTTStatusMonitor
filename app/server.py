from pymongo.mongo_client import MongoClient
from fastapi import Query, HTTPException
from config import MONGO_COLLECTION, MONGO_DATABASE

import datetime
import json
import os

MONGO_URL = os.environ.get("URL")
client = MongoClient(MONGO_URL)
db = client[MONGO_DATABASE]
collection = db[MONGO_COLLECTION]

# storing messages to Mongodb
async def store_data(message):
    try:
        client = MongoClient(MONGO_URL)
        # Accessing thedatabase and collection
        db = client[MONGO_DATABASE]
        collection = db[MONGO_COLLECTION]

        # Parsing the message to extract status
        message_dict = json.loads(message)
        status = message_dict.get("status")

        # document with timestamp as a datetime object
        timestamp = datetime.datetime.now()
        document = {
            "status": status,
            "timestamp": timestamp
        }

        # Inserting the document into the collection
        result = collection.insert_one(document)
        print(f"Document inserted with _id: {result.inserted_id}")

    except Exception as e:
        print(f"An error occurred saving to MongoDB: {e}")

    finally:
        # Close the connection to avoid resource leaks
        client.close()

def get_status_count(
    start_time: datetime.datetime = Query(...),
    end_time: datetime.datetime = Query(...)):

    try:
        print(f"Received start_time: {start_time}, end_time: {end_time}")

        # Validate start and end times
        if not start_time or not end_time:
            raise HTTPException(status_code=400, detail="Missing start_time or end_time parameter")

        # Query for MongoDB collection
        query = {"timestamp": {"$gte": start_time, "$lt": end_time}}
        results = list(collection.find(query))

        # Count status occurrences
        status_counts = {}
        for result in results:
            status = result.get("status")
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1

        print(f"Status counts: {status_counts}")

        return status_counts

    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
