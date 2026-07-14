#Tuple
#Tuples are used to store multiple items in a singke variable
#A tuple is a collection which is ordered and unchangeable
#tuples are written with round brackets

#Tuple items
#Tuple items are ordered,unchangeable,and allow duplicate values.Tuple items are indexed

#Tuple length:
#len() function is used
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create tuple with one item:
#To create a tuple with only one item, we have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple items data types
#tuple items can be of any data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#type()
#The tuple constructor()
#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Access tupl items
#we can access tuple items by referring to the index number, inside square brackets
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Negative indexing

#Range of indexes
#we can specify a range of indexes by specifying where to start and where to end the range.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Check if items exists 
#uses in keyword
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Change tuple values
#Once a tuple is created, we cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. we can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add items
#Append() method
#Convert into a list: Just like the workaround for changing a tuple, we can convert 
#it into a list, add our item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#Add tuple to a tuple. we are allowed to add tuples to tuples, so if we want to add one item, (or many), 
#create a new tuple with the item(s), and add it to the existing tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#del keyword is also used
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#unpack tuples
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple
ruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#use asterisk
#If the number of variables is less than the number of values, we can add an * to the variable name and
#the values will be assigned to the variable as a list
ruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#other example
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Loop tuples
#we can loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Loop through index values
#use the range() and len() functions to create a suitable iterable
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#using a while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join two tuples: + operator is used
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply tuples : * operatoe=r is used
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#Tuple methods
#count()
#index()

