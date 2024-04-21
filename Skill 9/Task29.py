## Skill 9, Task 29: Debug and modify
## Description: Debug the code
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

# Code from the assignment, the code was simply debugged not changed or commented (expect for where errors where found and corrected)

# Fix the below code so it works
# This programm tells you if the given number is a float or not, and whether its above or below a 100

print('Please input a float number')
try:
    a = float(input("Enter a number:")) # Casting the input to a float, whcih will raise an ValueError expection if it is not a float
    print('Yes - that is a float number')

    # Corrected the problems with spacing and idents
    if a > 100:
        print('Your number is higher than 100')
    else:
        print('Your number is lower than 100')
except ValueError:
    print('Error - that is not a float')