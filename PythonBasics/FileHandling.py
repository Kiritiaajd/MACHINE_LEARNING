from typing import TextIO
import csv
import json

# 1. Reading from a file
print("Reading the first line and then the entire content of 'data.txt':")
with open('data.txt', 'r') as f:
    print(f.readline())  # Read and print the first line
    f.seek(0)  # Move the cursor back to the beginning of the file
    print(f.read())  # Read and print the entire file content

# 2. Writing to a file
print("\nWriting 'Hello Aman' to 'data1.txt':")
with open('data1.txt', 'w') as f:
    f.write("Hello Aman")

# Reading the content of 'data.txt'
print("\nReading the entire content of 'data.txt':")
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading 'data.txt' line by line
print("\nReading 'data.txt' line by line:")
with open('data.txt', 'r') as file:
    for line in file:
        print(line, end='')

# Writing to 'data1.txt'
print("\n\nWriting multiple lines to 'data1.txt':")
with open('data1.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# Appending to 'data.txt'
print("\nAppending a new line to 'data.txt':")
with open('data.txt', 'a') as file:
    file.write("Appending a new line.\n")

# 3. Reading and Writing Binary Files
# Reading a binary file (like an image)
try:
    with open('image.png', 'rb') as file:
        content = file.read()
        print("\nBinary content of 'image.png':", content)
except FileNotFoundError:
    print("\n'image.png' not found. Please ensure the file exists.")

# Writing to a binary file
try:
    with open('image_copy.png', 'wb') as file:
        file.write(content)
except Exception as e:
    print("An error occurred while writing to 'image_copy.png':", e)

# 4. Using seek and tell
print("\nUsing seek and tell methods on 'data.txt':")
with open('data.txt', 'r') as file:
    print(file.readline())  # Read the first line
    print("Current position:", file.tell())  # Get the current position
    file.seek(0)  # Move the pointer back to the beginning
    print(file.readline())  # Read the first line again

# 5. Handling File Exceptions
print("\nHandling exceptions for file operations:")
try:
    with open('data.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file was not found.")
except IOError:
    print("An error occurred while reading the file.")

# 6. Working with CSV Files
# Reading from a CSV file
print("\nReading from 'data.csv':")
try:
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("'data.csv' not found. Please ensure the file exists.")

# Writing to a CSV file
print("\nWriting to 'data.csv':")
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])

# 7. JSON File Handling
# Reading from a JSON file
print("\nReading from 'data.json':")
try:
    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)
except FileNotFoundError:
    print("'data.json' not found. Please ensure the file exists.")

# Writing to a JSON file
print("\nWriting to 'data.json':")
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

with open('data.json', 'w') as file:
    json.dump(data, file)
