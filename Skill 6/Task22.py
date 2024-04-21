## Skill 6, Task 22: Nb of days between two dates
## Description: Print number of days between two given days
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

# Import datetime for the excerise
from datetime import date

# Define the two dates as per the instructions
a = date(2017, 2, 28)
b = date(2018, 2, 28)

# Calculate the difference between the two dates and print to the console the amount of days
difference = b - a
print(f"Number of days between the two dates: {difference.days}")