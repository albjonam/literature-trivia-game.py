# Basic calculator for adding two numbers

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = float(num1) + float(num2)

if result == int(result):
    result = int(result)

print(result)
