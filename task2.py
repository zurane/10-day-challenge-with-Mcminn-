# Write a program that calculates the area of a rectangle using user-provided length and width To make the programme
# flexible, I converted the step by step formula to calculate the area of a rectangle into a reusable block of code (
# Function) which takes no args but prompts the user for the width and length of their shape, performs the calculation
# and returns the value back to the user
def rect_total_area():
    rect_width = int(input("Enter the width of the rectangle: "))
    rect_length = int(input("Enter the length of the rectangle: "))
    return rect_length * rect_width


# The value or output of the function is printed inside a
# formatted string which is prefixed by the letter f and followed by a string.
# The variable total carries the output returned by the function.
# and is nested inside the formatted string inside the curly braces
total = rect_total_area()
print(f"The total Area of your Rectangle is : {total} ")
