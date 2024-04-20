## Skill 2, Task 6: Intro to float
## Description: Collect a float, check that it is a float and print if it is over or under 100
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# Create a variable to store the float
input_value = 0.0

## Function: is_float
## Description: checks if a value is a float and that there is at least one decimal
def is_float(num):
    try:
        float(num) ## cast the value to a float and see if it raises a ValueError
        if "." in str(num) and len(num.split(".")[1]) > 0: # check if there is a decimal point and that there is at least one value behind the decimal
            return True # return that the value is a float
        else:
            return False # return that the value is not a float
    except ValueError:
        return False # return that the value is not a float


while True:
    # Collect the float from the user
    input_float = input("Please enter a float (decimal number with at least one decimal): ")
    if is_float(input_float): # Verify that the input is a float with our helper method
        input_value = float(input_float) # Set the input_value equal to the input
        break # Break out of the while loop to print the result
    else:
        print("Only floats with at least one decimal can be entered, please try again (example 3.0).") # Print an error if the input is not correct

# Check if the float is under or over 100
if input_value < 100:
    print(f"Your number ({input_value}) is smaller than 100.") # Print that it is under
else:
    print(f"Your number ({input_value}) is higher than 100.") # Print that it is over
