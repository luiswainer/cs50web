import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Enter an integer number")
    sys.exit(1)

try:
    print (x / y)
except ZeroDivisionError:
    print("Error /0")
    sys.exit(1)

