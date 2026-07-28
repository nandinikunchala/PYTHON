#1.Count the occurrences of a given character in a string.
a = "Nandini"
char_to_find = "n"
count = 0
for char in a:
    if char == char_to_find:
        count += 1
print(count)

#2.Remove duplicate characters from a string
a = "programming"
result = ""
for char in a:
    if char not in result:
        result += char
print(result)

#3.Find the first non-repeating character in a string
a = "programming"

for char in a:
    count = 0

    for ch in a:
        if char == ch:
            count += 1

    if count == 1:
        print(char)
        break

#4.Check whether two strings are anagrams
a = "listen"
b = "silent"

if sorted(a) == sorted(b):
    print("Anagrams")
else:
    print("Not Anagrams") 

#5.Compress a string (Example: aaabbcc → a3b2c2)
a = "aaabbcc"
result = ""
count = 1
for i in range(len(a)):
    if i + 1 < len(a) and a[i] == a[i + 1]:
        count += 1
    else:
        result += a[i] + str(count)
        count = 1
print(result)   

#6.Reverse each word in sentence
sentence = "Hello Python World"
words = sentence.split()
result = ""
for word in words:
    result += word[::-1] + " "
print(result)

#7.Reverse the order of words in a sentence
sentence = "I love Dance"
words = sentence.split()
reversed_sentence = ""
for word in words[::-1]:
    reversed_sentence += word + " "
print(reversed_sentence)

#8.Find the longest word in a sentence
sentence = "I love programming language"
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)

#9.Find all duplicate characters in a string
a = "programming"
duplicates = ""
for char in a:
    if a.count(char) > 1 and char not in duplicates:
        duplicates += char
print(duplicates)

#10.Check whether one string is a rotation of another.
a = "ABCD"
b = "CDAB"
if len(a) == len(b) and b in (a + a):
    print("Rotation")
else:
    print("Not a Rotation")