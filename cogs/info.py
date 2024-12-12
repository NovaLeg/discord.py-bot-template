import discord
from discord.ext import commands
import time
from config.config import color  

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command(name="ping", description="Check the bot's latency")
    async def ping(self, ctx):
        embed = discord.Embed(
            description=f"My Latency: **{round(self.bot.latency * 1000)}ms**",
            color=color
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name="uptime", description="Check the bot's uptime")
    async def uptime(self, ctx):
        current_time = time.time()
        uptime_seconds = int(current_time - self.start_time)

        days = uptime_seconds // (24 * 3600)
        hours = (uptime_seconds % (24 * 3600)) // 3600
        minutes = (uptime_seconds % 3600) // 60
        seconds = uptime_seconds % 60

        uptime = []
        if days > 0:
            uptime.append(f"{days} day{'s' if days > 1 else ''}")
        if hours > 0:
            uptime.append(f"{hours} hour{'s' if hours > 1 else ''}")
        if minutes > 0:
            uptime.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
        if seconds > 0:
            uptime.append(f"{seconds} second{'s' if seconds > 1 else ''}")

        uptime_str = ", ".join(uptime) if uptime else "0 seconds"

        embed = discord.Embed(
            description=f"Uptime: {uptime_str}",
            color=color
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(info(bot))
    
