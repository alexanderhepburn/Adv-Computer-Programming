## Advanced 3: Improved translator
## Description:
## Language: Python
## Author: Alexander Hepburn
## Date: 22.04.2024

""" You should now improve the previous translator by asking user 2 options:
1) Enter a new word into the dictionary
(when user enters new word then you should also ask for the swedish translation and add both words to the list) or
2) Translate user's input example: user says 'Merry' OUTPUT: god """

dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

def translate(lst):

#test
  print (translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year', 'mom']))