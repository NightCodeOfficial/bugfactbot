# Bug of the Week Discord Bot

A Discord bot that fetches and displays the latest bug information from the Bug of the Week RSS feed.

## Features

- Fetches latest bug information from RSS feed
- Displays bug facts in Discord channels
- Clean and formatted output
- Automatic command syncing

## Setup

### Prerequisites

- Python 3.8 or higher
- A Discord bot token
- Git (optional, for version control)

### Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd bug_of_the_week
   ```

2. **Create a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   
   # On macOS/Linux
   python3 -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # On Windows (Command Prompt)
   venv\Scripts\activate
   
   # On Windows (PowerShell)
   venv\Scripts\Activate.ps1
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create environment file**
   Create a `.env` file in the project root with your Discord bot token:
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

6. **Run the bot**
   ```bash
   python bot.py
   ```

### Discord Bot Setup

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section
4. Create a bot and copy the token
5. Add the bot to your server with appropriate permissions
6. Paste the token in your `.env` file

## Usage

Once the bot is running, you can use the following commands:

- `bb!bugfact` - Get the latest bug fact
- `bb!help` - Show help information

## Project Structure

```
bug_of_the_week/
├── bot.py                 # Main bot file
├── bug_info_fetcher.py    # RSS feed fetcher
├── config.py              # Configuration settings
├── cogs/                  # Bot command modules
│   ├── bug_commands.py
│   └── general_commands.py
├── logs/                  # Log files
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

