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

#Create a class called BankAccount.
# Using __init__(), store:
# name
# balance
# Create a method:
# deposit(amount)
# The method should increase the balance by the given amount.
# Then:
# account = BankAccount("Nandini", 1000)
# account.deposit(500)
# print(account.balance)
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
account=BankAccount("Nandini",1000)
account.deposit(500)
print(account.balance)

#Create a BankAccount class with:
# name
# balance
# Use __init__().
# Create a method:
# withdraw(amount)
# It should decrease the balance by the given amount.
# Test with:
# account = BankAccount("Nandini", 2000)
# account.withdraw(500)
# print(account.balance)
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def withdraw(self,amount):
        self.balance-=amount
account = BankAccount("Nandini", 2000)
account.withdraw(500)
print(account.balance)

#Create a Student class with:
# name
# marks
# Use __init__().
# Create a method:
# display()
# that prints:
# Name: <name>
# Marks: <marks>
# Then create two objects:
# s1 = Student("Rahul", 85)
# s2 = Student("Priya", 92)
# Call display() for both objects.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Name:{self.name}")
        print(f"Marks:{self.marks}")
s1=Student("Rahul",85)
s2=Student("Priya",92)
s1.display()
s2.display()

# Create a Person class with a class attribute:
# country = "India"
# Use __init__() to create an instance attribute:
# name
# Create:
# p1 = Person("Rahul")
# p2 = Person("Priya")
# Print the name and country for both.
class Person:
    country="India"
    def __init__(self,name):
        self.name=name
p1=Person("Rahul")
p2=Person("Priya")
print(p1.name,p1.country)
print(p2.name,p2.country)

#Create a Person class with:
# name
# age
# Use __init__().
# Create:
# p1 = Person("Rahul", 25)
# Then change Rahul's age to 30 using the object.
# Finally, print the age.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Rahul",25)
p1.age=30
print(p1.age)

#Create a Person class with:
# country = "India"
# Create two objects:
# p1 = Person()
# p2 = Person()
# Then change the class attribute using the class itself:
# Person.country = "USA"
class Person:
    country="India"
p1=Person()
p2=Person()
Person.country="USA"
print(p1.country) 
print(p2.country)

