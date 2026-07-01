import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents) # feel free to change the prefix


@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user} (id: {bot.user.id})")
    print(f"Running version: {os.environ.get('APP_VERSION', 'unknown')}")


def main() -> None:
    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN is not set (see .env.example)")
    bot.run(token)

# ======= Add commands here =========

# ===================================

if __name__ == "__main__":
    main()
