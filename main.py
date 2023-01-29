import discord
from discord import app_commands
import os

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord. Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=908141823288045568))
            self.synced = True
        print (f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command (name="test", description="testing", guild=discord.Object(id = 908141823288045568))
async def self(interaction: discord. Interaction, name: str):
    await interaction.response.send_message(f"Hello {name}! I was made with Discord.py!")

client.run(os.environ["DISCORD_TOKEN"])