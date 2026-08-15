#1.count the number of words in a string
x="Nandini"
count=0
for i in x:
    count+=1
print(count)
#2.Palindrome check
n=21212
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if original==rev:
    print("Palindrome")
elif original!=rev:
    print("Not palindrome")
else:
    print("Invalid Input")
#3.Buzz checker
m=42
if m%10==7 or m%7==0:
    print("Buzz number")
else:
    print("Not a Buzz number")
#4.Second largest number
def sec_largest(d):
    largest=0
    second_largest=0
    for x in d:
       if x>largest:
          second_largest=largest
          largest=x
    return second_largest
print(sec_largest([10,20,30,40]))
#5.reverse an integer
def rev_integer(c):
   rev=0
   while c>0:
     digit=c%10
     rev=rev*10+digit
     c=c//10
   return rev
print(rev_integer(4587))

#6.count vowels
def count_vowels(s):
    count=0
    for char in s.lower():
       if char in "aeiou":
            count+=1
    return count
print(count_vowels("Nandini"))
#7.string palindrome
def string_palindrome(f):
        if f==f[::-1]:
            return "Palindrome"
        else:
            return "Not Palindrome"
print(string_palindrome("afifa"))
#8.reverse a string
def rev_string(h):
    rev=""
    for ch in h:
        rev=ch+rev
    return rev
print(rev_string("Nandini"))
#9.generate a bill for vohras purchase
a=int(input("Enter number of pizzas:"))
b=int(input("Enter number of puffs:"))
c=int(input("Enter number of cool drinks:"))
print("Number of pizzas:",a)
print("Number of puffs:",b)
print("Number of cooldrinks:",c)
total=(a*100)+(b*20)+(c*10)
print("Total Price:",total)
