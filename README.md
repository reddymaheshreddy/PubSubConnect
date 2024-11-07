# MQTT-based PubSubConnect

This project demonstrates a basic **Tweet Publisher** and **Hashtag Follower** system using MQTT for message-passing. It includes two applications:
1. **Tweet Publisher**: Allows users to publish tweets to specific hashtag topics.
2. **Hashtag Follower**: Enables users to subscribe and view tweets from specific hashtags in real-time.

## Features

- **Publish Tweets**: Publish a tweet message along with a username and hashtag as the topic.
- **Subscribe to Hashtags**: Follow specific hashtags to see real-time tweets posted under those topics.
- **Unsubscribe**: Stop following a hashtag at any time.

## MQTT Broker: Mosquitto

This project uses the **Eclipse Mosquitto MQTT broker**, a popular open-source MQTT broker. We connect to the public Mosquitto broker (`test.mosquitto.org`), which allows for easy testing of MQTT publish-subscribe functionality without setting up a server.

- **Broker Address**: `test.mosquitto.org`
- **Protocol**: MQTT (Message Queuing Telemetry Transport)

> **Note**: The public broker `test.mosquitto.org` is shared among users globally, so you may occasionally see unrelated messages. For production use, it’s recommended to set up a private Mosquitto server.

## Prerequisites

Ensure you have Python 3.6+ installed on your system. You’ll need the dependencies listed in `requirements.txt`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mqtt-tweet-system.git
   cd mqtt-tweet-system
