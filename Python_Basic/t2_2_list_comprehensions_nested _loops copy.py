# Task 2: List Comprehensions and Nested Loops
# Write a Python program that:
# - Uses a list comprehension to create a list of all even numbers from 1 to 100.
# - Uses a list comprehension with a nested loop to create a multiplication table (i.e., a list of lists) for the numbers 1 to 5.
# - Print both the even numbers list and the multiplication table.

even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print("even_numbers: ", even_numbers)

multiplication_table = [[x*y for x in range(1, 11)] for y in range(1, 6)]
print("multiplication_table: ",multiplication_table)