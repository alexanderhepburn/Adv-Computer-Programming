## Skill 5, Task 17: Count words
## Description: Count the amount of words and 'i's given an input
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# While loop in case of Value Error
while True:
    # Collect the sentence from the user
    string_input = input("Please enter a sentence: ")
    try:
        string_length = len(string_input.split(" ")) # Calculate the length of the sentence
        string_count_i = string_input.count("i") # Calculate the amount of 'i's

        # Print the output to the console
        print("You entered: ", string_input)
        print(f"The string has {string_length} words.")
        print(f"The string has {string_count_i} 'i's.")
        break
    except ValueError:
        print("Please enter a sentence, there was something wrong with your input.") # Print an error if a ValueError is raised

