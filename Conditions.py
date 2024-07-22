num = -5
if num == 0:
    print("Number is Zero")
elif num < 0:
    print("Negative number")
else:
    print("Positive Number")

# range() function implementation
a = range(10)
print(a)  # range(0, 10)

a = list(range(10))  # this is Exclusive
print(a)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = list(range(2, 10, 2))  # [2, 4, 6, 8] -> range(start , end , increment)
print(a)

# loop implementation
for a in range(10):
    print(a)
    print("->")  # python is space effected code
print(10000)  # this out from for loop

a = ['Anuj', 'Aman', 'Kiriti']
for name in a:
    print(name * 2)

# while loops
n = 10
while n >= 1:
    print(n)
    n -= 1

# keyword "break " , "continue"
# for i in range(10) :
#     if i > 6 :
#         break;
#      print(i)





