import os
import discord

TOKEN = input("Insert Bot Token here: ")

client = discord.Client()

@client.event
async def on_ready():
    print(client.user, "Has connected!")


client.run(TOKEN)