# A function in Python is a reusable block of code designed
# to perform a specific task. Functions help in organizing and
# structuring code, making it more readable, maintainable, and
# reusable.

# Types of functions
# 1. Built-in -> int() ,
# 2. Module
# 3. User define

# Built-in functions :

# Module:
# A module is a file containing functions and variables defined
# in separate files. A Module is simply a file that contains Python
# code. When we break a program into modules, each module should
# contain functions that perform related tasks.
# Example

from math import cos, pi

print(cos(pi))


# User defined function
def greet():
    print('Hello , Aman')


greet()
greet()


def sum1(a, b):
    return a + b


print(sum1(10, 10))


def sum_of_list(a):
    print("Calculating .......")
    return sum(a)


a = [1, 2, 3, 4, 5, 6, 7]
print("Sum pf list is : ", sum_of_list(a))


def greet():
    print("Hello, World!")


greet()  # Output: Hello, World!


def greet(name):
    print(f"Hello, {name}!")


greet("Alice")  # Output: Hello, Alice!


def add(a, b):
    return a + b


result = add(3, 5)
print(result)  # Output: 8


def greet(name="World"):
    print(f"Hello, {name}!")


greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info(name="Alice", age=30)
# Output:
# name: Alice
# age: 30

add = lambda x, y: x + y
print(add(3, 5))  # Output: 8


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120


def square_numbers(numbers):
    return [n ** 2 for n in numbers]


numbers = [1, 2, 3, 4]
print(square_numbers(numbers))  # Output: [1, 4, 9, 16]


def apply_function(x, func):
    return func(x)


print(apply_function(5, lambda x: x ** 2))  # Output: 25
