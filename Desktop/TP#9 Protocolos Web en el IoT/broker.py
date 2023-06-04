import paho.mqtt.client as mqtt

# Callback para cuando se recibe un mensaje
def on_message(client, userdata, message):
    print("Mensaje recibido:", message.payload.decode())

# Configurar el cliente MQTT
client = mqtt.Client()
client.on_message = on_message

# Conectarse al broker
client.connect("localhost", 1883)

# Suscribirse a un tema
client.subscribe("mi_tema")

# Publicar mensajes en el tema
client.publish("mi_tema", "Hola, esto es un mensaje MQTT")

# Mantener el cliente en ejecución
client.loop_forever()
