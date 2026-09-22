#1.Print Hello World without using a variable
print("Hello World")
#2.Swap two numbers without a third variable
a=1
b=2
a,b=b,a
print(a,b)
#3.Check whether a number is positive,negative or zero.
n=9
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")
#4.Find the largest of three numbers.
k=(10,20,30,90)
largest=0
for x in k:
    if x>largest:
        largest=x
print(largest)
#5.Check whether a number is even or odd.
m=2
if m%2==0:
    print("Even")
else:
    print("Odd")
#6.Calculate factorial
n=5
fac=1
for x in range(1,n+1):
    fac*=x
print(fac)
#7.Generate Fibonacci numbers.
n=5
a=0
b=1
for x in range(n):
    print(a)
    a,b=b,a+b
#8.Check whether a number is prime.
f = 5
count = 0
for x in range(1, f + 1):
    if f % x == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")
#9.Reverse an integer.
r=1234
rev=0
while r>0:
    rev=rev*10+r%10
    r//=10
print(rev)
#10.Find the sum of digits of a number.
k=123
sum=0
while k>0:
    sum=sum+k%10
    k//=10
print(sum)
#11.Reverse a string
n="Nandini"
rev=""
for x in n:
    rev=x+rev
print(rev)
#12.Check whether a string is palindrome.
h="afifa"
if h==h[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
#13.Count vowels and consonants.
m="Nandini"
vowel=0
consonant=0
for x in m.lower():
    if x in "aeiou":
        vowel+=1
    else:
        consonant+=1
print("Vowels:",vowel)
print("Consonants:",consonant)
#14.Count the frequency of every character
s="Nandini"
for x in s.lower():
    print(x,s.count(x))
#15.Find the first non-repeating character.
j="Nandini"
for char in j.lower():
    if j.lower().count(char)==1:
        print(char)
        break
#16.Remove duplicate characters from a string.
g="Nandini"
dup_str=""
for x in g.lower():
    if x not in dup_str:
        dup_str+=x
print(dup_str)
#17.Check whether two strings are anagrams.
n="silent"
m="listen"
if sorted(n)==sorted(m):
    print("Anagrams")
else:
    print("Not anagrams")
#18.Find the longest word in a sentence.
i="I am Kunchala Nandini"
longest=""
for x in i.split():
    if len(x)>len(longest):
        longest=x
print(longest) 
#19.Count words in a sentence.
p="I am Kunchala Nandini"
count=0
for x in p.split():
    count+=1
print(count)
#20. Remove duplicates from a list.
h=[10,20,10,30,10]
new_h=[]
for x in h:
    if x not in new_h:
        new_h.append(x)
print(new_h)
#21.Find maximum and minimum in a list without max()/min().
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
#22.Find the second-largest number.
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
#23.Reverse a list without reverse().
v=[10,20,30]
rev=[]
for x in v:
    rev=[x]+rev
print(rev)
#24. Find common elements between two lists.
k=[10,30,40,50]
l=[10,80,20,70,30]
common=[]
for x in k:
    if x in l:
        common.append(x)
print(common)
#25. Merge two sorted lists.
a=[10,20]
b=[30,40]
merge=[]
for x in a:
    merge.append(x)
for x in b:
    merge.append(x)
print(merge)
#26.Move all zeros to the end.
z=[0,20,0,40,50,0,60]
lis=[]
for x in z:
    if x!=0:
        lis.append(x)
for x in z:
    if x==0:
        lis.append(x)
print(lis)
#27.Find missing numbers from a sequence.
s= [1, 2, 4, 5, 7, 8]
for x in range(1, 9):
    if x not in s:
        print(x)
#28.Find unique elements using sets.
a = [10, 20, 10, 30, 20, 40]
unique = set(a)
print(unique)
#29.