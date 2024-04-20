## Skill 3, Task 11: Print the least integer
## Description: Collect two integers and print the lower one of the two
## Language: Python
## Author: Alexander Hepburn

# List of integers to be collected
numbers = []

# For loop to collect two integers from the user
for i in range(2):
    while True:
        # Collect an integer from the user
        input_number = input("Please enter a number (whole number): ")
        try:
            numbers.append(int(input_number)) # If the input is an integer append it to the numbers list
            break # Break out of the while loop to collect the next input
        except ValueError:
            print("Only ints can be entered, please try again.") # Print an error if the input is not an integer

# Print both inputs and which one is lower using the min function
print(f"The lower number out of {numbers} is: {min(numbers)}!")