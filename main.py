import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print("🤖 Hayumi đã online.")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if "hello" in content or "chào" in content:
        await message.channel.send(
            "Chào Bố, con là Hayumi."
        )

    await bot.process_commands(message)

bot.run(TOKEN)
