# Write a program that takes a temperature in Celsius and converts it to Fahrenheit
# Fahrenheit equation Tf = 1.8Tc + 32


def celsius_to_fahrenheit(x):
    return (1.8 * x) + 32


temp_fahrenheit = celsius_to_fahrenheit(int(input("Enter temperature in celsius to covert to Fahrenheit: ")))
print(int(temp_fahrenheit))
