# utils.py
import re

def clean_ingredient_string(raw):
    # Remove punctuation, lowercase, and split by commas
    raw = re.sub(r'[^\w\s,]', '', raw)  # Remove everything except words, spaces, commas
    parts = [item.strip().lower() for item in raw.split(',') if item.strip()]
    return parts
