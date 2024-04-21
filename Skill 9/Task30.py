## Skill 9, Task 30: Find the mistake
## Description: Correct the code
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

# Code from the assignment, the code was simply debugged not changed or commented (expect for where errors where found and corrected)

# This gets the random number generator.

# There are 3 mistakes in this code - FIX them

import random

i = random.randrange(10,50)
print('Your number is', i)
if i < 20:
    print("That is less than 20.")
elif i == 20:
    print("That is exactly twenty. How nice for you.")
else:
    print("Wow! That's more than 20!")

if i % 3 == 0:
    print("It is divisible by 3.")
elif i % 2 == 1:
    print("That is an odd number.")
else:
    print("That is twice", i / 2, '.')


# First mistake: j instead of i
# Second mistake: else: if instead of elif
# Third mistake: i + 1 instead of i?
# Fourth mistake: i < 200 instead of i < 20
# Fifth mistake: i > 20 needs to be i == 3 and below the i < 20 line
# Sixth mistake: else: Wow Thats more than 20 needs to be below the previous mistake