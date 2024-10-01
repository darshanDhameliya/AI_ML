# Task 5: Functions
# Write a Python function calculate_area() that:
# - Takes two parameters: length and width (both integers or floats).
# - Returns the area of a rectangle (length × width).
# - Call the function with different sets of parameters and print the results.

def calculate_area(length: float, width: float):
    return length * width

print('calculate_area(2, 2): ',calculate_area(2, 2))
print('calculate_area(2, 2.4): ',calculate_area(2, 2.4))
print('calculate_area(2.2, 2.4): ',calculate_area(2.2, 2.4))