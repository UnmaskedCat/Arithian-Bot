import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='^help'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '^ip':
        await client.send_message(message.channel,'158.69.238.91:27015 Come Join Us!')
    if message.content == '^workshop':
        await client.send_message(message.channel,'https://steamcommunity.com/sharedfiles/filedetails/?id=1448042260 Addons That Is Used On The Server!')
    if message.content == '^forums':
        await client.send_message(message.channel,'https://arithiansnetworks.mistforums.com/ Come Check Out Our Forums!')
    if message.content == '^donate':
        await client.send_message(message.channel,'https://arithiansnetworks.mistforums.com/donate Donate To The Server!')
    if message.content.startswith('^8ball'):
        randomlist = ["Hell Yeah","Yes in Fade Time","Hell to the no","Never ever ever","Only Nick Bosa"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '^apply':
        await client.send_message(message.channel,'https://arithiansnetworks.mistforums.com/category/staff-application-403464 Apply For Staff!')
    if message.content == '^overview':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=DMUeHumwd1s&t=1s')
    if message.content == '^help':
        await client.send_message(message.channel,'^ip | ^vote | ^forums | ^workshop | ^apply | ^donate | ^overview | ^8ball')
    if message.content == '^vote':
        await client.send_message(message.channel,'https://www.trackyserver.com/server/vikings-star-wars-rp-grand-opening-fastdl-need-commanders-free-61676 and https://topg.org/gmod-servers/in-502356 Get Out Server Populated!')
client.run('NTE0NDczMzA4ODU5NzkzNDA5.DtsKPg.He72xVFk6W5npzvAe2Vnyq0T77Y')
