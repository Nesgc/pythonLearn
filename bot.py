import os
import discord
from dotenv import load_dotenv
import requests
import random

# Carga las variables de entorno desde tu archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()  # Habilita solo los intents por defecto
intents.messages = True  # Asegúrate de que tu bot pueda escuchar y enviar mensajes

# Crea una instancia del cliente de Discord con los intents especificados
client = discord.Client(intents=intents)

# Evento que se dispara cuando el bot ha terminado de conectarse a Discord
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discords!')

# Evento que se dispara cada vez que se recibe un mensaje en un canal al que el bot tiene acceso
@client.event
async def on_message(message):
    # Ignora los mensajes enviados por el bot para evitar bucles de mensajes
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    # Responde a un comando específico con una cita aleatoria
    if message.content == '9':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    # Responde a mensajes que contienen "happy birthday"
    elif 'ha' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

    # Responde al comando !charinfo con información del personaje de Tibia
    elif message.content.startswith('!charinfo'):
        name = message.content[len('!charinfo '):].strip()
        response = requests.get(f'https://api.tibiadata.com/v4/characters/{name}.json')
        data = response.json()

        if 'error' not in data['characters']:
            char_info = data['characters']['data']
            reply = f"Nombre: {char_info['name']}\nNivel: {char_info['level']}\nVocación: {char_info['vocation']}"
        else:
            reply = f"Error: {data['characters']['error']}"

        await message.channel.send(reply)

# Ejecuta el bot con el token proporcionado
client.run(TOKEN)
