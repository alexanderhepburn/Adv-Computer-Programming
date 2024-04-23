## Advanced 2: Translate english to swedish
## Description: Simple program to translate a list from english to swedish
## Language: Python
## Author: Alexander Hepburn
## Date: 23.04.2024

"""Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"}
and use it to translate your Christmas cards from English into Swedish.
That is, write a function translate() that takes a list of English words and returns a list of Swedish words.

As output: you should have list of all swedish words
OUTPUT: ['god', 'jul', 'och', 'gott', 'nytt', 'ar']
"""
# dictionary from the exercise
dictionary = {"merry": "god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

## Function: translate
## Description: Takes a list and dictionary and translates all english words from the list based on the english-swedish dictionary (if it is not found None is returned for the word)
## Input: lst (List[str]), input_dictionary ({str: str})
## Returns: List[str or None]
def translate(lst, input_dictionary):
    try:
        all_dictionary_str = all(isinstance(value, str) for value in input_dictionary.values()) # Bool to check if all elements of the input dictionary are strings
        all_list_str = all(isinstance(item, str) for item in lst) # Bool to check if all elements of the list are strings

        if not all_dictionary_str or not all_list_str: # If not all inputs have string elements
            raise TypeError  # If not raise TypeError

        input_dictionary = {key.lower(): value.lower() for key, value in input_dictionary.items()} # Convert all key-value to lower case
        swedish_words = [] # Create an empty list with the swedish words

        for word in lst: # Iterate over the list
            if word.lower() in input_dictionary: # If the english word is in the input_dictionary (corrected to lower case)
                swedish_words.append(input_dictionary[word.lower()]) # Append the swedish word
            else: # If the english word is not in the input_dictionary
                swedish_words.append(None) # Append None because the word is not found
        return swedish_words # Return the list of swedish words to the user
    except TypeError: # If TypeError is raised
        print(f"TypeError (translate): input lst and input_dictionary must only contain str.")  # Print helpful information to the console
        print(f"lst types: {[type(x) for x in lst]} and input_dictionary types: {list(map(lambda pair: (type(pair[0]), type(pair[1])), zip(input_dictionary.keys(), input_dictionary.values())))}.") # Print all the types to the console
def main():
    # Example input used in the assignment
    print(translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year', 'mom'], input_dictionary=dictionary))

# Call the main function to execute the code
main()
