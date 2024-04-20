## Skill 4, Task 14: Delete an element from an array
## Description: Given an array ask the user which element they would like to delete and then remove it from the array
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024




original_array = ('i', [1, 3, 5, 7, 9])
new_array = ('i', [1, 3, 5, 7, 9])

while True:
    # Collect an integer from the user
    input_number = input("Please enter a number (whole number): ")
    try:
        value_to_delete = int(input_number) - 1

        count = 0
        for row in original_array:
            for element in row:
                if count == value_to_delete:
                    print("row", row)
                    print("element", element)
                    row.remove(element)
                    break
                count += 1
        print(f"Please enter a number that is not larger than the length of the array ({count}).")
    except ValueError:
        print("Only ints can be entered, please try again.")  # Print an error if the input is not an integer

print(original_array)