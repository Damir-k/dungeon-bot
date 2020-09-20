import os
import config
import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix=">")

#
#  tasks initialization
#
@client.event
async def on_ready():
    update_online.start()
    print("started")

@tasks.loop(seconds=60)
async def update_online():
    online = 0
    for member in client.get_guild(489852374433923074).members:
        if member.status == discord.Status.online:
            online += 1
    
    await client.get_channel(756876293676728360).edit(name="Онлайн 🪐: " + str(online))

#
# load Cogs
#
def is_developer(ctx):
    DEVELOPERS = [
        433668397599948810, #  HRODGRIM
        357079203235233792  #  Eugene
    ]
    return ctx.author.id in DEVELOPERS

@client.command()
@commands.check(is_developer)
async def load(ctx, extention):
    client.load_extension(f"cogs.{extention}")
    await ctx.send(f"Модуль {extention} успешно загружен")

@load.error
async def load_err(ctx, err):
    if isinstance(err, commands.CheckFailure):
        print("load:", ctx.author, "попытался исполнить команду")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")




client.run(config.TOKEN)