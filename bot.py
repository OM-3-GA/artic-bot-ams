import discord
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import os
import youtube_dl
import shutil
from os import system

#Variables
client = commands.Bot(command_prefix="!", status=discord.Status.idle, activity=discord.Game(name="ArticBOT | Starting..."))
token = 'NjI3NjM1MjczMjgyNDg2Mjky.XZEAQw.W-rRWEUZsw9KWGlh2cbnXYt1-9M'

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name="ArticBOT | !help"))
    print('Bot Started.')

@client.command(aliases=['load'])
@commands.has_permissions(administrator=True)
async def Load(ctx, extension):
    client.load_extension(f"{extension}")
    await ctx.channel.purge(limit=1)

@client.command(aliases=['unload'])
@commands.has_permissions(administrator=True)
async def Unload(ctx, extension):
    client.unload_extension(f"{extension}")
    await ctx.channel.purge(limit=1)

@client.command(aliases=['reload'])
@commands.has_permissions(administrator=True)
async def Reload(ctx, extension):
    client.unload_extension(f"{extension}")
    client.load_extension(f"{extension}")
    await ctx.channel.purge(limit=1)
    print(f'Reloaded {extension}.')

for filename in os.listdir(''):
    if filename.endswith('.py'):
        client.load_extension(f"{filename[:-3]}")

client.run('secretAccessKey: process.env.TOKEN')
