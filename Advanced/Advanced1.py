## Advanced 1: Filter long words
## Description: Simple program to filter words based on the length
## Language: Python
## Author: Alexander Hepburn
## Date: 22.04.2024

## Function: filter_my_words
## Description: Takes a string (with words) and a max number of characters as an int and returns all words that are covert n as a string
## Input: input_words (str), n (int)
## Returns: str
def filter_my_words(input_words, n):
    try:
        if isinstance(input_words, str) and isinstance(n, int): # Check that the type is correct
            list_of_words = input_words.split() # Convert  input_words to a list
            filtered_words = list(filter(lambda word: len(word) > n, list_of_words)) # Filter the list to only words that are greater than n and convert the filter to a list
            return ' '.join(filtered_words) # Return the list as a string as shown in the instructions
        else:
            raise TypeError
    except TypeError:
        if not isinstance(input_words, str): #If TypeError was raised because of input_words
            print(f"TypeError (filter_my_words): input input_words must be a string not a {type(input_words)}.") # Detailed message to the console
        elif not isinstance(n, int): #If TypeError was raised because of n
            print(f"TypeError (filter_my_words): input n must be a string not a {type(n)}.") # Detailed message to the console

def main():
    # Example input used in the assignment
    print(filter_my_words("school education management", 8)) # Execute function and print returned results

# Call the main function to execute the code
main()