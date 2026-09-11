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
# 21. Find maximum and minimum in a list without max()/min().
# 22. Remove duplicates from a list.
# 23. Find the second-largest number.
# 24. Reverse a list without reverse().
# 25. Find common elements between two lists.
# 26. Merge two sorted lists.
# 27. Move all zeros to the end.
# 28. Find missing numbers from a sequence.
# 29. Rotate a list by k positions.
# 30. Find duplicate elements.
# 31. Count word frequency using a dictionary.
# 32. Find the most frequent element.
# 33. Group words that are anagrams.
# 34. Invert a dictionary.
# 35. Merge two dictionaries.
# 36. Find common keys between dictionaries.
# 37. Find unique elements using sets.
# 38. Build a student grade tracker.
# 39. Create a phone-book application.
# 40. Create a dictionary-based inventory system.