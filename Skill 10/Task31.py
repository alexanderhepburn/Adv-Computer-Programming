## Skill 10, Task 31: Write to a file
## Description: Write three lines to a file named hello.txt
## Language: Python
## Author: Alexander Hepburn
## Date: 21.04.2024

# file_name to write
file_name = "hello.txt"

# As per instructions the rows to write
rows_to_write = ["a line of text", "another line of text", "a third line"]

# Open the file for writing
with open(file_name, "w") as fh:
    # Write the lines of text to the file
    for row in rows_to_write:
        fh.write(f"{row}\n")
    fh.close() # Close file after finished
    print(f"Successfully created the file: {file_name} and wrote to it!")
