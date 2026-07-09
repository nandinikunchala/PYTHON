#1.Reverse a string.
a="Nandini"
reversed_string = a[::-1]#(start,stop,step)
print(reversed_string)

#2.Check whether a string is a palindrome.
a="nandu"
if a == a[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#3.Count the number of vowels in a string.
a="Nandini"
vowels = "aeiouAEIOU"
count = 0
for char in a:
    if char in vowels:
        count += 1
print(count)

#4.Count the number of consonants in a string.
a="Nandini"
vowels = "aeiouAEIOU"
count = 0
for char in a:
    if char not in vowels and char.isalpha():
        count += 1
print(count)

#5.Count the number of digits in a string.
a="Nandini123"
count = 0
for char in a:
    if char.isdigit():
        count += 1
print(count)

#6.Count the number of spaces in a string.
a="Nandini is a good dancer"
count = 0
for char in a:
    if char.isspace():
        count += 1
print(count)

#7.Count the number of special characters in a string.
a="Nandini@123"
count = 0
for char in a:
    if not char.isalnum() and not char.isspace():
        count += 1
print(count)

#8.Replace all spaces with underscores (_).
a="Nandini is a good dancer"
a = a.replace(" ", "_")
print(a)

#9.Remove all spaces from a string.
a="Nandini is a good dancer"
a = a.replace(" ", "")  
print(a)

#10.Check whether two strings are equal.
a="Nandini"
b="nandini"
if a == b:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

#11.Print the first 3 characters using slicing
a="Nandini"
print(a[0:3])

#12.Print the last 4 characters using slicing.
a="Nandini"
print(a[-4:])

#13.Print every second character using slicing.
a="Nandini"
print(a[::2])

#14.Print the string in reverse using slicing only.
a="Nandini"
print(a[::-1])

#15.Remove the first and last character using slicing.
a="Nandini"
print(a[1:-1])

#16.Swap the first and last characters of a string.
a="Nandini"
a = a[-1] + a[1:-1] + a[0]
print(a)

#17.Print characters at even indices.
a="Nandini"
print(a[::2])

#18.Print characters at odd indices.
a="Nandini"
print(a[1::2])

#19.Print characters at odd indices.
a="Nandini"
print(a[1::2])

#20.Convert every word's first letter to uppercase.
a="nandini is a good dancer"
a = a.title()
print(a)

#21.Toggle the case of every character.
a = "PyThOn"
result = ""
for char in a:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()
print(result)