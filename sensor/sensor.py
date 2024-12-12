import paho.mqtt.client as mqtt
import time
import random
import socket

# MQTT settings
MQTT_BROKER = "host.docker.internal"
MQTT_PORT = 1883
MQTT_TOPIC = "moisture"

def on_connect(client, userdata, flags):
    print(f"Connected with result code:")

def on_disconnect(client, userdata):
    print(f"Disconnected with result code:")

def main():
    # Try to resolve the hostname first
    try:
        host_ip = socket.gethostbyname(MQTT_BROKER)
        print(f"Resolved {MQTT_BROKER} to {host_ip}")
    except socket.gaierror as e:
        print(f"Could not resolve {MQTT_BROKER}: {e}")
        return

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    
    print(f"Trying to connect to broker at {MQTT_BROKER} ({host_ip})...")
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        print("Connected!")

        while True:
            moisture = random.uniform(20.0, 25.0)
            print(f"Publishing: {moisture}")
            client.publish(MQTT_TOPIC, moisture)
            time.sleep(5)
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    main()