#Create a tuple with 5 integers and print it.
x=(1,2,6,7,9)
print(x)
# Print the first and last element of a tuple.
print(x[0],x[-1])
# Find the length of a tuple without using len().
count=0
for num in x:
    count+=1
print(count)
# Check whether a given element exists in a tuple.
i=2
if i in x:
  print("exists")
# Count how many times an element appears in a tuple.
b=(6,8,4,6,0,6)
count=0
for i in b:
   if i == 6:
      count+=1
print(count)
# Find the index of an element in a tuple.
n=(8,9,6,0)
index=0
for x in n:
   if x==0:
      print(index)
   index+=1
# Concatenate two tuples.
m=(6,8,9)
p=(5,4,3)
print(m+p)
# Repeat a tuple 3 times.
u=(4,5,8,7)
print(u*3)
# Slice a tuple to print the first 3 elements.
h=(7,8,9,1,2,3)
print(h[:3])
# Reverse a tuple using slicing.
print(h[::-1])