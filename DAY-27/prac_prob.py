#count vowels
n="Nandini"
count=0
for char in n.lower():
    if char in "aeiou":
        count+=1
print(count)
#first non repeating character
m="Nandini"
for char in m.lower():
    if m.count(char)==1:
        print(char)
        break

