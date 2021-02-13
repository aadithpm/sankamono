import os
import discord
import lost_sectors
import utils
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()
bot = commands.Bot(command_prefix='*')
bot.remove_command('help')

'''
Events
'''


@bot.event
async def on_ready():
    print(f'Sankamono is observing {len(bot.guilds)} guild(s):')
    for guild in bot.guilds:
        print(guild)


@bot.event
async def on_message(message):
    print(message)

    # Don't break commands
    await bot.process_commands(message)


###

'''
Command definitions
'''


@bot.command()
async def sectors(ctx):
    await ctx.send(embed=lost_sectors.get_lost_sectors_daily(discord.Embed))


@bot.command()
async def help(ctx):
    await ctx.send(embed=utils.get_help_message(discord.Embed))


###


bot.run(DISCORD_TOKEN)
