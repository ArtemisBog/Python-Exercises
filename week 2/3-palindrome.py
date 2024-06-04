# Write a function that checks if a given string is a palindrome. If it is - return True, otherwise return False.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
# Example of palindromes: "madam", "racecar", "level", "radar", "civic".


user_string = str(input("Enter the string: "))

reversed_string = user_string[::-1]

if user_string == reversed_string:
    print ("This is a palindrome")
else:
    print("This is NOT a palindrome")
    print("The string backwards is: ", reversed_string)