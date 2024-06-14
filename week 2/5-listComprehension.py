# Write a program that uses list comprehension to create a list of the squares of the numbers from 1 to 10.
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Here I dont want you to take an input from the user. Just create a list of squares of numbers from 1 to 10 using list comprehension.
# If you need to revise list comprehension, you can refer to this https://www.w3schools.com/python/python_lists_comprehension.asp

list = []

for number in range(1,11):
    list.append(number**2)

print(list)