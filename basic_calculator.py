num1 = input("Enter a number: ")
operator = input("Insert a operator(+, -, *, /): ")
num2 = input("Enter another number: ")

add = float(num1) + float(num2)
subtract = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)

if operator == "+": 
    print(add)

elif operator == "-":
    print(subtract)

elif operator == "*":
    print(multiply)

elif operator == "/":
    print(divide)

else:
    print("Error: Invalid input.")

