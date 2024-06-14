# Write a function to calculate the factorial of a given number.
# Factorial is the product of an integer and all the integers below it;
# Example: The factorial of 4 is 4*3*2*1 = 24


number = int(input("Enter the number: "))

def factorial(number):
    f = 1
    for any_number in range(1, number + 1):
        f *= any_number
    return f

factorial_result = factorial(number) 
print(factorial_result)