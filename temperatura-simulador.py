import random
import time
import json
import paho.mqtt.client as mqtt
from datetime import datetime

# Configurações MQTT
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "secadora/temperatura"

# Função para simular a temperatura


def simular_temperatura():
    return round(random.uniform(60, 110), 2)

# Callback quando conectado ao broker MQTT


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado com sucesso ao broker MQTT!")
    else:
        print(f"Falha na conexão. Código de resultado: {rc}")


# Configurar cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Iniciar loop MQTT em segundo plano
client.loop_start()

# Loop principal
try:
    while True:
        temperatura = simular_temperatura()
        timestamp = datetime.now().isoformat()
        # Construir a mensagem como JSON
        mensagem = json.dumps(
            {'temperatura': temperatura, 'timestamp': timestamp})

        # Publicar no tópico MQTT
        result = client.publish(MQTT_TOPIC, mensagem)

        # Verificar se a publicação foi bem-sucedida
        status = result.rc
        if status == 0:
            print(f"Temperatura publicada com sucesso: {temperatura}°C")
        else:
            print(f"Falha ao publicar mensagem. Código de erro: {status}")

        time.sleep(50)  # Espera 50 segundos antes da próxima leitura

except KeyboardInterrupt:
    print("Simulação interrompida pelo usuário")
    client.loop_stop()
    client.disconnect()
