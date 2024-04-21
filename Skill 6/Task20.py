## Skill 6, Task 20: Today, Tomorrow, Yesterday
## Description: Print yesterday, today and tomorrow respectively in YYYY-MM-DD format
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

# Import datetime for the excerise
from datetime import datetime, timedelta

# Get today's date with the datetime framework
today = datetime.now()

# Calculate yesterday and tomorrow dates by using timedelta
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Format the dates as strings as required by the assignment
formatted_yesterday = yesterday.strftime('%Y-%m-%d')
formatted_today = today.strftime('%Y-%m-%d')
formatted_tomorrow = tomorrow.strftime('%Y-%m-%d')

# Output the dates as per the assignment instructions (no additional formatting as been done)
print(f"Yesterday: {formatted_yesterday}")
print(f"Today: {formatted_today}")
print(f"Tomorrow: {formatted_tomorrow}")