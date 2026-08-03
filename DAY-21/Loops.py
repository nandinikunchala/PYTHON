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
# Print the multiplication table of a given number.
# Count the number of digits in a given number.
# Find the sum of digits of a number.
# Reverse a given number.
# Check whether a number is a palindrome.
# Find the largest digit in a number.
# Find the smallest digit in a number.
# Print each digit of a number on a new line.
# Count the number of even and odd digits in a number.