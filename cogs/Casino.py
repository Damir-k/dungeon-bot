import asyncio
import random
import discord
from discord.ext import commands

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
    
    @commands.command()
    async def newacc(self, ctx):
        if ctx.channel.id == 757288748672221265:
            if ctx.author.id in self.accounts.keys():
                await ctx.send("У вас уже есть аккаунт в нашем казино!")
            else:
                self.accounts[ctx.author.id] = 1000
                await ctx.send("Ваш новый аккаунт был успешно создан. Стартовый баланс: 1000 монет")
    
    @commands.command(aliases=["money", "coins"])
    async def balance(self, ctx):
        if ctx.channel.id == 757288748672221265:
            if ctx.author.id in self.accounts.keys():
                await ctx.send(f"Ваш баланс: {self.accounts[ctx.author.id]}")
            else:
                await ctx.send("У вас нет аккаунта в нашем казино. Используйте команду newacc.")
    
    @commands.command()
    async def bet(self, ctx, amount:int):
        if ctx.channel.id == 757288748672221265 and amount >= 1 and self.accounts[ctx.author.id] >= amount:
            message = await ctx.send(content="Ставка сделана")
            await asyncio.sleep(0.5)
            await message.edit(content="Ставка сделана:arrow_right:")
            await asyncio.sleep(0.5)
            await message.edit(content="Ставка сделана:arrow_right::arrow_right:")
            await asyncio.sleep(0.5)
            if random.choice([True, False]):
                await message.edit(content=f"Ставка сделана:arrow_right::arrow_right::arrow_right::white_check_mark:\nВы выйграли {amount} монет!")
                self.accounts[ctx.author.id] += amount
            else:
                await message.edit(content=f"Ставка сделана:arrow_right::arrow_right::arrow_right::no_entry:\nК сожалению вы проиграли {amount} монет!")
                self.accounts[ctx.author.id] -= amount

    #
    #  saving/loading casino status
    #
    @commands.command()
    @commands.check(is_developer)
    async def savecasino(self, ctx):
        await ctx.author.send(f"```{self.accounts}```")
    
    @commands.command()
    @commands.check(is_developer)
    async def loadcasino(self, ctx):
        self.accounts = dict(ctx.content)
    



def setup(client):
    client.add_cog(Casino(client))

# if ctx.author.id in self.accounts.keys():
#     pass
# else:
#     pass