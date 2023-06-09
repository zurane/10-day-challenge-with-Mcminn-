# Write a program that takes two numbers as input and
# prints their sum , difference, product, and quotient.

def nums():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    op = input("Choose an operator: +, * , -,  / , **, //\n")

    if op == "+":
        return num1 + num2
    elif op == "*":
        return num1 * num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == "**":
        return num1 ** num2
    elif op == "//":
        return num1 // num2
    else:
        return nums()


print(nums())
