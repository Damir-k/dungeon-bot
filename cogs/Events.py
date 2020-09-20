import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready to go")

    @commands.Cog.listener()
    async def on_member_joined(self, member):
        await self.client.get_channel(756875879623426068).edit(name="Участников 🌏: " + str(self.client.get_guild(489852374433923074).member_count))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.client.get_channel(756875879623426068).edit(name="Участников 🌏: " + str(self.client.get_guild(489852374433923074).member_count))

def setup(client):
    client.add_cog(Events(client))