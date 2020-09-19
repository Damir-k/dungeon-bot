import discord
from discord.ext import commands
import config
import random
import datetime

client = commands.Bot(command_prefix=">")

#  initialization
@client.event
async def on_ready():
    print('Logged in!')

#
#  general commands
#  
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
async def helpme(ctx, category=None):
    await ctx.send(config.help(category))

@client.command()
async def age(ctx):
    time_joined = ctx.author.joined_at
    current_time = datetime.datetime.now()
    time_passed = current_time - time_joined
    await ctx.send(ctx.author.mention + " на сервере " + str(time_passed.days) + " дней, " + str(time_passed.seconds // 3600) + " часов")

#
# moder-only
#
@client.command()
async def clear(ctx, amount=3):
    if type(amount) != int:
        return
    if amount <= 0:
        return

    if ctx.channel.permissions_for(ctx.author).manage_messages == True:
        await ctx.channel.purge(limit=amount+1)

@client.command()
async def kick(ctx, member:discord.Member, *, reason=None):
    if ctx.channel.permissions_for(ctx.author).kick_members == True:
        await member.kick(reason=reason)
    await ctx.send(member.mention + ", увидимся!")

@client.command()
async def ban(ctx, member:discord.Member, *, reason=None):
    if ctx.channel.permissions_for(ctx.author).ban_members == True:
        await member.ban(reason=reason)
    await ctx.send("Ложись спатки, " + member.mention)

@client.command(aliases=["unban", "pardon"])
async def unban(ctx, *, member):
    if ctx.channel.permissions_for(ctx.author).ban_members == True:
        banned_users = ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send("Мы прощаем тебя, " + user.mention())
                return

        
        
        



client.run(config.TOKEN)
