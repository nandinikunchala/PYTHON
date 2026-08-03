#Create a tuple with 5 numbers and print it.
t = (10, 20, 30, 40, 50)
print(t)
# Find the length of a tuple without using len().
t = (10, 20, 30, 40, 50)
count = 0
for x in t:
    count += 1
print(count)
# Print the first element of a tuple.
t = (10, 20, 30, 40, 50)
print(t[0])
# Print the last element of a tuple.
t = (10, 20, 30, 40, 50)
print(t[-1])
# Print all elements of a tuple using a for loop.
t = (10, 20, 30, 40, 50)

for x in t:
    print(x)
#Create a tuple containing 5 integers and print it.
t = (10, 20, 30, 40, 50)
print(t)
# Find the length of a tuple.
print(len(t))
# Check whether an element exists in a tuple.
if 30 in t:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")
# Count how many times a given element occurs in a tuple.
count=t.count(50)
print(count)
# Find the index position of a given element.
index=t.index(20)
print(index)
# Reverse a tuple.
rev=t[::-1]
print(rev)
# Convert a tuple into a list.
lst=list(t)
print(lst)
# Convert a list into a tuple
t2=tuple(lst)
print(t2)