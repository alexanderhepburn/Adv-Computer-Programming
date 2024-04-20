## Skill 5, Task 18: Replace the string
## Description:
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# While loop in case of Value Error
while True:
    # Collect the equation from the user
    string_input = input("Please enter the following equation (1+1=2): ")
    try:
        if string_input == "1+1=2":
            string_input = string_input.replace("1", "one") #Replacing 1 with one

            # As per the instructions only outputting the value one+one=2
            print(string_input)
            break
        else:
            print("You have to enter the following equation (1+1=2), please try again.")  # As per the instructions: 1+1=2 as to be entered
    except ValueError:
        print("Please enter the equation as shown.") # Print an error if a ValueError is raised

