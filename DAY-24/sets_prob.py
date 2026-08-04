#Create a set with 5 integers and print it.
x={1,2,3,4,5}
print(x)
# Add an element to a set.
x.add(7)
print(x)
# Add multiple elements to a set.
x.update([8,9,10])
print(x)
# Remove an element from a set.
x.remove(3)
print(x)
# Remove an element using discard().
x.discard(5)
print(x)
# Remove and return a random element using pop().
y=x.pop()
print(y)
print(x)
# Clear all elements from a set.
x.clear()
print(x)
# Find the number of elements in a set.
print(len(x))
# Check whether an element exists in a set.
print(3 in x)
# Copy a set into another set.
y=x.copy()
print(y)
# Print all elements of a set using a loop.
for i in x:
    print(i)
# Convert a list into a set.
l=[1,2,3,4,5]
x=set(l)
print(x)
# Convert a tuple into a set.
t=(1,2,3,4,5)
x=set(t)
print(x)
# Convert a string into a set of unique characters.
s="hello"
x=set(s)
print(x)
# Find the maximum and minimum elements in a set.
print(max(x))
print(min(x))
