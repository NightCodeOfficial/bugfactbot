import discord
from discord import app_commands
from discord.ext import commands
import asyncio
from datetime import datetime
import re
from bs4 import BeautifulSoup

from bug_info_fetcher import get_clean_bug_info
from logger import log_message

class BugCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def extract_image_url(self, summary_html):
        """Extract the first image URL from the summary HTML"""
        try:
            soup = BeautifulSoup(summary_html, 'html.parser')
            img_tag = soup.find('img')
            if img_tag and img_tag.get('src'):
                return img_tag['src']
        except Exception as e:
            log_message(f"Error extracting image URL: {e}")
        return None
    
    async def create_bug_embed(self, bug_data):
        """Create a Discord embed with bug information and image"""
        if not bug_data:
            embed = discord.Embed(
                title="❌ Error",
                description="Failed to fetch bug information. Please try again later.",
                color=discord.Color.red(),
                timestamp=datetime.utcnow()
            )
            return embed, None
        
        # Create embed
        embed = discord.Embed(
            title="🐛 Bug of the Week",
            description=bug_data['title'],
            url=bug_data['link'],
            color=discord.Color.green(),
            timestamp=datetime.utcnow()
        )
        
        # Add fields
        if bug_data['published']:
            if isinstance(bug_data['published'], datetime):
                published_str = bug_data['published'].strftime('%B %d, %Y')
            else:
                published_str = str(bug_data['published'])
            embed.add_field(name="📅 Published", value=published_str, inline=True)
        
        # Truncate summary if too long
        summary = bug_data['summary']
        if len(summary) > 1024:
            summary = summary[:1021] + "..."
        
        embed.add_field(name="📝 Summary", value=summary, inline=False)
        
        # Add footer
        embed.set_footer(text="Data from bugoftheweek.com")
        
        # Extract and set image
        image_url = self.extract_image_url(bug_data.get('summary_html', ''))
        if image_url:
            embed.set_image(url=image_url)
        
        return embed, image_url
    
    @app_commands.command(name="bugfact", description="Get the latest bug fact from Bug of the Week")
    async def bugfact_slash(self, interaction: discord.Interaction):
        """Slash command for getting bug facts"""
        await interaction.response.defer(thinking=True)
        
        try:
            log_message(f"Bug fact requested by {interaction.user} in {interaction.guild.name}")
            
            # Fetch bug data
            bug_data = get_clean_bug_info()
            
            # Create embed
            embed, image_url = await self.create_bug_embed(bug_data)
            
            # Send response
            await interaction.followup.send(embed=embed)
            
            log_message(f"Bug fact sent successfully to {interaction.user}")
            
        except Exception as e:
            log_message(f"Error in bugfact slash command: {e}")
            error_embed = discord.Embed(
                title="❌ Error",
                description="An error occurred while fetching the bug fact.",
                color=discord.Color.red(),
                timestamp=datetime.utcnow()
            )
            await interaction.followup.send(embed=error_embed)
    
    @commands.command(name="bugfact", aliases=["bf"])
    async def bugfact_prefix(self, ctx):
        """Prefix command for getting bug facts"""
        try:
            log_message(f"Bug fact requested by {ctx.author} in {ctx.guild.name}")
            
            # Send typing indicator
            async with ctx.typing():
                # Fetch bug data
                bug_data = get_clean_bug_info()
                
                # Create embed
                embed, image_url = await self.create_bug_embed(bug_data)
                
                # Send response
                await ctx.send(embed=embed)
                
                log_message(f"Bug fact sent successfully to {ctx.author}")
                
        except Exception as e:
            log_message(f"Error in bugfact prefix command: {e}")
            error_embed = discord.Embed(
                title="❌ Error",
                description="An error occurred while fetching the bug fact.",
                color=discord.Color.red(),
                timestamp=datetime.utcnow()
            )
            await ctx.send(embed=error_embed)

async def setup(bot):
    """Setup function for the cog"""
    await bot.add_cog(BugCommands(bot))
    log_message("BugCommands cog loaded") 