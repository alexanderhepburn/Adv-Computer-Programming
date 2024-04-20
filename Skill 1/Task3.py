## Skill 1, Task 3: Read an integer and print previous/next
## Description: Collect an integer and print the previous and next integer
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# Create a variable to store the integer
input_value = 0

while True:
    # Collect the integer from the user
    input_int = input("Please enter an integer (whole number): ")
    if input_int.isdigit(): # Verify that the input is an integer
        input_value = int(input_int) # Cast the input to an int and set the input_value equal to the input
        break # Break out of the while loop to print the result
    else:
        print("Only ints can be entered, please try again.") # Print an error if the input is not correct

# Output the next and previous number to the user
print(f"The next number for the number {input_value} is {input_value+1}")
print(f"The previous number for the number {input_value} is {input_value-1}")