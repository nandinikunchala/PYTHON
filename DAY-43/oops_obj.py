#OBJECT
#Almost everything in Python is an object, with its properties and methods.
#Create Object
# Now we can use the class named MyClass to create objects:
# Ex:
# Create an object named p1, and print the value of x:
class MyClass:
  x = 5
p1 = MyClass()#object
print(p1.x)

#Delete Objects
#You can delete objects by using the del keyword

#Multiple Objects
# You can create multiple objects from the same class:
# Example
# Create three objects from the MyClass class:
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)