# if we do not cast n to an int, will give errors
n = int(input("Integer number: "))

if n > 0:
    print("your number is positive")
elif n < 0:
    print("it is negative")
else:
    print("it is 0")