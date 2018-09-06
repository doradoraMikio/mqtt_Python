import paho.mqtt.client as mqtt
from time import sleep
from module import moduleMonitor

host = "192.168.56.40"
port = 1883
topic = "mqtt/test"


if __name__ == "__main__":
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.connect(host, port=port, keepalive=60)

    while True:
        publish_message = moduleMonitor.ProcessUtilities.get_computer_performance()
        client.publish(topic, str(publish_message))
        sleep(10)

    client.disconnect()