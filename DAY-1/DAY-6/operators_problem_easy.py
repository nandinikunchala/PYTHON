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

