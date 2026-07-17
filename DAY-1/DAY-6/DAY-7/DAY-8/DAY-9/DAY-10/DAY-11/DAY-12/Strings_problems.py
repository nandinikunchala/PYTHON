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
