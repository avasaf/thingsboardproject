import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("v1/devices/me/telemetry")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def send_data(data):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    client.loop_start()
    client.publish("v1/devices/me/telemetry", data)
