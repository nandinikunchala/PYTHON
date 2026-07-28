#1.Print the string "Hello, Python!"
print("Hello, Python!")

#2.Take a string as input and print it
name=input("Enter your name: ")
print(name)

#3.Take your name as input and print Hello <name>.
name=input("Enter your name: ")
print("Hello " + name)

#4.Print the first character of a string.
a="Nandini"
print(a[0])

#5.Print the last character of a string.
a="Nandini" 
print(a[-1])

#6.Print the second character of a string.
a="Nandini"
print(a[1])

#7.Print the middle character of a string (assume the length is odd).
a="Nandini"
middle_index = len(a) // 2
print(a[middle_index])

#8.Find the length of a string without using len()
a="Nandini"
count = 0
for char in a:
    count += 1
print(count)

#9.Convert a string to uppercase.
a="nandini"
print(a.upper())

#10.Convert a string to lowercase.
a="NANDINI"
print(a.lower())

#11.Capitalize the first letter of a string.
a="nandini"
print(a.capitalize())

#12.Check whether a string is empty or not.
a=input("Enter a string: ")
if a== "":
    print("The string is empty.")
else:
    print("The string is not empty.")

#13.Print each character of a string on a new line.
a="Nandini"
for char in a:
    print(char)

#14.Count the number of uppercase letters in a string.
a="Nandini"
count = 0
for char in a:
    if char.isupper():
        count += 1
print(count)

#15.Count the number of lowercase letters in a string.
a="Nandini"
count = 0
for char in a:
    if char.islower():
        count += 1
print(count)

