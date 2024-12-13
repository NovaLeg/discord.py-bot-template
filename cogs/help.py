import discord
from discord.ext import commands
from config.config import color

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", description="Show the help panel or specific command help")
    async def help(self, ctx):
        embed = discord.Embed(
            color=color,
            description="I'm Nova, a bot made by [Nova.](https://discord.com/users/1142754238179594240)\n### Features\n- General\n- Use the button below to explore the commands of the Settings module."
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)

        view = interaction(ctx.author.id, self.bot)
        await ctx.send(embed=embed, view=view)

class interaction(discord.ui.View):
    def __init__(self, command_runner_id, bot):
        super().__init__()
        self.command_runner_id = command_runner_id
        self.bot = bot

        self.add_item(button(label="Settings", style=discord.ButtonStyle.primary, category="settings", command_runner_id=command_runner_id, bot=bot))

class button(discord.ui.Button):
    def __init__(self, label, style, category, command_runner_id, bot):
        super().__init__(label=label, style=style)
        self.category = category
        self.command_runner_id = command_runner_id
        self.bot = bot

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.command_runner_id:
            await interaction.response.send_message("You can't use this.", ephemeral=True)
            return

        embed = discord.Embed(color=color)
        if self.category == "settings":
            embed.description = "`help`, `ping`, `uptime`"
            author_text = "Settings"
            embed.set_author(name=author_text, icon_url=self.bot.user.avatar.url)

        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(help(bot))
