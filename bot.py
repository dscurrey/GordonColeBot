import os
import discord
from dotenv import load_dotenv
import quotegenerator

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} is connected.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    gordonQuotes = [
        'TAKE ANOTHER LOOK SONNY, IT\'S GONNA HAPPEN AGAIN',
        'YOU ARE WITNESSING A FRONT THREE QUARTER VIEW OF TWO ADULTS SHARING A TENDER MOMENT',
        'YOU REMIND ME TODAY OF A SMALL MEXICAN CHIHUAHUA'
    ]

    if "gordon" in message.content.lower():
        response = quotegenerator.gc_quote()
        await message.channel.send(response)

client.run(TOKEN)
