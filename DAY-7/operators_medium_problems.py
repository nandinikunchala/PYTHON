#1.Write a Python program to find the largest number among two numbers
a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
if a>b:
    print(a,"is greater")
else:
    print(b,"is greater")

#2.Find the Largest of Three Numbers
x=int(input("Enter number:"))
y=int(input("Enter number:"))
z=int(input("Enter number:"))
if x>=y and x>=z:
    print(x,"is greater")
elif y>=x and y>=z:
    print(y,"is greater")
else:
    print(z,"is greater")

#3.Write a Python program to check whether a person is eligible to vote.
age = int(input("Enter your age: "))
voter_id = input("Do you have voter ID? (yes/no): ")

result = "Eligible to Vote" if age >= 18 and voter_id == "yes" else "Not Eligible to Vote"
print(result)

#4.Write a Python program to check whether a number is positive,negatiive or 0
num=int(input("Enter a value:"))
if num<0:
    print(num,"is Negative")
elif num>0:
    print(num,"is positive")
else:
    print("Number is zero")

#5.Write a Python program to check whether a number is divisible by both 5 and 11.
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")

#6.Write a Python program to check whether a given year is a leap year or not.
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

#7.Write a Python program to calculate the final price after applying a discount.
amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
else:
    discount = 0

final_price = amount - discount

print("Discount:", discount)
print("Final Price:", final_price)

#8.Write a Python program to calculate the final price after applying a discount.
amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
else:
    discount = 0

final_price = amount - discount

print("Discount:", discount)
print("Final Price:", final_price)

#9.Write a Python program to calculate an electricity bill.
units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5

elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

print("Electricity Bill:", bill)

#10.Write a Python program to calculate an employee's bonus.
salary = float(input("Enter salary: "))

if salary > 50000:
    bonus = salary * 0.10

elif salary >= 30000:
    bonus = salary * 0.05

else:
    bonus = salary * 0.02

total_salary = salary + bonus

print("Bonus:", bonus)
print("Total Salary:", total_salary)

#11.Write a Python program to calculate movie ticket price based on age.
age=int(input("Enter age:"))
if age<12:
    print("Ticket price ₹100.")
elif age >=12 and age<60:
    print("Ticket price is ₹200.")
else:
    print("Ticket price is ₹150")

#12.Write a Python program to calculate a student's grade based on marks
marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 35:
    grade = "D"

else:
    grade = "Fail"

print("Grade:", grade)

#13.Write a Python program to simulate an ATM withdrawal
balance = int(input("Enter account balance: "))
amount = int(input("Enter withdrawal amount: "))

if amount > 0 and amount <= balance and amount % 100 == 0:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)

else:
    print("Invalid Withdrawal")

#14.Create a login system.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Invalid Username or Password")

#15.Write a Python program to check whether a number belongs to a given range.
num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Number is in range")
else:
    print("Number is outside the range")

#15.Create a calculator that performs:Addition,Subtraction,Multiplication,Division
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

else:
    result = "Invalid Operator"

print("Result:", result)