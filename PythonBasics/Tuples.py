# Tuples ----->
# Immutable sequence type
# Defined with parentheses ()
# Access elements via indexing
# Maintain order
# Can contain heterogeneous elements
# Fixed size
# Hashable (can be used as dictionary keys and set elements)
# More memory-efficient and faster to iterate over than lists
# Support nested tuples
# Methods: count() and index()

s = "Aman"
# s[0] = M # Not applicable
a = ('A', 'B', 'C', 'D')
# a[0] = 's' -> Not applicable in tuple
# Traceback (most recent call last):
#   File "C:\Python\Tuples.py", line 5, in <module>
#     a[0] = 's'
#     ~^^^
# TypeError: 'tuple' object does not support item assignment
a = list(a)
print(a)  # ['A', 'B', 'C', 'D']
# tuples can be converted into a list
a = tuple(a)
print(a)  # ('A', 'B', 'C', 'D')
# list can be converted into a list
print(a.count('A'))

# Indexing: Access elements by their index.
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print(my_list[0])  # Output: 1
print(my_tuple[0])  # Output: 1

# Slicing: Extract a portion of the list or tuple.
print(my_list[1:3])  # Output: [2, 3]
print(my_tuple[1:3])  # Output: (2, 3)

# Concatenation: Combine two lists or tuples.
print(my_list + [4, 5])  # Output: [1, 2, 3, 4, 5]
print(my_tuple + (4, 5))  # Output: (1, 2, 3, 4, 5)

# Repetition: Repeat the elements.
print(my_list * 2)  # Output: [1, 2, 3, 1, 2, 3]
print(my_tuple * 2)  # Output: (1, 2, 3, 1, 2, 3)

# Membership Test: Check if an element is in the list or tuple
print(2 in my_list)  # Output: True
print(2 in my_tuple)  # Output: True

# Length: Get the number of elements.
print(len(my_list))  # Output: 3
print(len(my_tuple))  # Output: 3

# Iteration: Loop through elements.
for item in my_list:
    print(item)  # Output: 1 2 3

for item in my_tuple:
    print(item)  # Output: 1 2 3

# Count: Count the number of occurrences of a value.
print(my_list.count(2))  # Output: 1
print(my_tuple.count(2))  # Output: 1

# Index: Find the index of the first occurrence of a value.
print(my_list.index(2))  # Output: 1
print(my_tuple.index(2))  # Output: 1
