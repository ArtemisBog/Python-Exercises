# Write a Python program that prints the multiplication table for a given number.
# The user should input the number, and the program should print the table from 1 to 10.

# Hint: The output should look like this if the user enters 5:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# ...

number = int(input("Enter a number: "))

list = [1,2,3,4,5,6,7,8,9,10]
for n in list:
    print(number, "x", n, "=", number * n)