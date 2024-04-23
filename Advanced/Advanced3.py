## Advanced 3: Improved translator
## Description: More complex program for translating with a console interface
## Language: Python
## Author: Alexander Hepburn
## Date: 22.04.2024

""" You should now improve the previous translator by asking user 2 options:
1) Enter a new word into the dictionary
(when user enters new word then you should also ask for the swedish translation and add both words to the list) or
2) Translate user's input example: user says 'Merry' OUTPUT: god """

# dictionary given by the assignment
dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

## Function: translate
## Description: A console based application that allows the user to enter a new or translate an existing english word to a swedish word
## Input: dictionary (key-value english-swedish dictionary
## Returns: None
def translate(dictionary):
  print(f"Welcome to the Translator program!") # Welcome message
  while True: # While loop so that the user can enter as my commands as they want
    try:
      # Check that the input dictionary is a key-value string only dictionary
      if not all(isinstance(value, str) for value in dictionary.values()):
        raise TypeError # If not raise TypeError

      command = input(f"Please enter new (to enter a new english word) or translate (to translate an exciting word): ") # Ask for two commands from the user
      if command == "new": # if command is new
        english_word = input(f"Please enter a new english word: ") # Get the english word

        if english_word in dictionary: # Make sure that the english word is not in the dictionary
          print(f"{english_word} is already in the database!") # Print error
        else: # if english word is not in the dictionary
          swedish_word = input(f"Please enter the swedish word for your input ({english_word}): ") # Ask for the swedish word for the english word
          dictionary[english_word] = swedish_word # Add both words to the dictionary
          print(f"Success! The translation of {english_word} being {swedish_word} was added to the list!") # Confirm it to the user

      elif command == "translate": # if command is translate
        english_word = input(f"Please enter an english word: ") # Ask for the english word

        if english_word in dictionary: # Check that it is in the dictionary
          print(f"The translation of: {english_word} is {dictionary[english_word]}") # Print the translation to the user
        else: # Word is not in the dictionary
          print(f"Invalid word: {english_word}. Please enter it into the database using the command enter.") # Tell the user to enter the word

      else: # if command is neither translate nor new
        print(f"Invalid input: {command}. Input must either be new or translate, please try again!") # Tell the user that they must enter the correct input
    except TypeError:
      print(f"TypeError (translate): The input dictionary must only contain str values. Program shutting down, please fix the input dictionary!") # Type Error when dictionary is not all strings
      return None # Return because the program will not work

def main():
  translate(dictionary) # Call the translate function

# Call the main function to execute the code
main()