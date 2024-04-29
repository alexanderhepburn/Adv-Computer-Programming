## Skill 8, Task 28: Modify the program
## Description: Add input functionality
## Language: Python
## Author: Alexander Hepburn
## Date: 29.04.2024

# Function received from assignment
def my_function_with_args(username, greeting):
   print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

# Function received from assignment
def sum_two_numbers(a, b):
   return a + b

# Code received from assignment
my_function_with_args("John Doe", "a great year!")

# Two variables storing ints to be used later
input_1 = 0
input_2 = 0

# While loop to continue until both inputs have been received in correct Type (int)
while True:
   try:
      input_1 = int(input("Please input one number (only ints):")) # First input variable
      input_2 = int(input("Please input another number (only ints): ")) # Second input variable
      break # If this line is reached both variables (input_1 and input_2) have been received and have been casted succesfully to int
   except ValueError:
      print("TypeError: Only ints are allowed!") # Input 1 or 2 was not an int therefore give error message to the user
      print("Please start over!")

# Code received from assignment
x = sum_two_numbers(input_1,input_2)

print(f"The function sum_two_numbers with argument 1, 2 outputs: {x}")
