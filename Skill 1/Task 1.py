## Skill 1, Task 1: Numbers and their sum
## Description: Collect 3 integers from the user and print the sum
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# List of integers to be collected
numbers = []

# For loop to collect three integers from the user
for i in range(3):
    while True:
        # Collect an integer from the user
        input_number = input("Please enter a number (whole number): ")
        if input_number.isdigit(): # Check if the input is an integer
            numbers.append(int(input_number)) # If the input is an integer append it to the numbers list
            break # Break out of the while loop to collect the next input
        else:
            print("Only ints can be entered, please try again.") # Print an error if the input is not an integer

# Print the list and result of the sum of the list
print(f"The sum of {numbers} is: {sum(numbers)}")