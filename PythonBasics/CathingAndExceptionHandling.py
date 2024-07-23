try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if the exception occurs
    print("Cannot divide by zero!")

try:
    # Code that might raise different exceptions
    number = int("not a number")
    result = 10 / number
except ValueError:
    print("Cannot convert string to integer!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    # Code that might raise any exception
    result = 10 / 0
except Exception as e:
    # This will catch any exception
    print(f"An error occurred: {e}")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result is {result}")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")

try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print(e)


class NegativeValueError(Exception):
    pass


try:
    value = -10
    if value < 0:
        raise NegativeValueError("Value cannot be negative!")
except NegativeValueError as e:
    print(e)

try:
    with open("file.txt", "r") as file:
        try:
            content = file.read()
            result = int(content)
        except ValueError:
            print("File content is not a valid integer.")
except FileNotFoundError:
    print("File not found.")

try:
    with open("file.txt", "r") as file:
        content = file.read()
        result = int(content)
except (FileNotFoundError, ValueError) as e:
    print(f"Error: {e}")


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None


result = divide(10, 0)
if result is not None:
    print(f"Result is {result}")
