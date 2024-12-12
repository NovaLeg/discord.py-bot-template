import discord
import os
from discord.ext import commands
from config.config import color, token, owner

class Nova(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="-", intents=discord.Intents.all(), help_command=None)
        self.owner_ids = OWNER

    async def on_ready(self):
        print(f'{self.user.display_name} is ready!')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/help"))

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f'[Loaded] `{filename}`')
                except Exception as e:
                    print(f'Failed to load {filename}: {e}')

bot = Nova()
bot.run(token)
