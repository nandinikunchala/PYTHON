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

#Medium
#Find the maximum and minimum elements in a tuple.
j=(1,6,9,5,3)
max=0
for x in j:
    if x>max:
        max=x
print(max)
min=0
for x in j:
    if x<min:
        min=x
print(min)
# Find the sum of all elements in a tuple.
sum=0
for x in j:
    sum+=x
print(sum)
# Print all even numbers from a tuple.
even=()
for x in j:
    if x%2==0:
        even+=(x,)
print(even)
# Print all odd numbers from a tuple.
odd=()
for x in j:
    if x%2!=0:
        odd+=(x,)
print(odd)
# Create two tuples containing even and odd numbers separately.
even=()
odd=()
for x in j:
    if x%2==0:
        even+=(x,)
    else:
        odd+=(x,)
print("Even numbers:",even)
print("Odd numbers:",odd)
# Double every element in a tuple.
double=()
for x in j:
    double+=(x*2,)
print(double)
# Find the common elements between two tuples.
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)
common=()
for x in t1:
    if x in t2:
        common+=(x,)
print(common)
# Find elements present in the first tuple but not in the second.
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)
unique=()
for x in t1:
    if x not in t2:
        unique+=(x,)
print(unique)
# Check whether all elements in a tuple are unique.
t = (1, 2, 3, 4, 5)
if len(t) == len(set(t)):
    print("All elements in the tuple are unique.")
else:
    print("The tuple contains duplicate elements.")
# Remove duplicate elements from a tuple.
t = (1, 2, 3, 4, 5, 4, 3, 2, 1)
t = tuple(set(t))
print(t)
# Sort a tuple in ascending order.
t = (5, 4, 3, 2, 1)
t = tuple(sorted(t))
print(t)
# Sort a tuple in descending order.
t = (5, 4, 3, 2, 1)
t = tuple(sorted(t, reverse=True))
print(t)
# Find the second largest element in a tuple.
t = (1, 2, 3, 4, 5)
t = tuple(sorted(set(t), reverse=True))
print(t[1])
# Find the second smallest element in a tuple.
t = (1, 2, 3, 4, 5)
t = tuple(sorted(set(t)))
print(t[1])
# Count the number of positive and negative numbers in a tuple.
t = (1, -2, 3, -4, 5)
positive_count = 0
negative_count = 0
for x in t:
    if x > 0:
        positive_count += 1
    elif x < 0:
        negative_count += 1
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
# Find the frequency of each element in a tuple.
# Find all duplicate elements in a tuple.
# Find the first non-repeating element in a tuple.
# Find the largest and smallest elements without using max() and min().
# Merge two tuples and sort the resulting tuple.
# Find the elements that appear in both tuples without duplicates.
# Remove all occurrences of a given element from a tuple.
# Find the sum of all elements in a nested tuple.
# Flatten a nested tuple into a single tuple.
# Sort a tuple of tuples based on the second element.
# Find the tuple with the maximum sum from a tuple of tuples.
# Find the longest tuple from a tuple containing multiple tuples.
# Create a tuple containing only the first occurrence of each element while maintaining the original order.