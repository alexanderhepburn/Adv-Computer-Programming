## Skill 4, Task 15: Append a new item to the array
## Description:
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# Create a variable to store the integer
input_value = 0

while True:
    # Collect the integer from the user
    input_int = input("Please enter an integer (whole number in the range 1-365): ")
    if input_int.isdigit() and int(input_int) > 0 and int(input_int) < 366: # Verify that the input is an integer and in the range
        input_value = int(input_int) # Cast the input to an int and set the input_value equal to the input
        break # Break out of the while loop to print the result
    else:
        print("Only ints can be entered that are in the range of 1-365, please try again.") # Print an error if the input is not correct

# Adjust the input_value to 0-365 because the week starts on a Sunday
day_value = input_value - 1

## Add 4 to the value to compensate for the fact that the year starts on a Thursday
day_value = day_value + 4

# Calculate which day of the week the value would be
day_value = day_value % 7

# Create a key-value pair for the day of the week
day_to_weekday = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

# Output the day of the week and the integer value
print(f"The day of the week for day {input_value} of the year is {day_to_weekday[day_value]} or week integer value of {day_value}")