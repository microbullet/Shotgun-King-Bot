import discord
import random 
import os
import json
from discord.ui import Button, View
from discord.ext import commands
from asyncio import sleep

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="::", intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.slash_command(name="ping", description="Get the bot's latency")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {client.latency}")

@client.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

client.run(os.environ["DISCORD_TOKEN"])