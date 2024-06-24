# Write a function that merges two dictionaries into one.
# The function should take two dictionaries as input and return a single dictionary.
# If the two dictionaries have the same key, the value of the key in the second dictionary should be used.
# Example:
# Input: dict1 = {1: 'a', 2: 'b'}, dict2 = {2: 'c', 3: 'd'}
# Output: {1: 'a', 2: 'c', 3: 'd'}
# Here is how you can get a dictionary from the user:

dict1 = {}
n = int(input("First dictionary. Enter the number of elements in the dictionary: "))
for i in range(n):
    key1 = input("Enter the key: ")
    value1 = input("Enter the value: ")
    dict1[key1] = value1
print("First dictionary:", dict1)

dict2 = {}
m = int(input("Second dictionary. Enter the number of elements in the dictionary: "))
for ii in range(m):
    key2 = input("Enter the key: ")
    value2 = input("Enter the value: ")
    dict2[key2] = value2
print("Second dictionary:", dict2)

dict1.update(dict2)

print("Merged dictionary: ", dict1)



