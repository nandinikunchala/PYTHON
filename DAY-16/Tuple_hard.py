# Find the frequency of every element without using count().
# Example:
# (1,2,1,3,2,1)
# Output:
# 1 : 3
# 2 : 2
# 3 : 1
t = (1, 2, 1, 3, 2, 1)
for i in t:
    if t.index(i) == t.index(i):
        frequency = 0

        for j in t:
            if i == j:
                frequency += 1
        print(i, ":", frequency)
# Find the first non-repeating element.
t = (1, 2, 1, 3, 2, 4)
for i in t:
    frequency = 0
    for j in t:
        if i == j:
            frequency += 1
    if frequency == 1:
        print(i)
        break
# Find the first repeating element.
t = (1, 2, 3, 2, 4, 3)
for i in t:
    frequency = 0
    for j in t:
        if i == j:
            frequency += 1
    if frequency > 1:
        print(i)
        break
# Check whether two tuples are equal without using ==.
t1 = (1, 2, 3)
t2 = (1, 2, 3)
if len(t1) != len(t2):
    print("Not Equal")
else:
    equal = True

    for i in range(len(t1)):
        if t1[i] != t2[i]:
            equal = False
            break
    if equal:
        print("Equal")
    else:
        print("Not Equal")
# Check whether one tuple is a subset of another.
t1 = (2, 3)
t2 = (1, 2, 3, 4, 5)
is_subset = True
for i in t1:
    if i not in t2:
        is_subset = False
        break
if is_subset:
    print("Subset")
else:
    print("Not a subset")
# Find the intersection of two tuples without using sets.
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
result = ()
for i in t1:
    if i in t2 and i not in result:
        result += (i,)
print(result)
# Find the union of two tuples without using sets.
t1 = (1, 2, 3)
t2 = (3, 4, 5)
result = t1
for i in t2:
    if i not in result:
        result += (i,)

print(result)
# Split a tuple into two equal halves.
t = (1, 2, 3, 4, 5, 6)
middle = len(t) // 2
first = t[:middle]
second = t[middle:]
print(first)
print(second)
# Swap the first and last elements of a tuple.
t = (1, 2, 3, 4, 5)
result = (t[-1],) + t[1:-1] + (t[0],)
print(result)
# Find all pairs whose sum is equal to a given target.
# Example:
# (2,4,3,5,7,8)
# Target = 10
# Output:
# (2,8)
# (3,7)
t = (2, 4, 3, 5, 7, 8)
target = 10
for i in range(len(t)):
    for j in range(i + 1, len(t)):
        if t[i] + t[j] == target:
            print((t[i], t[j]))
# Find the longest increasing consecutive sequence in a tuple.
t = (1, 2, 3, 2, 3, 4, 5, 1)
current = (t[0],)
longest = (t[0],)
for i in range(1, len(t)):
    if t[i] > t[i - 1]:
        current += (t[i],)
    else:
        current = (t[i],)

    if len(current) > len(longest):
        longest = current
print(longest)
# Check whether a tuple is a palindrome.
# Example:
# (1,2,3,2,1)
# Output: Palindrome
t = (1, 2, 3, 2, 1)
if t == t[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
# Compress a tuple by counting consecutive repeated elements.
# Example:
# (1,1,1,2,2,3,3,3,3)
# Output:
# ((1,3), (2,2), (3,4))
t = (1, 1, 1, 2, 2, 3, 3, 3, 3)
result = ()
count = 1
for i in range(1, len(t)):
    if t[i] == t[i - 1]:
        count += 1
    else:
        result += ((t[i - 1], count),)
        count = 1
result += ((t[-1], count),)
print(result)
