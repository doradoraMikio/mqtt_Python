import paho.mqtt.client as paho
import ssl
import json
from time import sleep
from .module_monitor import ProcessUtilities

"""
MQTTでAWS IoTにﾒｯｾｰｼﾞを送信
"""


class MqttPub:

    # Setting topic during initialization
    def __init__(self, host, port, topic= "default"):
        self.topic = topic
        self.mqtt = paho.Client()
        self.host = host
        self.port = port
        ca_certs = "../resource/root-CA.crt"
        certfile = "../resource/88c9f704be-certificate.pem.crt"
        keyfile = "../resource/88c9f704be-private.pem.key"

        self.mqtt.tls_set(ca_certs=ca_certs,certfile=certfile,keyfile=keyfile,tls_version=ssl.PROTOCOL_TLSv1_2)
        self.mqtt.connect(self.host,self.port, keepalive=60)

    def start(self):
        self.mqtt.loop_start()
        while True:
            sleep(10)
            self.mqtt.publish(self.topic, payload=json.dumps(ProcessUtilities.get_computer_performance()))





