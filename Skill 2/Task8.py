## Skill 2, Task 8: Float, int and string
## Description: Check if 3 different values are equal to "hello", 10.0 and 20
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# Create the variables
mystring = "hallo"
myfloat = 21.0
myint = 21

# Check if the variables are of the correct type
try:
    str(mystring)
    float(myfloat)
    int(myint)
except ValueError:
    # If not print an error message
    raise TypeError(f"One of the values is not of correct type. mystring should be a string (it is a {type(mystring)}), myfloat should be a float (it is a {type(myfloat)}) and myint should be an int (it is a {type(myint)}).")

# Check if mystring is a string equal to "hello"
if mystring == "hello":
    print(f"The variable mystring is equal to the value hello") # Print that it is equal
else:
    print(f"The variable mystring is not equal to the value hello (its value is {mystring}") # Print that it is not equal

# Check if myfloat is a float equal to 10.0
if myfloat == 10.0:
    print(f"The variable myfloat is equal to the value 10.0") # Print that it is equal
else:
    print(f"The variable myfloat is not equal to the value 10.0 (its value is {mystring}") # Print that it is not equal

# Check if myint is an int equal to 20
if myint == 20:
    print(f"The variable myint is equal to the value 20") # Print that it is equal
else:
    print(f"The variable myint is not equal to the value 20 (its value is {mystring}") # Print that it is not equal