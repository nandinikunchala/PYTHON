#Check whether a number is positive.
n=6
if n>0:
    print(n,"is positive")
# Check whether a number is negative.
m=-7
if m<0:
    print(m,"is negative")
# Check whether a number is zero.
k=0
if k==0:
    print(k,"is zero")
# Check whether a number is even.
if n%2==0:
    print(n,"is even")
# Check whether a number is odd.
if n%2!=0:
    print(n,"is odd")
# Check whether a person is eligible to vote based on age.
age=20
if age>=18:
    print("Person is eligible to vote")
# Check whether a person is eligible for a driving license based on age.
age=16
if age>=18:
    print("Person is eligible for a driving license")
# Check whether a number is greater than 10.
if n>10:
    print(n,"is greater than 10")
# Check whether a number is divisible by 5.
if n%5==0:
    print(n,"is divisible by 5")
# Check whether a character is a vowel.
char='a'
if char in 'aeiouAEIOU':
    print(char,"is a vowel")
# Check whether a character is an uppercase letter.
char='A'
if char.isupper():
    print(char,"is an uppercase letter")
# Check whether a number is a multiple of 10.
if n%10==0:
    print(n,"is a multiple of 10")
# Check whether a student has passed based on marks.
marks=75
if marks>=40:
    print("Student has passed")
# Check whether a person is eligible for a scholarship based on marks.
marks=85
if marks>=90:
    print("Person is eligible for a scholarship")
# Check whether a number is divisible by both 3 and 5.
if n%3==0 and n%5==0:
    print(n,"is divisible by both 3 and 5")

#Medium
#Check whether a number is even or odd.
if n%2==0:
    print("Even")
else:
    print("Odd")
# Check whether a number is positive or negative.
if n>0:
    print("Positive")
else:
    print("Negative")
# Check whether a person is eligible to vote or not.
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")
# Check whether a student has passed or failed.
if marks>40:
    print("Passed")
else:
    print("Failed")
# Check whether a number is divisible by 7 or not.
if n%7==0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")
# Check whether a character is a vowel or consonant.
if char in"aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
# Check whether a number is a two-digit number or not.
if n>=10 and n<=99:
    print("Two digit number")
else:
    print("Not a two digit number")
# Check whether a year is a leap year or not.
year=int(input("Enter a year:"))
if year%4==0 and (year%100!=0 or year%400==0):
    print("leap year")
else:
    print("Not a leap year")
# Check whether a person is eligible for a driving license or not.
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")
# Check whether a number is divisible by both 2 and 3 or not.
if n%2==0 and n%3==0:
    print("Divisible by both 2 and 3")
else:
    print("Not divisible by both 2 and 3")

#Hard
#Find the largest of two numbers.
if n>m:
    print(n,"is largest")
else:
    print(m,"is largest")
# Find the largest of three numbers.
if n>m and n>k:
    print(n,"is largest")
elif m>n and m>k:
    print(m,"is largest")
else:
    print(k,"is largest")
# Find the smallest of three numbers.
if n<m and n<k:
    print("n, is smallest")
elif m<n and m<k:
    print("m, is smallest")
else:
    print("k, is smallest")
# Check whether a number is positive, negative, or zero.
if n<0:
    print("Negative")
elif n>0:
    print("Positive")
else:
    print("Zero")
# Print whether a number is one-digit, two-digit, or three-digit.
if n<10:
    print("One digit number")
elif n<100:
    print("Two digit number")
else:
    print("Three digit number")
# Print grades based on marks.
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
else:
    print("Grade C")
# Calculate electricity bill based on units consumed.
units=int(input())
if units<=100:
    bill=units*5
elif units<=200:
    bill=100*5+(units-100)*10
else:
    bill=100*5+100*10+(units-200)*15
print("Electricity bill:", bill)
# Calculate a discount based on the purchase amount.
purchase_amount=int(input())
if purchase_amount>1000:
    discount=purchase_amount*0.1
print("Discount:", discount)
# Check whether a person is a child, teenager, adult, or senior citizen based on age.
if age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior Citizen")
# Print the day of the week based on a number from 1 to 7.
day=int(input("Enter a number from 1 to 7:"))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
# Print the month name based on a number from 1 to 12.
month=int(input("Enter a number from 1 to 12:"))
if month==1:
    print("January")
elif month==2:
    print("February")
elif month==3:
    print("March")
elif month==4:
    print("April")
elif month==5:
    print("May")
elif month==6:
    print("June")
elif month==7:
    print("July")
elif month==8:
    print("August")
elif month==9:
    print("September")
elif month==10:
    print("October")
elif month==11:
    print("November")
elif month==12:
    print("December")
# Create a simple calculator using an operator (+, -, *, /).
operator=int(input())
if operator=='+':
    print(n+m)
elif operator=='-':
    print(n-m)
elif operator=='*':
    print(n*m)
elif operator=='/':
    print(n/m)
# Check whether a character is an uppercase letter, lowercase letter, digit, or special character.
if char.isupper():
    print("Uppercase letter")
elif char.islower():
    print("Lowercase letter")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")
# Check whether three sides can form a triangle.
a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    print("Can form a triangle")
# Determine whether a triangle is equilateral, isosceles, or scalene.
if a==b and b==c:
    print("Equilateral triangle")
elif a==b or b==c or a==c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")