## Advanced 2: Translate english to swedish
## Description:
## Language: Python
## Author: Alexander Hepburn
## Date: 22.04.2024

"""Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"}
and use it to translate your Christmas cards from English into Swedish.
That is, write a function translate() that takes a list of English words and returns a list of Swedish words.

As output: you should have list of all swedish words
OUTPUT: ['god', 'jul', 'och', 'gott', 'nytt', 'ar']
"""

dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

def translate(lst, input_dictionary):
    swedish_words = [input_dictionary[word.lower()] for word in lst if word.lower() in input_dictionary]
    return swedish_words

def main():
    # Example input used in the assignment
    print(translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year', 'mom'], input_dictionary=dictionary))

# Call the main function to execute the code
main()
