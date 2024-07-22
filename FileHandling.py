from typing import TextIO

# Use a context manager to handle the file
with open('data.txt', 'r') as f:  # Ensure the file is opened in read mode
    print(f.readline())  # Read and print the first line
    f.seek(0)  # Move the cursor back to the beginning of the file
    print(f.read())  # Read and print the entire file content

# Write to a file
# open the file using 'w' mode. We get a file Object that can be used
#  to write strings into the file.
# fileObject.write(String)
# fieldObject.writeLines(sequence)

with open('data1.txt', 'w') as f:
    f.write("Hello Aman")

