# Write a Python program that converts temperatures 
# from Celsius to Fahrenheit and vice versa. The user should input the temperature and the unit (C or F).

# Hint: The formula to convert from Celsius to Fahrenheit is: F = C * 9/5 + 32
# The formula to convert from Fahrenheit to Celsius is: C = (F - 32) * 5/9
# Get user input
temp = float(input("Enter temperature: "))
unit = input("Is this in Celsius or Fahrenheit? (C/F): ")

if unit == "C":
    print("The temperature in Fahrenheit is: ", temp * 9/5 + 32)
elif unit == "F":
    print("The temperature in Celsius is: ", (temp - 32) * 5/9)
else:
    print("Incorrect input")
