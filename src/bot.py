import os
import discord
import logging

from discord.ext import commands
from dotenv import load_dotenv

log = logging.getLogger('discord')

# Initialise dotenv
load_dotenv()

# Constants
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX")

intents = discord.Intents.default()
intents.message_content = True
help_command = commands.DefaultHelpCommand(no_category="Commands")

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=help_command)


@bot.event
async def on_ready():
    log.info(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    """
    'Ping' to get a 'Pong' response with latency
    """
    latency = round(bot.latency * 1000)
    log.info(f"!ping: Latency = {latency}")
    await ctx.send(f"Pong! {latency}ms")


bot.run(TOKEN)