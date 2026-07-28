#1.Sum of Two Numbers
a=10
b=20
c=(a+b)
print(c)

#2.Perform Arithmetic Operations
print(a+b)#addition
print(a-b)#subtraction
print(a*b)#Multiplication
print(a/b)#Division
print(a//b)#floor division
print(a**b)#Exponentiation
print(a%b)#Modulus

#3.Find Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#4.Swap Two Numbers Without Using a Third Variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping")
print("a =", a)
print("b =", b)

#5.Take a number as input and perform the assignment operators
x=int(input("Enter value"))
x+=2
print(x)
x-=2
print(x)
x*=2
print(x)
x/=2
print(x)
x//=2
print(x)
x%=2
print(x)
x**=2
print(x)

#6.Take two numbers as input and print the greater number using the ternary operator.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"{a} is greater" if a > b else f"{b} is greater")

#7.Take two numbers as input and compare them using all comparison operators.
x==2
print(x)
x!=2
print(x)
x>2
print(x)
x<2
print(x)
x<=2
print(x)
x>=2
print(x)

#8.Take a person's age and check whether they are eligible to vote.
age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")

if age >= 18 and citizen == "yes":
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

#9.Check whether two variables refer to the same object in memory using identity operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b :", a == b)
print("a is b :", a is b)
print("a is c :", a is c)
print("a is not b :", a is not b)

#10.Check whether a character exists inside a string using membership operators
text = input("Enter a string: ")
char = input("Enter a character to search: ")

print(char in text)
print(char not in text)

#11.Take two numbers as input and perform bitwise operators
a = 5
b = 8

print("AND :", a & b)
print("OR :", a | b)
print("XOR :", a ^ b)
print("NOT of a :", ~a)
print("Left Shift of a :", a << 2)
print("Right Shift of a :", a >> 2)

#12.Find the output of expressions using Python's operator precedence rules.
print(10 + 5 * 2)
print((10 + 5) * 2)
print(2 ** 3 * 4)
print(True or False and False)
x = 5
print(x + 3 > 10 and x * 2 == 10)
