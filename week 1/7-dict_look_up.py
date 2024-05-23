# Write a Python program that allows the user to look up the value 
# associated with a given key from a dictionary with some key-value pairs.

# Hint: Look up "Python dictionary" to learn about a dictionary.

simple_dict = {
    "apple": "A sweet red or green fruit",
    "banana": "A long yellow fruit",
    "orange": "A round orange fruit",
    "grape": "A small purple or green fruit"
}

key = input("Enter a fruit name to look up its description: ").lower()


if key in simple_dict.keys():
    print(simple_dict[key])

else:
    print("This fruit is unknown")