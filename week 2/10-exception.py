# Write a program that asks for two inputs from the user.
# The program should then divide the first input by the second input.
# If the result is an integer, the program should print the result.
# If the result is not an integer, the program should raise an exception and print "The result is not an integer".
# Check the following link to know how to raise an exception in Python: https://www.w3schools.com/python/python_try_except.asp


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    result = first_number / second_number
    if not result % 1 == 0:
        raise Exception("The result of division is NOT an integer")
    else:
       print("The result of division is an integer")
except Exception as e:
    print(e)




#if result % 1 != 0:
#  raise Exception("The result of division is NOT an integer")
#else:
#    print("The result of division is an integer")


#if result % 1 != 0:
#    print("The result of division is NOT an integer")
#else:
#    print("The result of division is an integer")