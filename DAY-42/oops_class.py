#CLASS
#A class is a blueprint/template for creating objects.

#Create a class called Student.
# Create an object of the class called s1.
# Print "Student created" using the object.
class Student:
    def display(self):
        print("Student created")
s1=Student()
s1.display()

#Create a class called Car.
# Create an object called c1.
# Add an attribute brand with the value "Toyota".
# Print the brand using the object.
class Car:
    pass
c1=Car()
c1.brand='Toyota'
print(c1.brand)

#Create a class called Student.
# Create an object s1.
# Add name = "Nandini" and age = 21 to the object.
# Print both values using s1.
class Student:
    pass
s1 = Student()
s1.name = "Nandini"
s1.age = 21
print(s1.name)
print(s1.age)
