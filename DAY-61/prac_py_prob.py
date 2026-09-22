#Write a Python program to count the number of vowels in a given string.
n=input("Enter string:")
count=0
for x in n.lower():
    if x in "aeiou":
        count+=1
print(count)