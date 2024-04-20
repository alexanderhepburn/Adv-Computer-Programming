## Skill 1, Task 2: Printing and input number
## Description: Collect name and greet the user
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# Create a variable to store the user name
user_name = ""

while True:
    # Collect the name from the user
    input_name = input("Please enter your name: ")
    if input_name.isprintable() and len(input_name.split()) == 1: # Verify that the name is printable and that the is only one word
        user_name = input_name # Set the user_name equal to the input
        break # Break out of the while loop to print the result
    else:
        print("Please enter a printable name (name must be one word only).") # Print an error if the input is not correct

# Greet the user with their name
print(f"Hello {user_name}")