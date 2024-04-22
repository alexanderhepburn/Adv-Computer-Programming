## Advanced 4: Is member of?
## Description:
## Language: Python
## Author: Alexander Hepburn
## Date: 22.04.2024

"""Write a function is_member() that takes a value i.e. a number, string, etc) x and a
list of values a, and returns True if x is a member of a, False otherwise.
(Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python
did not have this operator.)"""

def is_member(ele, lst):
    # Finde raus of str int float
    # und ob array und elemente gleich sind!

    return None

#test
print (is_member("e", ['a', 'e', 'i', 'o', 'u']))
print (is_member(19, [1,3,4,6,18,20]))

print (is_member('right', ['wrong', 'list', 'to', 'search']))
print (is_member('panda', ['lion', 'zebra', 'elephant', 'panda']))