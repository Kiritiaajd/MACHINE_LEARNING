#value = input('Plear Enter the value ')
#print(value)
#x = int(input("Enter the Number"))
#print(x)
import sys

print(sys.maxsize)
large_number = sys.maxsize + 1
print(large_number)

a = 5
b = 3
print("sum")
print(a + b)
print("sub")
print(a - b)
print("mul")
print(a * b)
print("div")
print(a / b)

print("Modulo")
print(a % b)
print("div (like int ) ")
print(a // b)
print("pow")
print(a ** b)
print("test")
print(int(a / b))
print("formated float")
print("{:.2f}".format(a / b))

print("AAssignment Operators")
a = 6
a += 5
print(a)

b = 6
b += 1  # same  we can do for division , multiplication , subtraction
print("a =", a)
print("b = ", b)
print("a > b ->", a > b)
print("a < b ->", a < b)
print("a == b ->", a == b)
print("a!=b->", a != b)

x = True
y = False
print("x ", x)
print("y ", y)
print("X and Y ->", x and y)
print("X or Y ->", x or y)

# Input in python
name = input()
print(name)

a = input()
b = input()
print(a + b)  # concatenation of the string because input()
# always takes string as input for input we use int in input
a = int(input("Enter the integer 'a'"))
b = int(input("Enter the integer 'b'"))
print(a * b)

# practice input
english_marks = int(input("Enter English marks : "))
maths_marks = int(input("Enter Maths marks : "))
sci_marks = int(input("Enter the Science marks :"))
total = english_marks + maths_marks + sci_marks
print("Total marks : ", total)
print("Average marks : {:.2f}".format(total /3))
