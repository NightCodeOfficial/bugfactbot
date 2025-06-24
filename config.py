import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Discord Bot Configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Bot Configuration
BOT_PREFIX = '!'
BOT_NAME = 'Bug of the Week Bot'

# RSS Configuration
RSS_URL = "https://bugoftheweek.com/?format=rss"

# Command Configuration
COMMANDS = {
    'bugfact': ['!bugfact', '!bf'],
    'help': ['!help', '!h']
} 