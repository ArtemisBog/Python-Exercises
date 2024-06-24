# Write a program that reads data from the CSV file in this folder and prints it in a tabular format.
# Output:
# Name    Age    City
# John    25    New York
# Alice    29    Chicago
# Want to learn more about CSV handling in Python? Check this out: https://realpython.com/python-csv/


import csv

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(f'\t{row[0]} {row[1]} {row[2]}')
        line_count += 1