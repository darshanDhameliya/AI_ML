# Task 4: Generators
# Write a Python program that:
# - Implements a generator fibonacci_generator(n) that generates the first n Fibonacci numbers.
# - Use the generator to print the first 10 Fibonacci numbers.
# - Explain the benefits of using generators over lists for large data.

def fibonacci_generator(n):
    index, n1, n2 = 0, 0, 1
    yield n1
    while index < n:
        yield n2
        n1, n2 = n2, n1 + n2
        index += 1

fibonacci_number = fibonacci_generator(10)

print(fibonacci_number)
print(next(fibonacci_number))
print(next(fibonacci_number))
print(next(fibonacci_number))
print(next(fibonacci_number))
print(list(fibonacci_number))