import discord
from discord.ext import commands

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot with the token
# Replace 'YOUR_TOKEN_HERE' with your actual bot token
bot.run('YOUR_TOKEN_HERE')
