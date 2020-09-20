import discord
from discord.ext import commands

DEVELOPERS = [
    433668397599948810, #  HRODGRIM
    357079203235233792  #  Eugene
]

class DevOnly(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @staticmethod
    def is_developer(ctx):
        return ctx.author.id in DEVELOPERS

    @commands.command()
    @commands.check(is_developer)
    async def load(self, ctx, extention):
        self.client.load_extension(f"cogs.{extention}")
        await ctx.send(f"Модуль {extention} успешно загружен")

    @commands.command()
    @commands.check(is_developer)
    async def unload(self, ctx, extention):
        self.client.unload_extension(f"cogs.{extention}")
        await ctx.send(f"Модуль {extention} успешно остановлен")

    @commands.command()
    @commands.check(is_developer)
    async def reload(self, ctx, extention):
        self.client.unload_extension(f"cogs.{extention}")
        self.client.load_extension(f"cogs.{extention}")
        await ctx.send(f"Модуль {extention} успешно перезагружен")

def setup(client):
    client.add_cog(DevOnly(client))