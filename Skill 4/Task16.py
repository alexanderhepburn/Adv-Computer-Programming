## Skill 4, Task 16: Debug a program: array
## Description:
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

#In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method.

# Create 3 lists: numbers, strings and names

numbers = []
strings = []
names = []

# Add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable

numbers.extend([1, 2, 3])
strings.extend(["hello", "world"])

# Add names John, Eric and Jessica to strings list

names.extend(["John", "Eric", "Jessica"])

#Create a new variable third_name with the third name taken from names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

third_name = names[2]

# At the end print all lists and one variable created.

print(f"Here are all the variables \n numbers: {numbers} \n strings: {strings} \n names: {names} \n third_name: {third_name}")