#Create a Student class with:
# name
# age
# Create one object with "Rahul", 21 and print the name and age.
class Student:
    name="Rahul"
    age=20
s1=Student()
print(s1.name)
print(s1.age)
#Now create a class called Car with these class properties:
# brand = "Toyota"
# model = "Camry"
class Car:
    brand="Toyota"
    model="Camry"

#Create a class called Laptop with these three class properties:
# brand = "Dell"
# ram = 16
# price = 60000
# Don't create an object.
class Laptop:
    brand="Dell"
    ram=16
    price=60000

#Create a class called Mobile with:
# brand = "Samsung"
# price = 25000
# Then:
# Create an object called m1
# Print m1.brand
# Print m1.price
class Mobile:
    brand="Samsung"
    price=25000
m1=Mobile()
print(m1.brand)
print(m1.price)

#Create a class called Person with a class property:
# country = "India"
# Then create two objects:
# p1
# p2
# Print the country property using both objects.
# Expected output:
# India
# India
class Person:
    country="India"
p1=Person()
p2=Person()
print(p1.country)
print(p2.country)

#Create a class called Student.
# Use __init__() to receive:
# name
# age
# Store them as instance attributes using self.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Nandini",20)
print(s1.name)
print(s1.age)

#Create a Car class using __init__() with:
# brand
# model
# year
# Create:
# car1 = Car("Toyota", "Camry", 2024)
# Then print all three attributes.
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
car1 = Car("Toyota", "Camry", 2024)
print(car1.brand)
print(car1.model)
print(car1.year)

#Create a class called Person with:
# name
# age
# Use __init__() to initialize them.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
p1 = Person("Nandini", 20)
p1.introduce()

#Create a class called Rectangle.
# Using __init__(), store:
# length
# width
# Create a method called area() that returns the area.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r1 = Rectangle(10, 5)
print(r1.area())