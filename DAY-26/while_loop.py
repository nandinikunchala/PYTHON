#print 1 to 5 using while loop
i=1
while i<=5:
    print(i)
    i+=1
#Print numbers from 5 to 1
i=5
while i>=1:
    print(i)
    i-=1 
#Print "Hello" 5 times
i=1
while i<=5:
    print("Hello")
    i+=1
#Print even numbers from 2 to 20
i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1

i=2
while i<=20:
    print(i)
    i+=2
#print odd numbers from 1 to 20
i=1
while i<=20:
    if i%2!=0:
        print(i)
    i+=1

i=1
while i<=20:
    print(i)
    i+=2
#Print the multiplication table of 5
i=1
while i<=10:
    print(5,"x",i,"=",5*i)
    i+=1
#Find the sum of numbers from 1 to 10
count=0
i=1
while i<=10:
    count+=i
    i+=1
print(count)
#Find the sum of even numbers from 1 to 10
count=0
i=1
while i<=10:
    if i%2==0:
        count+=i
    i+=1
print(count)
#Count numbers from 1 to 100 that are divisible by 5
count=0 
i=1
while i<=100:
    if i%5==0:
        count+=1
    i+=1
print(count)

count=0
i=5
while i<=100:
    count+=1
    i+=5
print(count)
#Take a number n from the user and print numbers from 1 to n
n=2
i=1
while i<=n:
    print(i)
    i+=1
#Find the factorial of a number
n=6
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)
#Count the number of digits in a number
num = 678
count = 0
while num > 0:
    count += 1
    num = num // 10
print(count)
#Find the sum of digits
n=9876
total=0
while n>0:
    digit=n%10
    total+=digit
    n//=10
print(total)
#Reverse anumber
n=1234
reverse=""#rev=0
while i>0:
    digit=n%10
    reverse=reverse+str(digit)#rev=rev*10+digit
    n//=10
print(reverse)






