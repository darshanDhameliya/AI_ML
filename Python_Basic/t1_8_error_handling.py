# Task 8: Error Handling
# Write a Python program that:- Attempts to divide two numbers.
# - Handles any ZeroDivisionError by printing an error message.
# - Handles any other exceptions using a generic except block and prints an appropriate message.

print("Divide Two Number")

first_number = input("Enter a First Number: ")
second_number = input("Enter a Second Number: ")

try: 
    result = float(first_number) / float(second_number)
    print(result)
except ZeroDivisionError:
    print("Error: Cloud not divide any value with 0")
except:
    print("Error: Inserted Value id Incorrect")