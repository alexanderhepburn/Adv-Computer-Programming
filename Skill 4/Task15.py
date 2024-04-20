## Skill 4, Task 15: Append a new item to the array
## Description: Append an item to the end of an array
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# Given original_array from the assignment
original_array = ('i', [1, 3, 5, 7, 9])

# Create a variable to store the integer
input_value = 0


while True:
    # Collect the integer from the user
    input_number = input("Please enter a number to append to the end of the array (whole number): ")
    try:
        input_value = int(input_number)  # If the input is an integer change input_value
        original_array[1].append(input_value)
        print(f"New array length is: {len(original_array[1])}; array is now: ")
        break  # Break out of the while loop to collect the next input
    except ValueError:
        print("Only ints can be entered, please try again.")  # Print an error if the input is not an integer