# Python List
# IN python programming a list is created by placing all the items(elements)
#  inside a square bracket [] , separated by commas.
# It can have any number of items, and they may be of  different
#  types (String , int , float , boolean  etc.)
from typing import List

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
print(pow2)  # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# a: list[int] = [x for x in range(100) if x % 2 == 0]
# print(a)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28,
# 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56,
# 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84,
# 86, 88, 90, 92, 94, 96, 98]


# List Functions
a = [1, 2, 3]
print(a)
a.append(4)
print(a)
a.insert(0, 0)
print(a)
a.insert(2, 0.5)
print(a)
a.clear()
print(a)
a = [2, 3, 1, 5, 7, 8, 3, 5, 9]
print(a)
a.sort()
print("Sorted a :")
print(a)
a = ["Apple ", "AAman", "Zoo", "Umbrella"]
print(a)
a.sort()
print("Sorted : ")
print(a)
a.pop(0)
print(a)
a = [2, 3, 1, 5, 7, 8, 3, 5, 9]
a.sort()
print(len(a))
a.pop()
print(a)
a.append(10)
print(a)
print("Maximum of 'a'")
print(max(a))
print("Minimum of 'a'")
print(min(a))
print("Sum of list ")
print(sum(a))
print(list(a))

# for loops in a list
a = [2, 3, 1, 5, 7, 8, 3, 5, 9]
for element in a:
    print(element * 2, end=" ")
