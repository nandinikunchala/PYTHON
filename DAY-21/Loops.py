#prime numbers from 1-10
n=10
for i in range(2,n+1):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
    if prime:
        print(i)

#Easy
#Print numbers from 1 to 10.
for i in range(1,11):
    print(i)
# Print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i)
# Print all even numbers from 1 to 100.
for i in range(1,101):
    if i%2==0:
        print(i)
# Print all odd numbers from 1 to 100.
for i in range(1,101):
    if i%2!=0:
        print(i)
# Find the sum of the first n natural numbers..
n=2
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
# Find the product of the first n natural numbers.
n=5
product=1
for i in range(1,n+1):
    product*=i
print(product)
# Print the multiplication table of a given number.
n=5
for i in range(1,11):
    print(n,"*",i,"=",n*i)
# Count the number of digits in a given number.
n=12345
count=0
while n>0:
    n//=10
    count+=1
print("Number of digits:", count)
# Find the sum of digits of a number.
n=12345
sum=0
while n>0:
    sum+=n%10
    n//=10
print("Sum of digits:", sum)
# Reverse a given number.
n=12345
reverse=0
while n>0:
    reverse=reverse*10+n%10
    n//=10
print("Reversed number:", reverse)
# Check whether a number is a palindrome.
n=12321
original=n
reverse=0
while n>0:
    reverse=reverse*10+n%10
    n//=10
if original==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
# Find the largest digit in a number.
n=12345
largest=0
while n>0:
    if n%10>largest:
        largest=n%10
    n//=10
print("Largest digit:", largest)
# Find the smallest digit in a number.
n=12345
smallest=9
while n>0:
    if n%10<smallest:
        smallest=n%10
    n//=10
print("Smallest digit:", smallest)
# Print each digit of a number on a new line.
n=12345
while n>0:
    print(n%10)
    n//=10
# Count the number of even and odd digits in a number.
n=12345
even_count=0
odd_count=0
while n>0:
    if n%10%2==0:
        even_count+=1
    else:
        odd_count+=1
    n//=10
print("Even digits:", even_count)
print("Odd digits:", odd_count)