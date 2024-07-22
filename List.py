# Python List
# IN python programming a list is created by placing all the items(elements)
#  inside a square bracket [] , separated by commas.
# It can have any number of items, and they may be of  different
#  types (String , int , float , boolean  etc.)

# It can have any number of items, and they may be different types(String , Integer , float etc.

# Example :
my_List = ["Aman", 10, 10.98, True]
print(my_List)  # python is type agnostic
print(my_List[0])
# print(my_List[10])  # ListIndex out of range
print(my_List[-1])
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(numbers[0:5])
print(numbers[0:10: 2])
print(numbers[-1:: -1])

# Slicing
numbers[2] = -2
print(numbers)
del numbers  # deleted the numbers from memory

# List Comprehension----
#  is an elegant and concise way to create a new List from
# an existing list in python.
# List comprehension consists of an expression followed by for statement
# inside square brackets.
# New_list = [expression for item in a list if condition]
# Example :
pow2 = [2 ** x for x in range(10)]
print(pow2) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

