## Skill 3, Task 13: Equal to each other
## Description: Collect three numbers and print 3 if they are all the same, 2 if two of them are, and 0 if they are all different
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
        try:
            numbers.append(int(input_number)) # If the input is an integer append it to the numbers list
            break # Break out of the while loop to collect the next input
        except ValueError:
            print("Only ints can be entered, please try again.") # Print an error if the input is not an integer


highest_commonality = 0 # Variable storing highest amount of commonalites

# Loop through all numbers
for num in numbers:
    same_values = 0 # Local variable storing how many values are the same
    for num2 in numbers: # Loop through the list again
        if num2 == num: # Check if the variable in the first loop is equal to the variable in the second loop
            same_values += 1 # If True add one to the same_values
    if same_values > highest_commonality and not same_values == 1: # Check if the same_values variable is higher than the highest_commonality AND that same_values is not equal to 1 (because we dont want to output 1 ONLY 0)
        highest_commonality = same_values

## As per the instructions only outputting 0, 2 or 3 without any text
print(highest_commonality)