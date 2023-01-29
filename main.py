import discord
from discord import app_commands
import os

punkcan = 535849677858275329
gid = 883968176155664405

bot = discord.Bot()

# If you use commands.Bot, @bot.slash_command should be used for
# slash commands. You can use @bot.slash_command with discord.Bot as well.

random = bot.create_group(
    "random", "gives a random thing based on the sub"
)


@random.command()  # Create a slash command under the math group
async def add(ctx: discord.ApplicationContext, num1: int, num2: int):
    """Get the sum of 2 integers."""
    await ctx.respond(f"The sum of these numbers is **{num1+num2}**")


bot.add_application_command(random)


bot.run(os.environ["DISCORD_TOKEN"])