# Write a program that reads the text file in this folder called text.txt and prints the number of words in it.
#  If you dont know how to read a file in Python, you can refer to this https://www.w3schools.com/python/python_file_handling.asp

file = open("text.txt")
contents = file.read()
file.close()

word_list = contents.split()
number_of_words = len(word_list)

print("Number of words:", number_of_words)
