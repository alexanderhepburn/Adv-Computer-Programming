## Skill 8, Task 28: Modify the program
## Description:
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# List of integers to be collected
numbers = []

# For loop to collect two integers from the user
for i in range(2):
    while True:
        # Collect an integer from the user
        input_number = input("Please enter a number (non-zero whole number): ")
        try:
            if not int(input_number) == 0: # Check that the inputed value is not a zero
                numbers.append(int(input_number)) # If the input is an integer append it to the numbers list
                break # Break out of the while loop to collect the next input
            else:
                print("Only non-zero integers can be entered, please try again.") # Print an error if the input is a zero
        except ValueError:
            print("Only ints can be entered, please try again.") # Print an error if the input is not an integer


# Create a variable with how many inputs are positive (first a lambda function is performed on the list to return a list of True and False and then the Trues are counted and returned as an int).
positive_number = list(map(lambda x: x > 0, numbers)).count(True)

# Check how many positives, if only one that print YES and otherwise NO as per assignment instructions
if positive_number == 1:
    print("YES")
else:
    print("NO")
