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

@client.command()
@commands.check(is_developer)
async def unload(ctx, extention):
    client.load_extension(f"cogs.{extention}")

@client.command()
@commands.check(is_developer)
async def reload(ctx, extention):
    client.load_extension(f"cogs.{extention}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(config.TOKEN)