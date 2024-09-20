import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
import json
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
import requests

# Carregar variáveis de ambiente
load_dotenv()

# Configurações MQTT
MQTT_BROKER = os.getenv('MQTT_BROKER', 'localhost') #Segurança de Dados Sensíveis: O .env é o local ideal para armazenar dados
MQTT_PORT = int(os.getenv('MQTT_PORT', 1883))
MQTT_TOPIC = os.getenv('MQTT_TOPIC', 'secadora/temperatura')
MQTT_ALERT_TOPIC = os.getenv('MQTT_ALERT_TOPIC', 'secadora/alerta')

# Configurações Firebase
FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH') #Segurança de Dados Sensíveis: O .env é o local ideal para armazenar dados

if not FIREBASE_CREDENTIALS_PATH:
    raise ValueError(
        "A variável de ambiente FIREBASE_CREDENTIALS_PATH não está definida")

# Configurações do Telegram
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN') #Segurança de Dados Sensíveis: O .env é o local ideal para armazenar dados
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': text}
    response = requests.post(url, data=data)
    return response.json()


# Inicializar Firebase
try:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("Conexão com Firebase estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao inicializar o Firebase: {e}")
    raise

# Função de callback quando uma mensagem é recebida


def on_message(client, userdata, message):
    try:
        # Decodificar a mensagem JSON
        payload = json.loads(message.payload.decode())
        temperatura = payload['temperatura']
        timestamp = payload['timestamp']

        # Converter o timestamp para um objeto datetime
        data_hora = datetime.fromisoformat(timestamp)

        # Formatando data e hora para a mensagem
        data_formatada = data_hora.strftime('%d/%m/%Y')
        hora_formatada = data_hora.strftime('%H:%M:%S')

        # Processar os dados recebidos
        print(f"Temperatura recebida: {temperatura}°C em {data_hora}")

        # Verificar se a temperatura está dentro dos limites
        if temperatura > 94:
            message = (f'ALERTA: Temperatura muito alta! {temperatura}°C pode queimar a roupa '
                       f'e danificar o equipamento. Data {data_formatada} Hora {hora_formatada}.')
            send_telegram_message(message)
            print("Notificação enviada via Telegram!")

        # Armazenar os dados no Firebase
        doc_ref = db.collection('temperaturas').document()
        doc_ref.set({
            'temperatura': temperatura,
            'timestamp': data_hora,
            'alerta': 'alto' if temperatura > 94 else 'normal'
        })
        print("Dados armazenados no Firebase com sucesso!")
    except json.JSONDecodeError:
        print("Erro ao decodificar a mensagem JSON")
    except KeyError:
        print("Formato de mensagem inválido")
    except Exception as e:
        print(f"Erro ao processar a mensagem: {e}")

# Função de callback quando conectado ao broker


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Conectado com sucesso ao broker MQTT: {MQTT_BROKER}")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Falha na conexão. Código de resultado: {rc}")

# Função de callback para reconectar ao broker MQTT em caso de desconexão


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"Desconectado do broker MQTT. Código de erro: {
              rc}. Tentando reconectar...")
        client.reconnect()


# Configurar cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Conectar ao broker
try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"Erro ao conectar ao broker MQTT: {e}")
    raise

# Iniciar o loop para processar mensagens
print(f"Iniciando o receptor MQTT. Aguardando mensagens no tópico {
      MQTT_TOPIC}...")
client.loop_forever()
