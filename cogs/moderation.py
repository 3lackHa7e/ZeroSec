import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks a member from the server""" 
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked. Reason: {reason}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans a member from the server"""
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned. Reason: {reason}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """Unbans a member from the server"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            if ban_entry.user.name == member_name and ban_entry.user.discriminator == member_discriminator:
                await ctx.guild.unban(ban_entry.user)
                await ctx.send(f'Unbanned {ban_entry.user.mention}')
                return
        await ctx.send(f'User {member} not found in ban list.')

def setup(bot):
    bot.add_cog(Moderation(bot))