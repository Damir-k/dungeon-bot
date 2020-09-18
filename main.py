import discord
from discord.ext import commands
import config
import random

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print('Logged in!')

@client.command()
async def wow(ctx):
    await ctx.send(":clown:, что сказать")

@client.command()
async def ping(ctx):
    await ctx.send(f"bot ping: {round(client.latency * 1000)}ms")

@client.command()
async def coinflip(ctx):
    result = random.choice(["Решка", "Орел"])
    await ctx.send(result)

client.run(config.TOKEN)
