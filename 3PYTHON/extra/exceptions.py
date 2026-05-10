import sys

try:
     x = int(input("Enter x : "))
     y = int(input("Enter y : "))
     result = x / y
     print(f"{x} / {y} = {result}")
except ZeroDivisionError:
     print("Error: Can not divide by zero")
     sys.exit(1)
except ValueError:
     print("Invalid Input")
     sys.exit(1)

