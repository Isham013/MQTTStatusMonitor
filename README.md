# MQTTStatusMonitor

MQTTStatusMonitor is an application that integrates MQTT, FastAPI, and MongoDB for monitoring and storing MQTT status messages.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- MongoDB (running locally or accessible via URI)
- rabbitMQ

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
 sudo # Server installation: RabbitMQ
To install RabbitMQ, follow the installation guide for your operating system:

Installing RabbitMQ on Linux: https://www.rabbitmq.com/install-debian.html

Installing RabbitMQ on Windows: https://www.rabbitmq.com/install-windows.html

Installing RabbitMQ on macOS: https://www.rabbitmq.com/install-homebrew.html



Configuration
Once we have  installed Celery and RabbitMQ, we will need to configure them for our project.


RabbitMQ

By default, RabbitMQ listens on port 5672. We can use the following command to start RabbitMQ:
``` bash
 sudo systemctl start rabbitmq-server
 sudo systemctl enable rabbitmq-server
 sudo rabbitmq-plugins enable rabbitmq_mqtt