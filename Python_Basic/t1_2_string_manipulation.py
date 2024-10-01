# Task 2: String Manipulation
# Given the string "Python programming is fun!", write a Python script that:
# - Converts the string to uppercase.
# - Replaces the word "fun" with "powerful".
# - Slices the string to print only the word "programming".
# - Prints the length of the original string.

string = "Python programming is fun!"

print("Upper: ", string.upper())

print("Replace: ", string.replace("fun", "powerful"))

print("Slices: ", string[7:18])

print("Length: ", len(string))