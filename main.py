# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

greetings = bot.create_group("greetings", "Greet people")

@greetings.command()
async def hello(ctx):
  await ctx.respond(f"Hello, {ctx.author}!")

@greetings.command()
async def bye(ctx):
  await ctx.respond(f"Bye, {ctx.author}!")

bot.run(os.environ["DISCORD_TOKEN"])
