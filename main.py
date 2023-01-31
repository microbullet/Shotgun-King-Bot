import discord
import simplegeneralgroup
import os
MY_GUILD = discord.Object(id=1234567890)

class MyBot(discord.ext.commands.Bot):
    async def on_ready(self):
        await self.tree.sync(guild=MY_GUILD)

bot: discord.ext.commands.Bot = MyBot

@bot.tree.command(guild=MY_GUILD)
async def slash(interaction: discord.Interaction, number: int, string: str):
    await interaction.response.send_message(f'Modify {number=} {string=}', ephemeral=True)

bot.tree.add_command(simplegeneralgroup.Generalgroup(bot), guild=MY_GUILD)

if __name__ == "__main__":
    bot.run(os.environ["DISCORD_TOKEN"])