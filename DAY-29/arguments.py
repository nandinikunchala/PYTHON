#Positional argument
def student(name,age):
    print(name,age)
student("Nandini",20)
#Keyword arguments
def student(name,age):
    print(name,age)
student(age=21,name="Nandini")
#default argument
def greet(name,message="Hello"):
    print(message,name)
greet("Nandu","Gud eve")

#addition
def add(a,b):
    return a+b
print(add(1,2))
#create a function that greets a person if no name is given use guest
def greet(name="guest"):
    return "Hello "+name
print(greet())
print(greet("laxmi"))
#create a function that displays name and age of a student call it using keyword argument
def student(name,age):
    print(age)
    print(name)
student(age=20,name="nandy")

#create a function to calculate a power default exponent 2(default+position)
def power(n,p=2):
    return n**p
print(power(5))
print(power(8,3))

#pos+key
def person(name,age,city):
    print(name,age,city)
person("veda",age=21,city="hyd")

