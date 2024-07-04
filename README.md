# MQTTStatusMonitor

MQTTStatusMonitor is an application that integrates MQTT, FastAPI, and MongoDB for monitoring and storing MQTT status messages.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- MongoDB (running locally or accessible via URI)
- RabbitMQ

## Setup

# Installation: RabbitMQ
To install RabbitMQ, follow the installation guide for your operating system:

Installing RabbitMQ on Linux: https://www.rabbitmq.com/install-debian.html

Installing RabbitMQ on Windows: https://www.rabbitmq.com/install-windows.html

Installing RabbitMQ on macOS: https://www.rabbitmq.com/install-homebrew.html



Configuration
Once we have  installed RabbitMQ, we will need to configure them for our project.


RabbitMQ

By default, RabbitMQ listens on port 5672. We can use the following command to start RabbitMQ:
``` bash
 sudo systemctl start rabbitmq-server
 sudo systemctl enable rabbitmq-server
 sudo rabbitmq-plugins enable rabbitmq_mqtt
```
# Install dependencies:
After cloning the repository.Create and activate a virtual environment (optional but recommended):
``` bash
python -m venv venv
source venv/bin/activate
```
 - Install dependencies:
 ``` bash
cd app
pip install -r requirements.txt
 ```
 - Environment Variables:
   Create a .env file in the root directory with the following content:
   ``` bash
  URL="your_mongodb_url_here"
   ``` 
 - Running the Application:
    Start the FastAPI application:
   ``` bash
    uvicorn main:app --reload
    ```
 - Accessing Endpoints:
  Status Count Endpoint: Open your browser and navigate to http://localhost:8000/status_count to retrieve status counts between specified start and end times.

# Usage
 -Publishing MQTT Messages: Modify client.py to publish MQTT messages to your broker. Ensure your MQTT broker details (broker_address, broker_port, topic) match your setup.
 -Monitoring: Monitor published MQTT messages in MongoDB using the FastAPI endpoint.

