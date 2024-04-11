import discord
import requests
import json
import os

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        elif message.content.startswith('$semen'):
            # Obtener la ruta completa del archivo de video
            video_file_path = os.path.join(os.path.dirname(__file__), 'Memillos', 'Ya no me sale c3m3n meme HD.mp4')
            with open(video_file_path, 'rb') as file:
                video = discord.File(file)
            await message.channel.send(file=video)
        elif message.content.startswith('$hello'):
            # Obtener la ruta completa del archivo de imagen
            image_file_path = os.path.join(os.path.dirname(__file__), 'Memillos', 'Hello.jpg')
            with open(image_file_path, 'rb') as file:
                image = discord.File(file)
            await message.channel.send(file=image)



intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run('MTIyMDY4Mjk0MzUyMTg4NjI4OQ.Gha4YP.zI-1LhVY2oufO1QwiiZcZovtgIaIzhW_oRWL1A')  
  
 


