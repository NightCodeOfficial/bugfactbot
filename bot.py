import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import traceback
from datetime import datetime

from config import DISCORD_TOKEN, BOT_NAME
from bug_info_fetcher import get_clean_bug_info
from logger import log_message

# Bot setup with intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

class BugBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='bb!',
            intents=intents,
            help_command=None
        )
        self.initial_extensions = ['cogs.bug_commands', 'cogs.general_commands']
    
    async def setup_hook(self):
        """Called when the bot is starting up"""
        log_message(f"Bot starting up: {BOT_NAME}")
        
        # Load extensions
        for extension in self.initial_extensions:
            try:
                await self.load_extension(extension)
                log_message(f"Loaded extension: {extension}")
            except Exception as e:
                log_message(f"Failed to load extension {extension}: {e}")
        
        log_message("Bot setup complete")
    
    async def on_ready(self):
        """Called when the bot is ready"""
        log_message(f"Bot logged in as {self.user} (ID: {self.user.id})")
        log_message(f"Bot is in {len(self.guilds)} guilds")
        
        # Sync slash commands
        try:
            synced = await self.tree.sync()
            log_message(f"Synced {len(synced)} command(s)")
        except Exception as e:
            log_message(f"Failed to sync commands: {e}")
    
    async def on_command_error(self, ctx, error):
        """Global error handler"""
        if isinstance(error, commands.CommandNotFound):
            return
        
        log_message(f"Command error in {ctx.guild.name} by {ctx.author}: {error}")
        
        # Send user-friendly error message
        embed = discord.Embed(
            title="❌ Error",
            description="An error occurred while processing your command.",
            color=discord.Color.red(),
            timestamp=datetime.utcnow()
        )
        embed.add_field(name="Error", value=str(error))
        embed.set_footer(text="Please try again or contact an administrator.")
        
        try:
            await ctx.send(embed=embed)
        except:
            await ctx.send("An error occurred while processing your command.")

# Create bot instance
bot = BugBot()

@bot.event
async def on_ready():
    """Override the on_ready event"""
    log_message(f"Bot is ready! Logged in as {bot.user}")

if __name__ == "__main__":
    if not DISCORD_TOKEN:
        log_message("ERROR: No Discord token found. Please set DISCORD_TOKEN in your .env file")
        exit(1)
    
    try:
        bot.run(DISCORD_TOKEN)
    except Exception as e:
        log_message(f"Failed to start bot: {e}")
        traceback.print_exc() 