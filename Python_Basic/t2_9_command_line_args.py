# Task 9: Command-line Arguments
# Write a Python program that:
# - Accepts two numbers as command-line arguments.
# - Multiplies the two numbers and prints the result.
# - Use the sys.argv list to get the command-line arguments.

import sys

print("Multiplies Two Number")


try: 
    first_number = sys.argv[1]
    second_number = sys.argv[2]
    result = float(first_number) * float(second_number)
    print(first_number,"*",second_number,"=",result)
except ZeroDivisionError:
    print("Error: Cloud not divide any value with 0")
except:
    print("Error: Inserted Value id Incorrect")
