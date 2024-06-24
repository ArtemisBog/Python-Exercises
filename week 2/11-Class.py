# Define a class called Person with attributes name and age.
# Add a method that prints a greeting message including the person’s name.
# Create a Person object and call the greeting method.
# Dont know how to create a class in Python? Check this link: https://www.w3schools.com/python/python_classes.asp

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print("Hello", p1.name)