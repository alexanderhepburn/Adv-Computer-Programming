## Skill 8, Task 26: Function sum of numbers
## Description: Return the sum of exactly three numbers
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

# Class to be used later for a function not being used correctly
class FunctionUsageError(Exception):
    """Exception raised for incorrect usage of a function."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

## Function: sumofthree
## Description: returns the sum of three inputs
## Input: three ints
## Returns: Int
def sumofthree(*args):
    try:
        if not len(args) == 3: # Make sure that there are exactly 3 arguments otherwise raise FunctionUsageError
            raise FunctionUsageError
        # Create a list of ints
        list_of_ints = []

        # Loop through the args
        for arg in args:
            list_of_ints.append(int(arg)) # Append them to the list of ints testing that they are an int (if they arent it will raise a TypeError

        # Return the sum of the ints
        return sum(list_of_ints)
    except FunctionUsageError:
        print(f"FunctionUsageError (sumofthree): Incorrect use of the function, exactly three arguments must be inputted ({len(args)} were inputted).")
        return 0
    except ValueError:
        print(f"ValueError (sumofthree): Only ints can be inputted.")
        return 0

# Print the output
print(f"The result of the function: sumofthree(5,3,10) is: {sumofthree(5,3,10)}")