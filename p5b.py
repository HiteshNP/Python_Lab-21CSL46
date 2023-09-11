"""Develop a python program that could search the text in a file for phone numbers
(+919900889977) and email addresses (sample@gmail.com)"""

import re

# Define patterns
phone_pattern = re.compile(r'\+\d{12}')
email_pattern = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

# Open the text file
with open('file.txt', 'r') as f:
    text = f.read()

# Search for phone numbers and email addresses
phones = phone_pattern.findall(text)
emails = email_pattern.findall(text)

# Print results
print(f"Phone numbers found: {phones}")
print(f"Emails found: {emails}")
