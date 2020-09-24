import asyncio
import humanize
import random
import math
import discord
from discord.ext import commands, tasks

UNIT = "Ď"
_t = humanize.i18n.activate("ru_RU")

def is_developer(ctx):
    DEVELOPERS = [
        433668397599948810, #  HRODGRIM
        357079203235233792  #  Eugene
    ]
    return ctx.author.id in DEVELOPERS

def win_chance(x, a, b):
    x /= a
    return 0.5 * (abs(x+1) + 1) / (x+1) - b


class Casino(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.accounts = {}
        self.invites = {}
        self.win_chance_a = 45
        self.win_chance_b = 0.005
        self.bank = 100000
        self.giveaway1_amount = 200
        self.giveaway1_claim = False
        self.giveaway1_claimed = []
    
    @commands.command(aliases=["ставка", "bet", "50-50", "challenge"])
    async def coinflip(self, ctx, amount:int, member:discord.Member=None):
        if ctx.channel.id == 757288748672221265:
            amount = int(amount)
            if member == None and self.accounts[ctx.author.id] >= amount >= 20: #  is it me
                result = random.random()
                if result < win_chance(self.accounts[ctx.author.id], self.win_chance_a, self.win_chance_b) and amount < self.bank:
                    await ctx.send(f"{ctx.author.mention}Ты выйграл {humanize.intcomma(amount)}{UNIT}!")
                    self.accounts[ctx.author.id] += amount
                    self.bank -= amount
                else:
                    await ctx.send(f"{ctx.author.mention}Ты проиграл {humanize.intcomma(amount)}{UNIT}!")
                    self.accounts[ctx.author.id] -= amount
                    self.bank += amount
            elif self.accounts[member.id] >= amount >= 20 and self.accounts[ctx.author.id] >= amount >= 20:
                random_key = random.randint(1, 10**4)
                await ctx.send(f"{member.mention}, Вас вызывают на дуэль! Ставка: {humanize.intcomma(amount)}")
                self.invites[ctx.author.id] = (member.id, random_key, amount)
                await asyncio.sleep(120)
                if self.invites[ctx.author.id] == (member.id, random_key, amount):
                    del self.invites[ctx.author.id]
                    await ctx.send(ctx.author.mention + "Ваше приглашение истекло")
        else:
            await ctx.author.send("Эта команда доступна только в канале #🎰╰╮казино")

    @commands.command(aliases=["принять", "ok"])
    async def accept(self, ctx, member:discord.Member):
        if ctx.channel.id == 757288748672221265:
            if member.id in self.invites.keys():
                amount = self.invites[member.id][2]
                if self.invites[member.id][0] == ctx.author.id:
                    del self.invites[member.id]
                    await ctx.send(f"Ставки по {humanize.intcomma(amount)}{UNIT} приняты!")
                    await asyncio.sleep(2)
                    if random.random() < 0.5:
                        self.accounts[member.id] += amount
                        self.accounts[ctx.author.id] -= amount
                        await ctx.send(f"{member.mention} Выйграл! Ему достается {humanize.intcomma(amount)}{UNIT}")
                    else:
                        self.accounts[member.id] -= amount
                        self.accounts[ctx.author.id] += amount
                        await ctx.send(f"{ctx.author.mention} Выйграл! Ему достается {humanize.intcomma(amount)}{UNIT}")
                else:
                    await ctx.author.send("Этот человек отправлял запрос не вам!")
            else:
                await ctx.author.send("Этот человек не отправлял вам запрос в течении последней минуты!")
        else:
            await ctx.author.send("Эта команда доступна только в канале #🎰╰╮казино")

    @commands.command(aliases=["баланс", "coins", "purse"])
    async def balance(self, ctx):
        if ctx.channel.id == 757288748672221265:
            await ctx.send(f"{ctx.author.mention}, у вас на балансе {humanize.intcomma(self.accounts[ctx.author.id])}{UNIT}")

    @commands.command()
    async def claim(self, ctx):
        if (self.giveaway1_claim) and (self.bank > self.giveaway1_amount) and (ctx.author.id not in self.giveaway1_claimed):
            self.accounts[ctx.author.id] += self.giveaway1_amount
            self.giveaway1_claimed.append(ctx.author.id)
            await ctx.send(f"{ctx.author.mention} Вы забрали свой приз")
    
    #
    #  admin-only
    #
    @commands.command()
    @commands.check(is_developer)
    async def give(self, ctx, member:discord.Member, amount:int):
        if amount < self.bank and amount > 0:
            self.accounts[member.id] += amount
        elif 
    
    @commands.command()
    @commands.check(is_developer)
    async def setvalue(self, ctx, var:str, value:int):
        if var == "bank":
            self.bank = value
        elif var == "win_chance_a":
            self.win_chance_a = value
        elif var == "win_chance_b":
            self.win_chance_b = value
        elif var == "giveaway1_amount":
            self.giveaway1_amount = value
    
    @commands.command()
    @commands.check(is_developer)
    async def startgiveaway(self, ctx):
        self.giveaway1_task.start()

    @commands.command()
    @commands.check(is_developer)
    async def casinoinfo(self, ctx):
        await ctx.author.send(f"accounts: ```{self.accounts}```, bank: {self.bank}, win_chance_a: {self.win_chance_a}, win_chance_b: {self.win_chance_b}, giveaway1_amount: {self.giveaway1_amount}")
    
    @commands.command()
    @commands.check(is_developer)
    async def loadaccounts(self, ctx, *, dictionary):
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
    #
    #  tasks
    #
    @tasks.loop(minutes=30)
    async def giveaway1_task(self):
        content = f"@here Проводится раздача коинов по {self.giveaway1_amount}{UNIT} на человека! Чтобы забрать свою введите команду >claim"
        message = await self.client.get_channel(757288748672221265).send(content)

        self.giveaway1_claimed = []
        self.giveaway1_claim = True
        await asyncio.sleep(900)
        self.giveaway1_claim = False

        await message.delete()
    #
    #  events
    #
    @commands.Cog.listener()
    async def on_ready(self):
        self.giveaway1_task.start()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 757883097881640980 and not payload.member.id in self.accounts.keys():
            await payload.member.add_roles(self.client.get_guild(payload.guild_id).get_role(757899902222204961))
            self.accounts[payload.member.id] = 500
            await payload.member.send("Ваш аккаунт в казино был создан. Стартовый баланс: 500" + UNIT)

def setup(client):
    client.add_cog(Casino(client))

# if ctx.author.id in self.accounts.keys():
#     pass
# else:
#     pass
