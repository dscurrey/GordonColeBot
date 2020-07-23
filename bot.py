import os
import discord
from dotenv import load_dotenv
import quotegenerator
import logging

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='gordon.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    logger.info(f'{client.user} Connected.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "gordon" in message.content.lower():
        response = quotegenerator.gc_quote()
        await message.channel.send(response)
        logger.info('[{}]\tSending Quote...'.format(message.author))

@client.event
async def on_error(event, *args, **kwargs):
    logger.error(f'Error Occured: {args[0]}\n')

client.run(TOKEN)
