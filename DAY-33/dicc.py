#dic problem
s="hi nandini"
count={}
for char in s:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
for char in count:
    if count[char]==3:
        print({char:count[char]})

        