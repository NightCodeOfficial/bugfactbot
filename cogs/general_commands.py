import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime

from logger import log_message

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="ping", description="Check bot latency")
    async def ping_slash(self, interaction: discord.Interaction):
        """Slash command to check bot latency"""
        try:
            latency = round(self.bot.latency * 1000)
            embed = discord.Embed(
                title="🏓 Pong!",
                description=f"Bot latency: **{latency}ms**",
                color=discord.Color.green(),
                timestamp=datetime.utcnow()
            )
            embed.set_footer(text=f"Requested by {interaction.user.display_name}")
            
            await interaction.response.send_message(embed=embed)
            log_message(f"Ping requested by {interaction.user} in {interaction.guild.name} - Latency: {latency}ms")
            
        except Exception as e:
            log_message(f"Error in ping slash command: {e}")
            await interaction.response.send_message("❌ Error checking latency.", ephemeral=True)
    
    @commands.command(name="ping")
    async def ping_prefix(self, ctx):
        """Prefix command to check bot latency"""
        try:
            latency = round(self.bot.latency * 1000)
            embed = discord.Embed(
                title="🏓 Pong!",
                description=f"Bot latency: **{latency}ms**",
                color=discord.Color.green(),
                timestamp=datetime.utcnow()
            )
            embed.set_footer(text=f"Requested by {ctx.author.display_name}")
            
            await ctx.send(embed=embed)
            log_message(f"Ping requested by {ctx.author} in {ctx.guild.name} - Latency: {latency}ms")
            
        except Exception as e:
            log_message(f"Error in ping prefix command: {e}")
            await ctx.send("❌ Error checking latency.")
    
    @commands.command(name="help", aliases=["h"])
    async def help_command(self, ctx):
        """Show help information"""
        embed = discord.Embed(
            title="🐛 Bug of the Week Bot Help",
            description="Get the latest bug facts and information!",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )
        
        embed.add_field(
            name="🐛 Bug Commands",
            value="""
**Slash Commands:**
`/bugfact` - Get the latest bug fact with image

**Prefix Commands:**
`bb!bugfact` or `bb!bf` - Get the latest bug fact with image
            """,
            inline=False
        )
        
        embed.add_field(
            name="🔧 General Commands",
            value="""
**Slash Commands:**
`/ping` - Check bot latency

**Prefix Commands:**
`bb!ping` - Check bot latency
`bb!help` or `bb!h` - Show this help message
            """,
            inline=False
        )
        
        embed.add_field(
            name="About",
            value="This bot fetches the latest bug information from bugoftheweek.com and displays it in a beautiful embed with images.",
            inline=False
        )
        
        embed.set_footer(text="Data from bugoftheweek.com")
        
        await ctx.send(embed=embed)
        log_message(f"Help requested by {ctx.author} in {ctx.guild.name}")

async def setup(bot):
    """Setup function for the cog"""
    await bot.add_cog(GeneralCommands(bot))
    log_message("GeneralCommands cog loaded")
