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
