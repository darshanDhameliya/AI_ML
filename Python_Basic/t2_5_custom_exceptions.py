# Task 5: Exception Handling with Custom Exceptions
# Write a Python program that:
# - Defines a custom exception class InvalidAgeError that is raised when an invalid age (less than 0 or greater than 150) is entered.
# - Write a function validate_age() that takes an age as input, raises InvalidAgeError for invalid ages, and prints a message if the age is valid.
# - Handle the exception with a try-except block and test with both valid and invalid age inputs.

class InvalidAgeError(Exception):
    pass

def validate_age():
    age = input("Enter a Age: ")

    age = int(age)
    if(age < 0 or age > 150):
        raise InvalidAgeError("enter age between 0 to 150")
    return age
    

try:
    age = validate_age()
    print("valid age:", age)
except InvalidAgeError as error:
    print("Custom Error(InvalidAgeError):", error)
except Exception as error:
    print("Other Error:", error)