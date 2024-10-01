# Task 6: Dictionaries
# Write a Python program that:
# - Creates a dictionary containing at least 3 key-value pairs where the keys are student names, andthe values are their scores.
# - Adds a new key-value pair to the dictionary for another student.
# - Updates the score of one student.
# - Prints out all the student names and their scores.

student_dict = {
    "darshan": 10,
    "om": 20,
    "dinesh": 30
}

print("student_dict: ", student_dict)

print("\nAdds a new key-value pair to the dictionary for another student.")
student_dict["paras"] = 40
print("student_dict: ", student_dict)

print("\nUpdates the score of one student.")
student_dict["darshan"] = 20
print("student_dict: ", student_dict)
