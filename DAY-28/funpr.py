#Create a function greet() that takes a name and prints
def greet():
    print("Hello")
greet()
#Create a function that takes two numbers and prints their sum.
def sum(a,b):
    return a+b
print(sum(5,6))
#Create a function that takes a number and prints whether it is even or odd.
def even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(even_odd(8))
#Create a function that takes a number and returns its square.
def square(n):
    return n*n
print(square(3))
#Create a function to find the largest of two numbers.
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(5,9))
#Create a function that returns the factorial of a number.
def fac(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(fac(5))

def fac(n):
    i=1
    fact=1
    while i<=n:
        fact*=i
        i+=1
    return fact
print(fac(4))

#count digits
def count(num):
    count=0
    while num>0:
        digit=num%10
        count+=1
        num//=10
    return count
print(count(2354))
#reverse digits
def rev(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    return rev
print(rev(4587))
#sum of digits
def sum(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n//=10
    return sum
print(sum(567))
#palindrome(String)
def palindrome(n):
    if n==n[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
print(palindrome("afifa"))

def pal(n):#num
    original=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    if original==rev:
        return True
    else:
        return False
print(pal(77777))


