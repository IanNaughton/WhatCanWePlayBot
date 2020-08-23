import os 

import discord
from dotenv import load_dotenv

# load up any environment variables 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
  guild = discord.utils.find(lambda guild: guild.name == GUILD, client.guilds)

  print(
    f'{client.user} has connected to the following guild:\n'
    f'{guild.name} (id: {guild.id})'
  )

client.run(TOKEN)