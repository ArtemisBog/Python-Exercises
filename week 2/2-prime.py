# Write a function that returns a list of all prime numbers up to a given number.
# A prime number is a number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# Example:
# Input: 10
# Output: [2, 3, 5, 7]

list = [3]

for number in list:
    test = True
    for lesser_number in range(0, number+1):
        test = False
    print("Test result: ", test)