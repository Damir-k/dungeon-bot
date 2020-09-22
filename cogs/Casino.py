import asyncio
import random
import math
import discord
from discord.ext import commands

UNIT = "Ď"

def is_developer(ctx):
    DEVELOPERS = [
        433668397599948810, #  HRODGRIM
        357079203235233792  #  Eugene
    ]
    return ctx.author.id in DEVELOPERS

class Casino(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.accounts = {}
        self.invites = {}
    
    @commands.command(aliases=["bet", "50-50", "challenge"])
    async def coinflip(self, ctx, member:discord.Member, amount):
        if ctx.channel.id == 757288748672221265:
            amount = int(amount)
            if member.id == 756518853072125982 and self.accounts[ctx.author.id] >= amount: #  is it me
                result = random.random()
                if result < 0.001:
                    await ctx.send(f"{ctx.author.mention}Погоди ка... Монета упала на ребро?.. Поздравляю! В честь такого события даю тебе x100 выйгрыш!")
                    self.accounts[ctx.author.id] += amount * 100
                elif result < 0.455:
                    await ctx.send(f"{ctx.author.mention}Ты выйграл {amount}{UNIT}!")
                    self.accounts[ctx.author.id] += amount
                else:
                    await ctx.send(f"{ctx.author.mention}Ты проиграл {amount}{UNIT}!")
                    self.accounts[ctx.author.id] -= amount
            elif self.accounts[member.id] >= amount and self.accounts[ctx.author.id] >= amount:
                random_key = random.randint(1, 10**4)
                await ctx.send(f"{member.mention}, Вас вызывают на дуэль! Ставка: {amount}")
                self.invites[ctx.author.id] = (member.id, random_key, amount)
                await asyncio.sleep(120)
                if self.invites[ctx.author.id] == (member.id, random_key, amount):
                    del self.invites[ctx.author.id]
                    await ctx.send(ctx.author.mention + "Ваше приглашение истекло")
        else:
            await ctx.author.send("Эта команда доступна только в канале #🎰╰╮казино")

    @commands.command()
    async def accept(self, ctx, member:discord.Member):
        if ctx.channel.id == 757288748672221265:
            if member.id in self.invites.keys():
                amount = self.invites[member.id][2]
                if self.invites[member.id][0] == ctx.author.id:
                    del self.invites[member.id]
                    await ctx.send(f"Ставки по {amount}{UNIT} приняты!")
                    await asyncio.sleep(2)
                    if random.random() < 0.5:
                        self.accounts[member.id] += amount
                        self.accounts[ctx.author.id] -= amount
                        await ctx.send(f"{member.mention} Выйграл! Ему достается {amount}{UNIT}")
                    else:
                        self.accounts[member.id] -= amount
                        self.accounts[ctx.author.id] += amount
                        await ctx.send(f"{ctx.author.mention} Выйграл! Ему достается {amount}{UNIT}")
                else:
                    await ctx.author.send("Этот человек отправлял запрос не вам!")
            else:
                await ctx.author.send("Этот человек не отправлял вам запрос в течении последней минуты!")
        else:
            await ctx.author.send("Эта команда доступна только в канале #🎰╰╮казино")

    @commands.command(aliases=["coins", "purse"])
    async def balance(self, ctx):
        if ctx.channel.id == 757288748672221265:
            await ctx.send(f"{ctx.author.mention}, у вас на балансе {self.accounts[ctx.author.id]}{UNIT}")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 757883097881640980 and not payload.member.id in self.accounts.keys():
            await payload.member.add_roles(self.client.get_guild(payload.guild_id).get_role(757899902222204961))
            self.accounts[payload.member.id] = 500
            await payload.member.send("Ваш аккаунт в казино был создан. Стартовый баланс: 500" + UNIT)
    
    #
    #  admin-only
    #
    @commands.command()
    @commands.check(is_developer)
    async def give(self, ctx, member:discord.Member, amount:int):
        self.accounts[member.id] += amount
    
    @commands.command()
    @commands.check(is_developer)
    async def savecasino(self, ctx):
        await ctx.author.send(f"```{self.accounts}```")
    
    @commands.command()
    @commands.check(is_developer)
    async def loadcasino(self, ctx, *, dictionary):
        self.accounts = eval(dictionary)
    
    #
    #  errors
    #
    @coinflip.error
    async def coinflip_error(self, ctx, err):
        if isinstance(err, ZeroDivisionError):
            pass
        else:
            print(err)


def setup(client):
    client.add_cog(Casino(client))

# if ctx.author.id in self.accounts.keys():
#     pass
# else:
#     pass