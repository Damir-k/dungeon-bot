import discord
from discord.ext import commands

class ModOnly(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=3):
        if type(amount) != int:
            return
        if amount <= 0:
            return

        await ctx.channel.purge(limit=amount+1)
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(member.mention + ", увидимся!")
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send("Ложись спатки, " + member.mention)
    
    @commands.command(aliases=["pardon"])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send("Мы прощаем тебя, " + user.name)
                return

def setup(client):
    client.add_cog(ModOnly(client))