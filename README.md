# Bug of the Week Discord Bot

A modern Discord bot that fetches and displays the latest bug facts from [bugoftheweek.com](https://bugoftheweek.com) with beautiful embeds and images.

## Features

- 🐛 Fetch latest bug information from RSS feed
- 🖼️ Display bug images in Discord embeds
- 📱 Both slash commands and prefix commands
- 📊 Comprehensive logging system
- 🛡️ Error handling and user-friendly messages
- 🎨 Beautiful Discord embeds with proper formatting

## Commands

### Slash Commands
- `/bugfact` - Get the latest bug fact with image

### Prefix Commands
- `!bugfact` or `!bf` - Get the latest bug fact with image
- `!help` or `!h` - Show help information

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create Discord Bot
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section
4. Create a bot and copy the token
5. Enable the following intents:
   - Message Content Intent
   - Server Members Intent

### 3. Configure Environment
Create a file called `.env`  in the project root:
```env
DISCORD_TOKEN=your_discord_bot_token_here
```

### 4. Invite Bot to Server
Use this URL (replace `YOUR_BOT_CLIENT_ID` with your bot's client ID):
```
https://discord.com/api/oauth2/authorize?client_id=YOUR_BOT_CLIENT_ID&permissions=2048&scope=bot%20applications.commands
```

### 5. Run the Bot
```bash
python bot.py
```

## Project Structure

```
bug_of_the_week/
├── bot.py                 # Main bot file
├── config.py              # Configuration and environment variables
├── bug_info_fetcher.py    # RSS feed fetching and data cleaning
├── logger.py              # Logging utility
├── requirements.txt       # Python dependencies
├── cogs/
│   ├── __init__.py
│   └── bug_commands.py    # Bot commands
├── logs/                  # Log files (created automatically)
└── README.md
```

## Features in Detail

### Data Fetching
- Fetches latest bug information from RSS feed
- Cleans HTML content for better readability
- Extracts images for Discord embeds
- Saves data to JSON files for caching

### Logging
- Comprehensive logging system
- Daily log files in `logs/` directory
- Tracks all bot activities and errors

### Error Handling
- Graceful error handling for network issues
- User-friendly error messages
- Fallback responses when data is unavailable

## Usage Examples

### Basic Usage
```
!bugfact
```
or
```
/bugfact
```

### Help Command
```
!help
```

## Development

### Adding New Commands
1. Create a new cog in the `cogs/` directory
2. Add the cog to `bot.py` in the `initial_extensions` list
3. Use the `@commands.command()` or `@app_commands.command()` decorators

### Logging
Use the logger throughout the project:
```python
from logger import log_message

log_message("Your log message here")
```

## Requirements

- Python 3.8+
- discord.py 2.3.0+
- feedparser 6.0.0+
- beautifulsoup4 4.12.0+
- python-dotenv 1.0.0+

