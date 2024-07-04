import paho.mqtt.client as mqtt
from server import store_data
from config import broker_address, broker_port, topic

import json
import random
import asyncio

# MQTT Client Setup
mqtt_client = mqtt.Client()

def on_publish(client, userdata, mid):
  print("Message published")

def on_connect(client, rc):
  if rc == 0:
    print("Connected to MQTT Broker!")
    client.subscribe(topic)
  else:
    print("Failed to connect, return code", rc)

# assigning callback functions to the Client
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish

# Connecting to the Broker
mqtt_client.connect(broker_address, broker_port)


async def publish_message():
  while True:
    status_value = random.randint(0, 6)
    message = json.dumps({"status": status_value})

    # Publish to MQTT broker
    mqtt_client.publish(topic, message)
    print(f"Published MQTT message: {message}")

    # the function to save the message to MongoDB
    await save_to_mongodb(message)

    await asyncio.sleep(1)


async def save_to_mongodb(message):
  # Call the store_data function with the message
  await store_data(message)


# asyncio.run(publish_message())
