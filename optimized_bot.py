import os
import config
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

def is_developer(ctx):
    return ctx.author.id in config.DEVELOPERS

@client.command()
@commands.check(is_developer)
async def load(ctx, extention):
    client.load_extension(f"cogs.{extention}")
    await ctx.send(f"Модуль {extention} успешно загружен")

@client.command()
@commands.check(is_developer)
async def unload(ctx, extention):
    client.unload_extension(f"cogs.{extention}")
    await ctx.send(f"Модуль {extention} успешно остановлен")

@client.command()
@commands.check(is_developer)
async def reload(ctx, extention):
    client.unload_extension(f"cogs.{extention}")
    client.load_extension(f"cogs.{extention}")
    await ctx.send(f"Модуль {extention} успешно перезагружен")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(config.TOKEN)