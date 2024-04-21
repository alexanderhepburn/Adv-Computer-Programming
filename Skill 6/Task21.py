## Skill 6, Task 21: Next 5 days
## Description: Program to print next 5 days starting from today
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

# Import datetime for the excerise
from datetime import datetime, timedelta

# Get today's date with the datetime framework
today = datetime.now()

# Input that can be changed
days = 5

# For loop to loop through the days
for i in range(days):
    # Calculate the date for the current iteration
    next_date = today + timedelta(days=i)
    # Print the formatted date to the console
    print(next_date.strftime('%Y-%m-%d %H:%M:%S.%f'))