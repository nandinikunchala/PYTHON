#1.Create a list containing 5 integers and print it.
mylist=[10,20,30,40,50]
print(mylist)

#2.Print the first, last, and middle element of a list.
print(mylist[0])
print(mylist[-1])
print(mylist[len(mylist)//2])

#3.Print elements from index 2 to 5 using slicing.
x=[2,4,6,8,10,12,14]
print(x[2:6])

#4.Replace the second element with a new value.
x[1]=9
print(x)

#5.Replace the last three elements with new values.
x[4]=7
x[5]=5
x[6]=3
print(x)

#6.Append an element and insert another at index 2.
x.append(15)
print(x)
x[2]=16
print(x)

#7.Extend a list using another list.
y=[20,40,60,80]
x.extend(y)
print(x)

#8.Remove an element using remove() and another using pop().
x.remove(16)
print(x)
x.pop(6)
print(x)

#9.Clear all elements from a copied list.
a=["apple","banana","orange"]
copied_list=a.copy()
copied_list.clear()
print(copied_list)

#10.Print all elements using for and while loops.
for value in a:
    print(value)

i=0
while i< len(a):
    print(a[i])
    i += 1

#Find the length of a list without using len().
z=[12,5,8,44,85]
count=0
for num in z:
    count+=1
print(count)
# Find the sum of all elements.
sum=0
for num in z:
    sum+=num
print(sum)
# Find the maximum and minimum elements.
max=0
for x in z:
    if x>max:
        max=x
print(max)
min=z[0]
for x in z:
    if x<min:
        min=x
print(min)
# Find the average of all elements.
avg=0
for num in z:
    avg+=num
print(avg/len(z))
# Count even, odd, positive, negative, and zero elements.
count=0
for x in z:
    if x%2==0:
        count+=1
print(count)
odd=0
for x in z:
    if x%2!=0:
        odd+=1
print(odd)
positive=0
for x in z:
    if x>0:
        positive+=1
print(positive)
neg=0
for x in z:
    if x<0:
        neg+=1
print(neg)
zero=0
for x in z:
    if x==0:
        zero+=1
print(zero)
# Search for an element and print its index.
# Count the frequency of a given element.
# Count the frequency of every element without using count().
# Reverse a list without using reverse().
# Copy a list without using copy().
# Check whether a list is in ascending order.
# Remove all duplicate elements while preserving order.
# Find the second largest and second smallest elements.
# Rotate a list left by k positions.
# Rotate a list right by k positions.

