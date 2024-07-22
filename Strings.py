# Strings - > Sequence od Characters
# Strings can be created by enclosing characters inside a single quote
# or double quotes. Even triple quotes can be used in Python but
# generally used to represent used multilines strings and docstrings

# Strings are immutable . This means that elements of string cannot be changed
# once it has been declared . we can simply re-assign different strings  to same name

name = 'Aman'
print(name)
name = "Hello My self Aman"
print(name)
name = ''' Aman!
            Hello My self Aman'''
print(name)

# Python string indexing
print("String Indexing")
word = "Hello"
print(word[0])  # -> H
print(word[-1])  # -> o
print(word[-1] == word[4])  # True

# Slicing
# Accessing characters in String(Slicing)
# We can access individual characters indexing and a range od characters using slicing
# Index starts from 0 . Trying to access a character out of index range will
# raise an IndexError. The index mist be an integer.
# Python allows negative indexing for its sequences.
# As above mentioned the index -1 refers to the last item , and -2 represents the second last item and so on.
# We can access index in a string by using the slicing operator
print(word[1:4])  # ell
print(word[:4])  # Hell
print(word[2:])  # llo
print(word[0:5:2])  # Hlo  [StartingIndex : EndingIndex : Steo]
print("reverse of string 'Hello '", word[::-1])  # reverse of string 'Hello ' olleH

# for loops in String
a = "abc"
b = "def"
print(a + b)
print(a * 2)
for i in a:
    print(i * 2)

print(a.upper())
print(a.isalpha())  # Ture
a = "12asd"
print(a.isalpha())  # True
b = "12345"
print(b.isdigit())  # True
a = "abcde"
print(a.islower())  # True
print(a.upper())  # ABCDE
a = a.upper()
print(a.islower())  # False
print(a.isupper())  # True
