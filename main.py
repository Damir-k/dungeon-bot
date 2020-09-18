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
    result = random.choice(["Ого! решка", "Вау! орел"])
    await ctx.send(result)

@client.command()
async def clear(ctx, amount=3):
    if type(amount) != int:
        return
    if amount <= 0:
        return

    if ctx.channel.permissions_for(ctx.author).manage_messages == True:
        await ctx.channel.purge(limit=amount+1)

@client.command()
async def helpme(ctx, category=None):
    ctx.send(config.help(category))
    

client.run(config.TOKEN)
