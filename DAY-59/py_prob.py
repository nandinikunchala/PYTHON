#1.Print Hello World without using a variable.
print("Hello World")
# 2. Swap two numbers without a third variable.
a=1
b=2
a,b=b,a
print(a,b)
# 3. Check whether a number is positive, negative or zero.
n=0
if n<0:
    print("Negative")
elif n>0:
    print("Positive")
else:
    print("Zero")
# 4. Find the largest of three numbers.
m=(20,30,40)
largest=0
for x in m:
    if x>largest:
        largest=x
print(largest)
# 5. Check whether a number is even or odd.
m=2
if m%2==0:
    print("Even")
else:
    print("Odd")
# 6. Calculate factorial.
n=5
fac=1
for x in range(1,n+1):
    fac*=x
print(fac)
# 7. Generate Fibonacci numbers.
n=10
a=0
b=1
for x in range(n):
    print(a)
    a,b=b,a+b
# 8. Check whether a number is prime.
f = 6
count = 0
for x in range(1, f + 1):
    if f % x == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")
# 9. Reverse an integer.
a=1236
rev=0
while a>0:
    rev=rev*10+a%10
    a//=10
print(rev)
# 10. Find the sum of digits of a number.
d=1234
sum=0
while d>0:
    sum=sum+d%10
    d//=10
print(sum)
# 11. Reverse a string.
k="Nandini"
rev=""
for x in k:
    rev=x+rev
print(rev)
# 12. Check whether a string is a palindrome.
l="afifa"
if l==l[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
# 13. Count vowels and consonants.
h="Nandini"
count_vowels=0
count_consonents=0
for char in h.lower():
    if char in "aeiou":
        count_vowels+=1
    else:
        count_consonents+=1
print("Vowels:",count_vowels)
print("Consonants:",count_consonents)
# 14. Count the frequency of every character.
s="Nandini"
for x in s:
    print(x,s.count(x))
# 15. Find the first non-repeating character.
j="Nandini"
for char in j.lower():
    if j.lower().count(char)==1:
        print(char)
        break
# 16. Remove duplicate characters from a string.
g="Nandini"
dup_str=""
for x in g.lower():
    if x not in dup_str:
        dup_str+=x
print(dup_str)
# 17. Check whether two strings are anagrams.
n="silent"
m="listen"
if sorted(n)==sorted(m):
    print("Anagrams")
else:
    print("Not anagrams")
# 18. Find the longest word in a sentence.
i="I am Kunchala Nandini"
longest=""
for x in i.split():
    if len(x)>len(longest):
        longest=x
print(longest)
# 19. Count words in a sentence.
p="I am Kunchala Nandini"
count=0
for x in p.split():
    count+=1
print(count)
# 20. Implement string compression.
s = "aaabbc"
compressed = ""
count = 1
for x in range(1, len(s)):
    if s[x] == s[x - 1]:
        count += 1
    else:
        compressed += s[x - 1] + str(count)
        count = 1
compressed += s[-1] + str(count)
print(compressed)
# 21. Find maximum and minimum in a list without max()/min().
p=[10,20,30,40]
min=p[0]
max=0
for x in p:
    if x<min:
        min=x
    if x>max:
        max=x
print("Maximum:",max)
print("Minimum:",min)
# 22. Remove duplicates from a list.
h=[10,20,10,30,10]
new_h=[]
for x in h:
    if x not in new_h:
        new_h.append(x)
print(new_h)
# 23. Find the second-largest number.
l=(10,20,30)
lar=0
sec_lar=0
for x in l:
    if x>lar:
        sec_lar=lar
        lar=x
    elif x>sec_lar:
        sec_lar=x
print("Second Largest:",sec_lar)
# 24. Reverse a list without reverse().
v=[10,20,30]
rev=[]
for x in v:
    rev=[x]+rev
print(rev)
# 25. Find common elements between two lists.
k=[10,30,40,50]
l=[10,80,20,70,30]
common=[]
for x in k:
    if x in l:
        common.append(x)
print(common)
# 26. Merge two sorted lists.
a=[10,20]
b=[30,40]
merge=[]
for x in a:
    merge.append(x)
for x in b:
    merge.append(x)
print(merge)
# 27. Move all zeros to the end.
z=[0,20,0,40,50,0,60]
lis=[]
for x in z:
    if x!=0:
        lis.append(x)
for x in z:
    if x==0:
        lis.append(x)
print(lis)
# 28. Find missing numbers from a sequence.
s= [1, 2, 4, 5, 7, 8]
for x in range(1, 9):
    if x not in s:
        print(x)
# 29. Rotate a list by k positions.
a = [10, 20, 30, 40, 50]
k = 2
k = k % len(a)
result = a[-k:] + a[:-k]
print(result)
# 30. Find duplicate elements.
g=(10,20,10,30,20)
dup_ele=[]
for x in g:
    if x in dup_ele:
        print(x)
    else:
        dup_ele.append(x)
# 31. Count word frequency using a dictionary.
sentence = "I am Nandini and I am learning Python"
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)
# 32. Find the most frequent element.
a = [10, 20, 10, 30, 10, 20]
frequent= a[0]
for x in a:
    if a.count(x) > a.count(frequent):
        frequent = x
print(frequent)
# 33. Group words that are anagrams.
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}
for word in words:
    key = "".join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
print(list(groups.values()))
# 34. Invert a dictionary.
d = {"a": 1, "b": 2, "c": 3}
inverted = {}
for key, value in d.items():
    inverted[value] = key
print(inverted)
# 35. Merge two dictionaries.
l={"a":10,"b":20}
m={"c":30,"d":40}
merged={}
for key, value in l.items():
    merged[key] = value
for key, value in m.items():
    merged[key] = value
print(merged)
# 36. Find common keys between dictionaries.
l={"a":10,"b":20}
m={"a":10,"d":40}
common={}
for key,vaslue in l.items():
    if key in m:
        common[key]=value
print(common)
# 37. Find unique elements using sets.
a = [10, 20, 10, 30, 20, 40]
unique = set(a)
print(unique)
# 38. Build a student grade tracker.
marks=90
if marks>=90:
    print("A Grade")
elif marks<90 and marks>=80:
    print("B Grade")
elif marks<80 and marks>=70:
    print("C Grade")
elif marks<70 and marks>=60:
    print("D Grade")
else:
    print("Fail")
# 39. Create a phone-book application.
phonebook = {}
phonebook["Nandini"] = "6302238280"
phonebook["Rahul"] = "8018831349"
phonebook["Priya"] = "9876543212"
name = input("Enter name: ")
if name in phonebook:
    print("Phone number:", phonebook[name])
else:
    print("Contact not found")
# 40. Create a dictionary-based inventory system.
inventory = {
    "Laptop": 5,
    "Phone": 10,
    "Keyboard": 15
}
item = input("Enter item: ")
if item in inventory:
    print("Available quantity:", inventory[item])
else:
    print("Item not found")