# Task 7: File Handling
# Write a Python program that:
# - Creates a text file named students.txt.
# - Writes the names of five students into the file, each on a new line.
# - Reads the file and prints its contents to the console.
import os
script_dir = os.path.dirname(__file__)

rel_path = "data_files/t7_file_handaling.txt"
file_path = os.path.join(script_dir, rel_path)

file = open(file_path, "w")
file.write("Darshan")
file.write("\nOm")
file.write("\nDinesh")
file.write("\nParas")
file.write("\nSuraj")

file.close()

#open and read the file after the overwriting:
file = open(file_path, "r")
print(file.read())