#Indentation is important in Python, as it defines the structure of the code
if 10<100:
    print("10 is less than 100")


# Data types 
print(type("100"))#<class 'str'>
print(type(100))#<class 'int'>
print(type(10.0))#<class 'float'>
print(type(True))#<class 'bool'>        
print(type(None))#<class 'NoneType'>
print(type([1, 2, 3]))#<class 'list'>
print(type((1, 2, 3)))#<class 'tuple'>
print(type({1, 2, 3}))#<class 'set'>
print(type({"A":1}))#<class 'dict'>
print(type(range(6)))#<class 'range'>
print(type(b"Hello"))#<class 'bytes'>
print(type(bytearray(5)))#<class 'bytearray'>
print(type(memoryview(bytes(5))))#<class 'memoryview'>
print(type(frozenset({1, 2, 3})))#<class 'frozenset'>
print(type(complex(1j)))#<class 'complex'>



a = True
print(type(a))#<class 'bool'> not str because no quotes are used
a = {}
print(type(a))#<class 'dict'> not set because no values are used


#RANDOM NUMBER
#Python does not have a built-in random() function to make a random number, 
#but Python has a built-in module called random that can be used to make random numbers.
import random
print(random.randrange(1, 10)) #it will print a random number between 1 and 10

#PYTHON CASTING
#int()-integers , float(removes all decimals),string(represents a whole number)
#float-integer,float,string(represents float or string)
#string-integer, float, string.
