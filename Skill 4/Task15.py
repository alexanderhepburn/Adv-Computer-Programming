## Skill 4, Task 15: Append a new item to the array
## Description: Append an item to the end of an array
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

#Starting list as per assignment
i = [1, 3, 5, 7, 9]

while True:
    # Collect an integer from the user
    print(f"Array: i is currently: {i}")
    input_number = input("Please enter an int you would like to add to the list: ")
    try:
        value_to_add = int(input_number) # Check that value is an int

        i.append(value_to_add) # Add to the end of the list
        print(f"Added: {input_number}, array now is: {i}!") # Print the added int and new list
        break # Exit the while loop
    except ValueError:
        print("Only ints can be entered, please try again.")  # Print an error if the input is not an integer