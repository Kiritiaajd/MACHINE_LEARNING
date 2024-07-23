# Definition:
# A set is an unordered collection of unique elements.
# Unordered: Sets do not maintain any particular order of elements.
# Unique Elements: Sets automatically eliminate duplicate elements.
# Mutable: Elements can be added or removed from a set.
# Heterogeneous Elements: Sets can contain elements of different types.
# Hashable Elements: Elements must be immutable (e.g., numbers, strings, tuples) to be added to a set.
# No Indexing: Elements in a set cannot be accessed by index or sliced.
a = {1, 2, 3, 4, 5, 6, 7, 8}

for element in a:
    print(element * 2)

# Dictionary
# python dictionary is an unordered collection of items.
# While other compound data types have only value as an element
# , a dictionary has a key: value pair
# my_dict = {}
my_dict = {1: 'apple', 2: 'Mango', 3: 'Ball'}
print(my_dict)
print(my_dict[1])
marks = {'Aman': 99, 'Raju': 78, 'Dimple': 90}
print("Marks of aman : ", marks['Aman'])

squares = {1: 1, 2: 3, 3: 9, 4: 16, 5: 25}
for i in squares:
    print(i, " ", squares[i])

my_set = {1, 2, 3}
empty_set = set()

# Adding Elements:
my_set.add(4)
print(my_set)

# Removing Elements:
my_set.remove(2)  # Raises KeyError if the element is not present
my_set.discard(3)  # Does not raise an error if the element is not present

# Membership Test
print(1 in my_set)  # Output: True
print(5 in my_set)  # Output: False

# Set Operations:
# Union:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

#  Intersection:
print(set1 & set2)  # Output: {3}

# Difference:
print(set1 - set2)  # Output: {1, 2}

# Symmetric Difference:
print(set1 ^ set2)  # Output: {1, 2, 4, 5}

# Set Methods:
my_set.update([5, 6])  # Add multiple elements
my_set.clear()  # Remove all elements

# If you need to access elements by index or need to maintain
# the order of elements, you should use a list or a tuple
# instead of a set. However, if you still need to access
# elements in a set-like structure while maintaining the
# order, you can convert the set to a list or tuple.

# Example:
# Creating a set
my_set = {1, 2, 3, 4}

# Convert the set to a list to access elements by index
my_list = list(my_set)
print(my_list[0])  # Output: 1 (or another element, as set order is not guaranteed)

# Convert the set to a tuple to access elements by index
my_tuple = tuple(my_set)
print(my_tuple[0])  # Output: 1 (or another element, as set order is not guaranteed)

my_set = {1, 2, 3, 4}
# add(): Adds an element to the set.
my_set.add(5)
print(my_set)

# pop(): Removes and returns an arbitrary element from the set.
# Raises a KeyError if the set is empty.
element = my_set.pop()
print(element)

# copy(): Returns a shallow copy of the set.
new_set = my_set.copy()
print(new_set)

# issubset(): Checks if the set is a subset of another set.
result = set1.issubset(set2)  # Output: False
print(result)

# issuperset(): Checks if the set is a superset of another set.
result = set1.issuperset(set2)  # Output: False
print(result)
# isdisjoint(): Checks if two sets have no elements in common.
result = set1.isdisjoint(set2)  # Output: False
print(result)