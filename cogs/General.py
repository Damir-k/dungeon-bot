import datetime
import random
import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wow(self, ctx):
        await ctx.send(":clown:, что сказать")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"пинг бота: {round(self.client.latency * 1000)}ms")

    @commands.command()
    async def coinflip(self, ctx):
        result = random.choice(["Ого! решка", "Вау! орел"])
        await ctx.send(result)

    @commands.command()
    async def age(self, ctx):
        time_joined = ctx.author.joined_at
        current_time = datetime.datetime.now()
        time_passed = current_time - time_joined
        await ctx.send(ctx.author.mention + " на сервере " + str(time_passed.days) + " дней, " + str(time_passed.seconds // 3600) + " часов")

    @commands.command()
    async def members(self, ctx):
        bots = len(ctx.guild.get_role(489877721439010847).members)
        await ctx.send(f"На сервере {ctx.guild.member_count - bots} человек")
    
    #
    #  error handlers
    #
    @age.error
    async def age_err(self, ctx, err):
        if isinstance(err, AttributeError):
            print("age: недопустимо выполнение")
        else:
            print(err)
    
    @members.error
    async def members_err(self, ctx, err):
        if isinstance(err, AttributeError):
            print("members: недопустимо выполнение")
        else:
            print(err)


def setup(client):
    client.add_cog(General(client))