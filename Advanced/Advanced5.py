## Advanced 5: Reverse string
## Description: Simple program to reverse the order of words
## Language: Python
## Author: Alexander Hepburn
## Date: 23.04.2024


#Write a Python program to reverse a string word by word.

# Input string : 'hello .py'
# Expected Output : '.py hello'

class py_solution:

    ## Function: reverse_words
    ## Description: Takes a string (with words) and reverse the order of the words
    ## Input: s (str)
    ## Returns: str
  def reverse_words(self, s):
      try:
          if isinstance(s, str): # Check that the input is of type string
              list_of_words = s.split() # Split the string into a list of words
              new_list_of_words = list_of_words[::-1] # Reverse the order of the list of words
              return ' '.join(new_list_of_words) # Convert the reversed order list of words based to a string and return it
          else: # If the input is anything but string
              raise TypeError # Raise a TypeError
      except TypeError:
          print(f"TypeError (reverse_words): input s must be a string not a {type(s)}.")



def main():
    # Example input used in the assignment
    print(py_solution().reverse_words("hello .py"))

# Call the main function to execute the code
main()