## Skill 10, Task 32: Read from a file
## Description: Read and print from the previously created file
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

# file_name from the previous assignment
file_name = "hello.txt"

# Open the file for reading
with open(file_name, "r") as fh:
    # Read the lines of text from the file
    print(f"Successfully opened the file: {file_name}! The file contains: ")
    lines = fh.readlines()
    for n, line in enumerate(lines): # Using the enumerate to get the value and index of the line
        print(f"Line {n+1}: {line}", end="") # Printing the line number (plus one as python starts at 0) with the text and removing the line break
    fh.close() # Close file after finished
