#Lists
#list are used to store multiple items in a single variable
#lists are one of 4 built-in data types in python used to store collections of data,the other 3 are tuple,list,dict
#lists are created using square brackets
thislist = ["apple", "banana", "cherry"]
print(thislist)

#list items
#list items are ordered,changeable and allow duplicates
#list items are indexed

#list length
#to determine how many items a list has,use the len() keyword
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#list items-data types
#list items can be of any data type (str,bool,int)
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#type()
#lists are defined as objects with the data type 'list'<class 'list'>
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#list() constructor
#list constructor is used to create new list

#python collections:
#there are four collection data types in python
#list,tuple,set,dict

#Access list items
#list items are indexed and we can access them by referring to the index number

#Range of indexes
#wecan specify a range of indexes by specifying where to start and where to end the range.

#Check if item exits(use in keyword)

#Change list items
#To change the value of a specific item,refer to the index number. 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a range of item values
#To change the value of items within a specific range, define a list with the new values, 
#and refer to the range of index numbers where you want to insert the new values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#If you insert more items than you replace, the new items will be inserted where you specified, 
#and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#The length of the list will change when the number of items inserted does not match the number of items replaced.

#Insert items
#to insert a new list item,without replacing any of the existing values,we can use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Append items
#To add an item to the end of list,we use the append() method.
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Extend list
#To append elements from another list to the current list,use the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove item
#The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#If there are more than one item with the specified value, the remove() method removes the first occurrence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#remove index: pop() method is used
#del keyword also removes the specified index
#del keyword can also delete the list completely
#clear list:
#clear() method empties list.The list still remains,but it has no content.

#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#loop throug index number
#Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while loop:
#len() function is used to determine the length of list
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#looping using list comprehension
#List Comprehension offers the shortest syntax for looping through lists
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#list comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#sort list alphanumerically
#list objects have a sort() method that will sort the list alphanumerically,ascending,by default
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)#sorted alphanumerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)#sorted numerically

#sort descending
#to sort descending,use the keyword argument reverse=True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#copy lists
#we can use built-in list method copy() to copy a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#another way to make a copy is to use the built-in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#we can also make a copy of a list by using the :(slice) operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Join lists
#easiest way is to use + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#another way is appending
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#extend() method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
