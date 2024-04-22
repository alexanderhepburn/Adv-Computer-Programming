## Advanced 5: Reverse string
## Description:
## Language: Python
## Author: Alexander Hepburn
## Date: 22.04.2024


#Write a Python program to reverse a string word by word.

# Input string : 'hello .py'
# Expected Output : '.py hello'

class py_solution:

  def reverse_words(self, s):
      # test of str
      try:
          if isinstance(s, str):
              list_of_words = s.split()
              new_list_of_words = list_of_words[::-1]
              return ' '.join(new_list_of_words)
          else:
              raise TypeError
      except TypeError:
          print(f"TypeError (reverse_words): input s must be a string not a {type(s)}.")



def main():
    print(py_solution().reverse_words("hello .py"))

main()