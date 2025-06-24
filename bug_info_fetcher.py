import feedparser
import json
import re
from datetime import datetime
from bs4 import BeautifulSoup
from logger import log_message

RSS_URL = "https://bugoftheweek.com/?format=rss"

def clean_fetched_info(text):
    """
    Clean text to be more reader and Python friendly.
    Removes HTML tags, extra whitespace, and normalizes text.
    """
    if not text:
        return ""
    # Remove HTML tags using BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')
    clean_text = soup.get_text()
    # Remove extra whitespace and normalize
    clean_text = re.sub(r'\s+', ' ', clean_text)  # Replace multiple spaces with single space
    clean_text = re.sub(r'\n\s*\n', '\n', clean_text)  # Remove empty lines
    clean_text = clean_text.strip()
    # Remove common HTML entities
    clean_text = clean_text.replace('&nbsp;', ' ')
    clean_text = clean_text.replace('&amp;', '&')
    clean_text = clean_text.replace('&lt;', '<')
    clean_text = clean_text.replace('&gt;', '>')
    clean_text = clean_text.replace('&quot;', '"')
    # Normalize quotes
    clean_text = clean_text.replace('"', '"').replace('"', '"')
    clean_text = clean_text.replace(''', "'").replace(''', "'")
    return clean_text

def parse_published_date(date_string):
    """
    Parse the published date string into a Python datetime object.
    """
    try:
        # Parse the RSS date format: "Mon, 16 Jun 2025 04:00:00 +0000"
        return datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %z")
    except ValueError as e:
        log_message(f"Error parsing date '{date_string}': {e}")
        # If parsing fails, return the original string
        return date_string

def fetch_latest_bug(rss_url=RSS_URL):
    """Fetch the latest bug information and save to JSON."""
    log_message("Starting fetch of latest bug info from RSS feed.")
    feed = feedparser.parse(rss_url)
    if not feed.entries:
        log_message("No entries found in RSS feed.")
        print("No entries found.")
        return None
    latest_entry = feed.entries[0]
    bug_data = {
        "title": latest_entry.title,
        "link": latest_entry.link,
        "published": latest_entry.published,
        "summary": latest_entry.summary,
        "fetched_at": datetime.now().isoformat()
    }
    try:
        with open("latest_bug.json", "w", encoding="utf-8") as f:
            json.dump(bug_data, f, indent=2, ensure_ascii=False)
        log_message("Bug information saved to latest_bug.json.")
    except Exception as e:
        log_message(f"Error saving latest_bug.json: {e}")
    print(f"Bug information saved to latest_bug.json")
    return bug_data

def get_clean_bug_info(rss_url=RSS_URL):
    """Fetch and return cleaned bug information."""
    bug_data = fetch_latest_bug(rss_url)
    if not bug_data:
        return None
    clean_data = {
        "title": clean_fetched_info(bug_data["title"]),
        "link": bug_data["link"],
        "published": parse_published_date(bug_data["published"]),
        "summary": clean_fetched_info(bug_data["summary"]),
        "summary_html": bug_data["summary"],  # Keep raw HTML for image extraction
        "fetched_at": bug_data["fetched_at"]
    }
    try:
        with open("latest_bug_clean.json", "w", encoding="utf-8") as f:
            json_data = clean_data.copy()
            if isinstance(json_data["published"], datetime):
                json_data["published"] = json_data["published"].isoformat()
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        log_message("Cleaned bug information saved to latest_bug_clean.json.")
    except Exception as e:
        log_message(f"Error saving latest_bug_clean.json: {e}")
    print(f"Cleaned bug information saved to latest_bug_clean.json")
    return clean_data

def print_clean_info():
    """Print the cleaned bug information in a readable format."""
    clean_data = get_clean_bug_info()
    if not clean_data:
        log_message("No clean data to print.")
        return
    print("\n" + "="*80)
    print("CLEANED BUG OF THE WEEK")
    print("="*80)
    print(f"Title: {clean_data['title']}")
    print(f"Link: {clean_data['link']}")
    print(f"Published: {clean_data['published']}")
    print(f"Fetched: {clean_data['fetched_at']}")
    print("\nSummary:")
    print("-" * 40)
    print(clean_data['summary'])
    print("="*80)
    log_message("Printed cleaned bug info to console.")

if __name__ == "__main__":
    print_clean_info()
