# Write a function that prints the first n Fibonacci numbers.
# Where n is the user input.
# Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding ones.
# Example: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# So if the user inputs 10, the output should be:
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

n = int(input("n = "))

fibonacci_numbers = []

if n == 0:
    fibonacci_numbers = fibonacci_numbers
elif n == 1:
    fibonacci_numbers = [1]
elif n >= 2:
    fibonacci_numbers = [1, 1]
    for x in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[x-1] + fibonacci_numbers[x-2])

print("The Fibonacci numbers up to n: ", fibonacci_numbers)