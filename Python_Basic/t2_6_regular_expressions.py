# Task 6: Regular Expressions
# Write a Python program that:
# - Prompts the user to input an email address.
# - Uses a regular expression to validate if the entered email address follows the format:[username]@[domain].[extension] (e.g., user@example.com).
# - Print a message indicating whether the email is valid or not.
# - Use the re module to implement the regular expression.

import re

email = input("Enter Email:")
valid_email = re.search("^.*@.*\..*$", email)

if valid_email:
    print("Email is Valid")
else:
    print("Email is InValid")