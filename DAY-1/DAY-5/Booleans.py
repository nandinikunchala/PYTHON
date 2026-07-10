#Booleans
#Boolean represent one of two values:True or False
print(10>9)
print(10==9)
print(30<50)

#bool() function
print(bool("Hello"))
print(bool(15))

#Evaluate two values
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#Evaluate values
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#Some evaluate false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Functions can return a boolean
def myFunction() :
  return True
print(myFunction())


