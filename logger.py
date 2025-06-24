import os
from datetime import datetime

LOGS_DIR = 'logs'

def ensure_logs_dir():
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)

def get_log_file_path():
    today = datetime.now().strftime('%Y-%m-%d')
    return os.path.join(LOGS_DIR, f'{today}.log')

def log_message(message):
    """
    Appends a timestamped message to the daily log file in the logs directory.
    """
    ensure_logs_dir()
    log_file = get_log_file_path()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'[{timestamp}] {message}\n') 