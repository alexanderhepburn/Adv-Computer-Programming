## Advanced 4: Is member of?
## Description: Simple program to check if an element of AnyType is an element of a List[AnyType]
## Language: Python
## Author: Alexander Hepburn
## Date: 23.04.2024

"""Write a function is_member() that takes a value i.e. a number, string, etc) x and a
list of values a, and returns True if x is a member of a, False otherwise.
(Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python
did not have this operator.)"""

## Function: is_member
## Description: Takes an element and a list of elements (all types must be the same) and returns True (False) if the element is (not) in the list
## Input: ele (Any), lst (Any)
## Returns: Boolean (True or False)
def is_member(ele, lst):
    try:
        first_type = type(lst[0]) # Get the first type of the array
        same_type = all(isinstance(x, first_type) for x in lst) # compare all types of the list to the first and return if all are the same or not

        # Check if the list contains the same type and that the array is the same type as ele
        if same_type and first_type == type(ele):
            for item in lst: # For list over each element in the list
                if item == ele: # Test if the item is the same as the input ele
                    return True # Return true if it is the case
            return False # Return false after the for-loop as gone through all items (as none were True)
        else:
            raise TypeError # If the types are not the same raise a TypeError
    except TypeError:
        print(f"TypeError (is_member): input lst and ele must be all the same type.") # Print helpful information to the console with all the types
        print(f"lst type: {[type(x) for x in lst]} and ele type: {type(ele)}.")


#test
print (is_member("e", ['a', 'e', 'i', 'o', 'u']))
print (is_member(19, [1,3,4,6,18,20]))

print (is_member('right', ['wrong', 'list', 'to', 'search']))
print (is_member('panda', ['lion', 'zebra', 'elephant', 'panda']))