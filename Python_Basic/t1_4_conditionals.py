# Task 4: Conditionals
# Write a Python program that:
# - Asks the user for their age using input().- Checks if the age is greater than or equal to 18 and prints a message based on whether the user is an adult or not.
# - Add error handling to ensure the user enters a valid number.

age = input("Enter your Age: ")

try:
    age = int(age)
    if(age <= 0):
        raise Exception("Invalid Age")
    if(age >= 18):
        print("Adult")
    else:
        print("Not Adult")
except:
    print("Age value is Incorrect: ", age)