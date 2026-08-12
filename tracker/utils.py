import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), 'expiry_data.json')

def load_items():
    try:
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_items(items):
    with open(DATA_FILE, 'w') as f:
        json.dump(items, f, indent=4)

def calculate_status(expiry_date_str):
    try:
        expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
        today = datetime.now().date()
        days_left = (expiry_date - today).days

        if days_left < 0:
            return "Expired", "red"
        elif days_left <= 3:
            return "Expiring Soon", "orange"
        else:
            return "Fresh", "green"
    except ValueError:
        return "Invalid Date", "gray"