import os
import config
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

def is_developer(ctx):

    DEVELOPERS = [
        433668397599948810, #  HRODGRIM
        357079203235233792  #  Eugene
    ]

    return ctx.author.id in DEVELOPERS

@client.command()
@commands.check(is_developer)
async def load(self, ctx, extention):
    self.client.load_extension(f"cogs.{extention}")
    await ctx.send(f"Модуль {extention} успешно загружен")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(config.TOKEN)