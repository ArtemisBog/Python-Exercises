# Write a function that takes a list and returns a new list with duplicates removed, preserving the original order of elements.
# Example:
# Input: [1, 2, 3, 1, 2, 4]
# Output: [1, 2, 3, 4]

input_list = [1, 2, 3, 1, 2, 4]

def dupremoval(input_list):
    output_list = list(set(input_list))
    return output_list

result = dupremoval(input_list)
print(result)