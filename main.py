import discord
from discord import app_commands
from typing import Literal, Optional
from discord.ext.commands import Greedy, Context
from discord.ext import commands
import os

bot = discord.Bot(command_prefix='!')


punkcan = 535849677858275329
gid = 883968176155664405

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=gid))
            self.synced = True
        print(f"We have logged in as {self.user}.")


client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name="test", description="testing", guild=discord.Object(id=gid))
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Hello {name}! I was made with Discord.py!")

@tree.command(name="pingg", description="pong", guild=discord.Object(id=gid))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")

# ------------------

@bot.group(invoke_without_command=True)
async def your_command(ctx):
    await ctx.send("This is your command.")

@your_command.command()
async def subcommand(ctx):
    await ctx.send("This is a subcommand.")

if __name__ == "__main__": 
    client.run(os.environ["DISCORD_TOKEN"])