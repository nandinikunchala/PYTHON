#Print each character of a string using a loop.
name="Nandini"
for char in name:
    print(char)
# Count the number of characters in a string without using len().
name="Nandini"
count=0
for char in name:
    count+=1
print(count)
# Count the number of vowels.
name="Nandini"
count=0
for char in name.lower():
    if char in "aeiou":
        count+=1
print(count)
# Count the number of consonants.
name="Nandini12"
count=0
for char in name.lower():
    if char.isalpha() and char not in "aeiou":
        count+=1
print(count)
# Count uppercase and lowercase letters separately.
name="Sowbhagya"
upper=0
lower=0
for char in name:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1
print(upper)
print(lower)
# Count the number of digits in a string.
name="Laxmi123"
count=0
for char in name:
    if char.isdigit():
        count+=1
print(count)
# Count the number of spaces.
name="nan lak "
count=0
for char in name:
    if char==" ":
        count+=1
print(count)
# Reverse a string without using slicing ([::-1]).
name="Shivani"
rev=""
for char in name:
    rev=char+rev
print(rev)
# Check whether a string is a palindrome.
name="Gayatri"
if name==name[::-1]:
    print("palindrome")
else:
    print("Not palindrome")   
# Find the first occurrence of a character.
name="Nandu"
print(name.find("N"))
# Find the last occurrence of a character.
print(name.find("u"))
# Count how many times a character appears.
name="afifa"
char="a"
count=name.count(char)
print(count)
# Convert lowercase letters to uppercase without using .upper().
name="pavani"
result=""
for char in name:
  result+=chr(ord(char)-32)
print(result)
# Convert uppercase letters to lowercase without using .lower().
name="AKHILA"
result=""
for char in name:
  result+=chr(ord(char)+32)
print(result)
# Remove all spaces from a string.
name="kun cha la"
result=""
for char in name:
    if char!=" ":
        result+=char
print(result)
# Replace every vowel with *.
name="Nandu"
result=""
for char in name.lower():
   if char in "aeiou":
       result+="*"
   else:
       result+=char
print(result)
# Print characters at even indices.
name="Pallavi"
for i in range(0,len(name),2):
    print(name[i],end="")
print()
# Print characters at odd indices.
a="Bhargavi"
for i in range(1,len(a),2):
    print(a[i],end="")
print()
# Find the longest word in a sentence.
x="Hello, I'm Nandini."
words=x.split()
longest=""
for word in words:
    if len(word)>len(longest):
        longest=word
print(longest)
# Find the shortest word in a sentence.
x="Hello, I'm Nandini."
words=x.split()
shortest=words[0]
for word in words:
    if len(word)<len(shortest):
        shortest=word
print(shortest)


#MEDIUM PROBLEMS
# Count the frequency of every character.
b="Manasa"
target="a"
print(b.count(target))
# Count the frequency of every word.
c="Satwika is rupa friend"
words=c.split()
frequency= {}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print(frequency)
# Remove duplicate characters.
d="Nandini"
result=""
for char in d.lower():
    if char not in result:
        result+=char
print(result)
# Print duplicate characters only.
e = "Nandini"
result = ""
for char in e.lower():
    if char in e.lower() and e.lower().count(char) > 1:
        if char not in result:
            result += char
print(result)
# Find the first non-repeating character.
f="Madhav"
count=0
for char in f:
    if f.count(char)==1:
        print(char)
        count+=1
        if count==2:
            break
# Find the first repeating character.
g="Madhav"
for char in g:
   if g.count(char)>1:
       print(char)
       break
# Check whether two strings are anagrams.
h="heart"
i="earth"
if sorted(h)==sorted(i):
    print("anagrams")
else:
    print("Not anagrams")
# Check whether two strings are rotations of each other.
j="ABCD"
k="CDAB"
if len(j)==len(k) and k in (j+j):
    print("Rotation")
else:
    print("No rotation")
# Remove all vowels.
l="Nandu"
result="" 
for char in l:
    if char.lower() not in "aeiou":
        result+=char
print(result)
# Remove all special characters.
m="Nandy@!2185"
result=""
for char in m:
    if char.isalnum():
        result+=char
print(result)
# Count the number of words.
n="Nandy"
count=0
for char in n:
    count+=1
print(count)
# Reverse each word in a sentence.
o="Nandini and Shivani are Friends"
words=o.split()
result=""
for word in words:
   rev=""
   for char in word:
     rev=char+rev

   result+=rev+" "
print(result)
#Reverse the order of words.
p="Veda and Nandini are friends"
words=p.split()
for i in range(len(words)-1,-1,-1):
    print(words[i],end=" ")
print()
# Capitalize the first letter of every word without using .title().
q="nandu is also nandini"
words=q.split()
result=""
for word in words:
    new_word=word[0].upper()+word[1:]
    result+=new_word +" "
print(result)
# Find the most frequent character.
s = "afifa"
most = max(s, key=s.count)
print(most)
# Find the least frequent character.
s = "afifa"
least = min(s, key=s.count)
print(least)
# Compress a string.
# Example:
# aaabbccccd
# Output:
# a3b2c4d1
s = "aaabbccccd"
result = ""
for char in set(s):
    result += char + str(s.count(char))
print(result)
# Expand a compressed string.
# Example:
# a3b2c4
# Output:
# aaabbcccc
s = "a3b2c4"
result = ""
for i in range(0, len(s), 2):
    char = s[i]
    count = int(s[i+1])
    result += char * count
print(result)
# Check whether one string is a subsequence of another.
s1 = "abc"
s2 = "aebdc"
i = 0
for ch in s2:
    if i < len(s1) and ch == s1[i]:
        i += 1
print(i == len(s1))
# Check whether all characters are unique.
s = "apple"
if len(s) == len(set(s)):
    print("Unique")
else:
    print("Not Unique")