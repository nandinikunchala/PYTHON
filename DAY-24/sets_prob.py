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

#Medium
#Find the sum of all elements in a set.
f={8,9,6,5}
sum=0
for i in f:
    sum+=i
print(sum)
# Find all even elements in a set.
for i in f:
    if i%2==0:
        print(i)
# Find all odd elements in a set.
for i in f:
    if i%2!=0:
        print(i)
# Create a new set containing squares of all elements.
for i in f:
    print(i**2)
# Count the number of even and odd elements in a set.
even=0
odd=0
for i in f:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even:",even)
print("odd:",odd)
# Find the union of two sets.
a={1,2,3}
b={4,5,6}
union=a.union(b)
print(union)
# Find the intersection of two sets.
intersection=a.intersection(b)
print(intersection)
# Find the difference of two sets.
difference=a.difference(b)
print(difference)
# Find the symmetric difference of two sets.
symmetric_difference=a.symmetric_difference(b)
print(symmetric_difference)
# Check whether one set is a subset of another.
print(a.issubset(b))
# Check whether one set is a superset of another.
print(a.issuperset(b))
# Check whether two sets are disjoint.
print(a.isdisjoint(b))
# Remove all common elements from two sets.
a.difference_update(b)
print(a)
# Find elements present in the first set but not in the second.
print(a.difference(b))
# Merge three sets into one.
c={7,8,9}
merged=a.union(b).union(c)
print(merged)
# Remove duplicate elements from a list using a set.
l=[1,2,3,4,5,1,2,3]
unique=set(l)
print(unique)
# Find common elements among three sets.
common=a.intersection(b).intersection(c)
print(common)
# Find unique elements from two lists using sets.
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
unique_elements=set(l1).symmetric_difference(set(l2))
print(unique_elements)
# Count the number of unique words in a sentence.
sentence="This is a sample sentence with some sample words"
words=sentence.split()
unique_words=set(words)
print("Number of unique words:", len(unique_words))
# Count the number of unique characters in a string.
s="hello"
unique_characters=set(s)
print("Number of unique characters:", len(unique_characters))

