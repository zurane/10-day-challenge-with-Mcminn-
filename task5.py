# Write a program that checks if a number
# entered by the user is even or odd.


def even_odd():
    num = int(input("Enter a number to check if it's an odd or even number: "))

    if num % 2 == 0:
        return "The number is even"
    elif num % 2 == 1:
        return "The number is odd"
    else:
        return "The number is neither even or odd"


print(even_odd())
