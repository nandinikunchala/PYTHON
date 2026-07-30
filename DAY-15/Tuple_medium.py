#Find the maximum element in a tuple without using max().
x=(1,2,5,9)
max=0
for number in x:
    if number>max:
        max=number
print(max)
# Find the minimum element in a tuple without using min().
a=(50,60,85,20,40)
min=a[0]
for number in a:
    if number<min:
        min=number
print(min) 
# Find the sum of all elements without using sum().
sum=0
for x in a:
    sum+=x
print(sum)
# Find the average of the tuple elements.
avg=0
for x in a:
    avg+=x
print(avg/len(a))
# Find the second largest element.
largest=0
s_largest=0
for x in a:
    if x>largest:
        s_largest=largest
        largest=x
print(s_largest)
# Find the second smallest element.
# Count even and odd numbers in a tuple.
a=(2,3,4,5,6,7,8)
even=0
odd=0
for x in a:
    if x%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers:",even)
print("Odd numbers:",odd)
# Create a new tuple containing only even numbers.
c=(2,4,2,6,8,4,12,14)
# Remove duplicate elements (create a new tuple).
new=()
for x in c:
    if x not in new:
        new+=(x,)
print(new)
# Check whether a tuple is sorted in ascending order.
if c==tuple(sorted(c)):
    print("Sorted")
else:
    print("Not sorted")
# Merge two tuples and sort them.
u=(8,9,7,6)
v=(1,2,3,4)
y=u+v
y==tuple(sorted(y))
print(y)
# Find the common elements between two tuples.
i=(1,2,3,4,5)
j=(1,7,8,4,5)
common=()
for x in i:
    if x in j:
        common+=(x,)
print(common)
# Find the elements that are present in the first tuple but not in the second.
result=()
for x in i:
    if x not in j:
        result+=(x,)
print(result)
# Check whether all elements are unique.
if len(j)==len(set(j)):
    print("Unique")
else:
    print("Not Unique")
# Convert a tuple into a list and vice versa.
f=(4,7,8,9)
k=list(f)
print(k)
o=tuple(k)
print(o)
