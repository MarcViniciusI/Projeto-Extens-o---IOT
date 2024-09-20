import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')#Segurança de Dados Sensíveis: O .env é o local ideal para armazenar dados
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': text}
    response = requests.post(url, data=data)
    return response.json()
