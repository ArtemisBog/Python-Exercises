# Write a function that takes two sorted lists and returns a single sorted list that combines both inputs.
# Example:
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]

list1 = [1, 2, 4]
list2 = [1, 3, 4]

combined_list = list1 + list2
print(combined_list)

combined_list.sort()
print(combined_list)

