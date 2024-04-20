## Skill 2, Task 7: Float and printing
## Description: Collect an integer or float and convert the value from Fahrenheit to Celsius
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# Create a variable to store the float
input_value = 0.0

while True:
    # Collect the integer/float (if it is an integer it will simply be converted to a float ie 3 -> 3.0) from the user
    input_float = input("Please enter a temperature in fahrenheit to be converted to celsuis (float/int): ")
    try:
        input_value = float(input_float) # cast the value to a float and see if it raises a ValueError
        break # Exit the while loop
    except ValueError:
        print("Only numbers (float or integers) can be entered, please try again.") # Print an error if the input is not correct"

# Convert from Fahrenheit to Celsius
value_in_celsius = (input_value - 32) * (5/9)

# Print the input and output rounded to 2 decimals places
print(f"{input_value} in celsuis is {value_in_celsius:.2f} (rounded to two decimal places).")
