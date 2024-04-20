## Skill 2, Task 10: Reverse strings
## Description: Collect first and last name and print last then first name
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

## Function: is_a_name
## Description: checks if a value is a name but checking if it contains any numbers or special charactes
## Input: input_string: String
## Returns: True or False
def is_a_name(input_string):
    # Check to see if the string is printable and doesnt contain any numbers or special characters
    if input_string.isprintable() and not any(char.isdigit() for char in input_string) and not any(not c.isalnum() for c in input_string):
        return True # Return that the string is a name
    else:
        return False # Return that the string is not a name

# List of names to be collected
names = []

# key-value pair to associate which value is the first and which is the last name
value_dictionary = {0: "first", 1: "last"}

# For loop to collect two names from the user
for i in range(2):
    while True:
        # Collect an integer from the user
        input_name = input(f"Please enter your {value_dictionary[i]} name: ")
        if is_a_name(input_name): # Check if the input is a name with the help of our helper method
            names.append(input_name) # If the input is a string append it to the names list
            break # Break out of the while loop to collect the next input
        else:
            print("Only names can be entered (no numbers or characters), please try again.") # Print an error if the input is not a name

# Print the last then first name to the console
print(f"Hello {names[-1]} {names[0]}!")