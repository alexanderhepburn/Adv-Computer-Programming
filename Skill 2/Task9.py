## Skill 2, Task 9: Debug a program so it works
## Description: Debug the given code so that it works
## Language: Python
## Author: Alexander Hepburn
## Date: 20.04.2024

# Code so that the program will not raise any errors:
mystring = "hello"
myfloat = 10.0
myint = 20

# Code from the assignment
if mystring == "hello": # Needed == instead of =
    print(f"String: {mystring}") # Changed to printf

if isinstance(myfloat, float) and myfloat == 10.0: # Needed == instead of =
    print(f"Float: {myfloat}") # Changed to printf

if isinstance(myint, int) and myint == 20: # Needed == instead of =
    print(f"Integer: {myint}") # Changed to printf