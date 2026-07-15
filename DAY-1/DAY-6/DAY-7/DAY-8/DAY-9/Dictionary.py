#Dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Dictionary Items
#Dictionary items are ordered, changeable, and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Dictionary Length
#len() function is used
print(len(thisdict))
#Dictionary Items - Data Types
#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#type()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#The dict() Constructor
#It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Accessing Items
#We can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#There is also a method called get() that will give you the same result:
x = thisdict.get("model")

#Get Keys
#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
#The list of the keys is a view of the dictionary, meaning that any changes done to the 
#dictionary will be reflected in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x) #after the change

#Get Values
#The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
#The list of the values is a view of the dictionary, meaning that any changes done to the 
#dictionary will be reflected in the values list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

#Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change

car["color"] = "red"
print(x) #after the change

#Get Items
#The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
#The returned list is a view of the items of the dictionary, meaning that any changes done to the 
#dictionary will be reflected in the items list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

#Add a new item to the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change

car["color"] = "red"
print(x) #after the change
#Check if Key Exists
# in keyword is used
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change Values
#We can change the value of a specific item by referring to its key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Update Dictionary
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#add items same as change items

#Removing Items
#There are several methods to remove items from a dictionary:

#The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Loop Through a Dictionary
#We can loop through a dictionary by using a for loop.
#When looping through a dictionary, the return value are the keys of the dictionary, 
#but there are methods to return the values as well.
for x in thisdict:
  print(x)

#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])

#We can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

#We can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

#Copy dictionaries
#copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#use the built-in function dict().(another way)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Access Items in Nested Dictionaries
#To access items from a nested dictionary, we use the name of the dictionaries, starting with the outer dictionary:
print(myfamily["child2"]["name"])

#Loop Through Nested Dictionaries
#We can loop through a dictionary by using the items() method like this:
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#Dictionary Methods
# clear()	
# copy()	
# fromkeys()	
# items()	
# keys()
# pop()	
# popitem()	
# setdefault()
# update()	
# values()