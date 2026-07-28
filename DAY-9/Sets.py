#Sets
#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unchangeable, but you can remove items and add new items.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Set items
#Unordered
#Unchangeable
#No duplicates allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)#duplicate values will be ignored
#The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#The values False and 0 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Length of a set
#len() function is used
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Sets-data types
#Set items can be of any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#A set can contain different datatypes
set1 = {"abc", 34, True, 40, "male"}

#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

#set() constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Acess items
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Add items
#To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#The object in the update() method does not have to be a set, 
#it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove items
#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#If the item to remove does not exist, discard() will NOT raise an error.

#Remove a random item by using the pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#The clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#Loop items
#We can loop through the set items by using a for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Join sets
#The union() and update() methods joins all items from both sets.
#The intersection() method keeps ONLY the duplicates.
#The difference() method keeps the items from the first set that are not in the other set(s).
#The symmetric_difference() method keeps all items EXCEPT the duplicates.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)#The union() method returns a new set with all items from both sets.

#You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#Join Multiple Sets
#All the joining methods and operators can be used to join multiple sets.
#When using a method, just add more sets in the parentheses, separated by commas:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#When using the | operator, separate the sets with more | operators
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#Join a Set and a Tuple
#The union() method allows you to join a set with other data types, like lists or tuples.
#The result will be a set.
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
#The  | operator only allows you to join sets with sets, and not with other data types 
#like you can with the  union() method.

#Update
#The update() method inserts all items from one set into another.
#The update() changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#Both union() and update() will exclude any duplicate items.

#Intersection
#Keep ONLY the duplicates
#The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#You can use the & operator instead of the intersection() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
#The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

#The intersection_update() method will also keep ONLY the duplicates, 
#but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#The values True and 1 are considered the same value. The same goes for False and 0.
#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)#False,True,apple

#The difference() method will return a new set that will contain only the 
#items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
#You can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
#The - operator only allows you to join sets with sets, and not with 
#other data types like you can with the difference() method.

#The difference_update() method will keep the items from the first set that are not in the other set,
#but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
#The ^ operator only allows you to join sets with sets, and not with
# other data types like you can with the symmetric_difference() method.

#The symmetric_difference_update() method will also keep all but the duplicates, 
#but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

#Frozenset
#frozenset is an immutable version of a set.
#Like sets, it contains unique, unordered, unchangeable elements.
#Unlike sets, elements cannot be added or removed from a frozenset.
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
#Methods
#copy()
#difference()
#intersection()
##isdisjoint()
#issubset()
#issuperset()
#symmetric_difference()
#union()

#set methods
#add()	 	
#clear()	 	
#copy()	 	
#difference()	-	
#difference_update()	-=	
#discard()	 	
#intersection()	&	
#intersection_update()	&=	
#isdisjoint()	<=,< 	
#issuperset()	>=,>	
#pop()	 	
#remove()	 	
#symmetric_difference()	^	
#symmetric_difference_update()	^=	
#union()	|
#update()