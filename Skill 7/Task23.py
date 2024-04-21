## Skill 7, Task 23: Sum of ten numbers
## Description: Collect ten numbers and print the sum to the console
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

# List of integers to be collected and variable for how many numbers should be collected (description says 10 but example only has 8)
numbers = []
number_of_numbers = 10

# For loop to collect two integers from the user
for i in range(number_of_numbers):
    while True:
        # Collect an integer from the user
        input_number = input(f"Please enter a number ({i+1}/{number_of_numbers}): ")
        try:
            numbers.append(int(input_number)) # If the input is an integer append it to the numbers list
            break # Break out of the while loop to collect the next input
        except ValueError:
            print("Only ints can be entered, please try again.") # Print an error if the input is not an integer

# Print both inputs and sum of the numbers
print(f"The sum of the numbers: {numbers} is: {sum(numbers)}!")
