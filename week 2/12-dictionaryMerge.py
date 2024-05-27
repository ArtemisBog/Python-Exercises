# Write a function that merges two dictionaries into one.
# The function should take two dictionaries as input and return a single dictionary.
# If the two dictionaries have the same key, the value of the key in the second dictionary should be used.
# Example:
# Input: dict1 = {1: 'a', 2: 'b'}, dict2 = {2: 'c', 3: 'd'}
# Output: {1: 'a', 2: 'c', 3: 'd'}
# Here is how you can get a dictionary from the user:
dict1 = {}
n = int(input("Enter the number of elements in the dictionary: "))
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dict1[key] = value
print(dict1)