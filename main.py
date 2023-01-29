# This example requires the 'message_content' privileged intents

import os
import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents, guild_id=id=883968176155664405)
tree = app_commands.CommandTree(client)

@tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=883968176155664405)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name='sync', description='Owner only')
async def sync(interaction: discord.Interaction):
    if interaction.user.id == 508066804485324831:
        await tree.sync()
        print('Command tree synced.')
    else:
        await interaction.response.send_message('You must be the owner to use this command!')

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=883968176155664405))
    print("Ready!")

client.run(os.environ["DISCORD_TOKEN"])