import requests
import random
import string
import time
from urllib.parse import urljoin

webhook_url = 'https://discord.com/api/webhooks/1210349485172199424/MGml5bHCoM3exBNgT3-_9DOTPkQ6wOeqSYIXaQn3vgEIvPD9cK65SGkd-JcdDh78-8VI'

def generate_proxy():
    username_characters = string.ascii_lowercase + string.digits
    username = ''.join(random.choices(username_characters, k=10))
    port = random.randint(10000, 65535)
    protocol = random.choice(['http', 'https'])
    return f'{protocol}://{username}:{port}'

def send_proxy_to_webhook(proxy):
    webhook_data = {
        'content': f'New Proxy: {proxy}'
    }
    response = requests.post(webhook_url, json=webhook_data, timeout=5)
    if response.status_code == 204:
        print('Sent proxy to webhook by hassen!')
    else:
        print('Failed to send proxy to webhook.')

while True:
    proxy = generate_proxy()
    send_proxy_to_webhook(proxy)
    time.sleep(1)