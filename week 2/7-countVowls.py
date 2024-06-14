# Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
# Example:
# Input: "hello"
# Output: 2

user_string = str(input("Enter the string: "))
vowels = "aeiouAEIOU"

number_of_vowels = 0

for x in user_string:
    if x in vowels:
        number_of_vowels = number_of_vowels + 1

print("The number of vowels is: ", number_of_vowels)
