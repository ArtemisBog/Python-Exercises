# Write a function that returns a list of all prime numbers up to a given number.
# A prime number is a number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# Example:
# Input: 10
# Output: [2, 3, 5, 7]

user_number = int(input("Enter the number: "))

primes_list = []

for prime_number in range(2, user_number + 1):
    is_prime = True
    for divisor in range(2, int(prime_number ** 0.5) + 1):
        if prime_number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        primes_list.append(prime_number)


print(primes_list)
