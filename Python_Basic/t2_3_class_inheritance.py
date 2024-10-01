# Task 3: OOP - Classes and Inheritance
# Write a Python program that:
# - Defines a class Person with attributes for name and age, and a method greet() that prints a greeting with the person's name.
# - Defines a subclass Employee that inherits from Person, adds an additional attribute employee_id,and overrides the greet() method to include the employee ID in the greeting.
# - Create objects of both Person and Employee and call their respective greet() methods.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("name:", self.name, ", age:", self.age)
        
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    def greet(self):
        print("name:", self.name, ", age:", self.age, ", employee_id:", self.employee_id)


person = Person("darshan", 25)
person.greet()

employee = Employee("paras", 24, 101)
employee.greet()