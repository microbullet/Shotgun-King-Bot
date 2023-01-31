import discord
import os # default module

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run("MTA2OTA2MzIzNTk4NDE3MTA0OQ.GiPpcb.EraypgpBEOcu2FK2CqFt7_H91LPvU0N4WOl3R0")