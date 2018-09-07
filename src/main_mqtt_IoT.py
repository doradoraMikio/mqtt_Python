from mqttInfosys.mqttPub import MqttPub

if __name__ == "__main__":
    mqttPub = MqttPub("a31ggkp9l4qa0h.iot.ap-northeast-1.amazonaws.com", 8883)
    mqttPub.start()


