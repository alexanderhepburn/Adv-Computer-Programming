## Skill 4, Task 14: Delete an element from an array
## Description: Given an array ask the user which element they would like to delete and then remove it from the array
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

#Starting list as per assignment
i = [1, 3, 5, 7, 9]

while True:
    # Collect an integer from the user
    print(f"Array: i is currently: {i}")
    input_number = input("Please enter which element you would like to delete (starting with index=1): ")
    try:
        value_to_delete = int(input_number) - 1 # Test if value is an int otherwise ValueError will be thrown
        if value_to_delete < 0 or value_to_delete > (len(i)-1): # Test that int is inbounds otherwise KeyError will be thrown
            raise KeyError

        del i[value_to_delete] # Delete requested value
        print(f"Removed index: {input_number}, array now is: {i}!") # Print the removed index and new array
        break # Exit the while loop (could remove this to allow infinite deletion
    except ValueError:
        print("Only ints can be entered, please try again.")  # Print an error if the input is not an integer
    except KeyError:
        print(f"Please enter an index within the range of (1, {len(i)}).") # Error message for KeyError