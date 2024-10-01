# Task 1: Lambda Functions and Built-in Functions
# Write a Python program that:
# - Creates a list of tuples representing the names and ages of 5 people.
# - Sorts the list of tuples based on age using a lambda function.
# - Uses the map() function to create a list of only the names from the sorted list.
# - Uses the filter() function to return a list of people whose age is greater than or equal to 30.
# - Print the final lists.

people = [
    ('darshan', 25),
    ('vivek', 20),
    ('pintal', 32),
    ('mitul', 30),
    ('dhanraj', 25),
]

sorted_people = sorted(people, key=lambda x: x[1])
print("sorted_people: ", sorted_people)

map_sorted_people = map(lambda x: x[0], sorted_people)
print("map_sorted_people: ", list(map_sorted_people))

filter_sorted_people = filter(lambda x: x[1] >= 30, sorted_people)
print("filter_sorted_people: ", list(filter_sorted_people))
