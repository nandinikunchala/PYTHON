#Class Methods
# Methods are functions that belong to a class. They define the behavior of objects created from the class.
#EX:Create a method in a class:
class Person:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()

#Methods with Parameters
# Methods can accept parameters just like regular functions.
# EX:Create a method with parameters.
class Calculator:
  def add(self, a, b):
    return a + b
  def multiply(self, a, b):
    return a * b
calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

#Methods Accessing Properties
# Methods can access and modify object properties using self
# EX:A method that accesses object properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def get_info(self):
    return f"{self.name} is {self.age} years old"
p1 = Person("Tobias", 28)
print(p1.get_info())

#The __str__() Method
#The __str__() method is a special method that controls what is returned when the object is printed
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name} ({self.age})"
p1 = Person("Tobias", 36)
print(p1)
