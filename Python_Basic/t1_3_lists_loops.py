# Task 3: Lists and Loops
# Write a Python program that:
# - Creates a list of at least 5 integers.
# - Uses a for loop to iterate through the list and print each number.
# - Uses a while loop to find the sum of all numbers in the list.

list = [1, 2, 3, 4, 5]

print("For Loop: Print all number")
for number in list:
    print(number)

sum = 0
index = 0


print("While Loop: Sum of all number")
while index < len(list):
    sum += list[index]
    index += 1

print(sum)