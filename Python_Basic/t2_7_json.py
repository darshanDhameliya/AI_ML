# Task 7: Working with JSONWrite a Python program that:
# - Creates a dictionary with details about a book, including title, author, and year published.
# - Converts the dictionary to a JSON string using the json module and writes it to a file named book.json.
# - Reads the JSON string back from the file and converts it back to a Python dictionary.
# - Print both the JSON string and the final dictionary.

import json
import os

script_dir = os.path.dirname(__file__)

rel_path = "data_files/t7_json.json"
file_path = os.path.join(script_dir, rel_path)


book_dict = {
  "brand": "Rich Dad Poor Dad",
  "author": "Robert Kiyosaki",
  "published year": 1997,
}

# # First way
# json_data = json.dumps(book_dict, indent=4)
# file = open(file_path, "w")
# file.write(json_data)
# file.close()

# file_data = open(file_path, "r")
# file_data_dict = json.load(file_data)
# print(file_data_dict)
# print(type(file_data_dict))
# file_data.close()

# Second way
with open(file_path, 'w') as file:
    json.dump(book_dict, file)

with open(file_path) as file_data:
    file_data_dict = json.load(file_data)
    print(file_data_dict)
    print(type(file_data_dict))