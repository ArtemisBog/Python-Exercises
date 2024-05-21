# Write a Python program that creates a list of numbers,
# prints the list, and then prints the sum of the numbers in the list.

# Hint: Search for "Python list" to learn how to create a list.
# Hint: Use a for loop to iterate over the list and calculate the sum.

import random

# Creating a list of 10 integers, randed from 0 to 999
random_list=[]
n=10
for i in range(n):
    random_list.append(random.randint(0,1000))

# Printing the list
print("The list is: ", random_list)

# Printing the sum of the numbers in the list
print("The sum of numbers in the list is: ", sum(random_list))

# Calculating and printing the sum of the numbers in the list using for loop
sum = 0
for x in random_list:
    sum = sum + x
print("The sum of numbers in the list, calculated using for loop: ", sum)