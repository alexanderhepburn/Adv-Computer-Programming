## Skill 8, Task 27: Highest number
## Description:
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

# Class to be used later for a function not being used correctly
class FunctionUsageError(Exception):
    """Exception raised for incorrect usage of a function."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

## Function: highest_of_three
## Description: returns the highest int of three int
## Input: three ints
## Returns: Int
def highest_of_three(*args):
    try:
        if not len(args) == 3: # Make sure that there are exactly 3 arguments otherwise raise FunctionUsageError
            raise FunctionUsageError
        # Create a list of ints and check that they are all ints
        list_of_ints = map(lambda x: int(x), args)

        # Return the highest int
        return max(list_of_ints)
    except FunctionUsageError:
        print(f"FunctionUsageError (highest_of_three): Incorrect use of the function, exactly three arguments must be inputted ({len(args)} were inputted).")
        return 0
    except ValueError:
        print(f"ValueError (highest_of_three): Only ints can be inputted.")
        return 0

# Print the output
print(f"The result of the function: highest_of_three(5,3,10) is: {highest_of_three(5,3,10)}")
