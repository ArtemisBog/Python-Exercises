# Write a Python program that asks the user for a number and prints whether it is even or odd.

# Hint: Use the modulo operator (%) to determine if a number is even or odd.

number = int(input("Enter a number: "))

if int(number%2) == 1:
    print("This number is odd")

else:
    print("This number is even")