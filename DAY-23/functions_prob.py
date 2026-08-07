#Write a function to find the maximum of two numbers
# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# m,n=map(int,input().split(","))
# print(max(m,n))
#Write a function to check whether a number is even or odd
def even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
print(even_odd(7))
#Write a function to count vowels in a string
def count_vowels(text):
    count=0
    for char in text.lower():
        if char in "aeiou":
            count+=1
    return count
print(count_vowels("nandini"))

#Write a function to add two numbers.
def add(a,b):
    return(a+b)
print(add(6,7))

#Write a function to find the minimum of two numbers.
def min(a,b):
    if a<b:
        return a
    else:
        return b
print(min(4,4))

#Write a function to check whether a number is positive, negative, or zero.
def check(num):
    if num<0:
        return("negative")
    elif num>0:
        return("positive")
    else:
        return("Zero")
print(check(0))

#Write a function to find the square of a number
def square(num):
    return num*num
print(square(5))

#Write a function to find the maximum of three numbers.
def max_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(max_three(2,6,4))

#Write a function to check whether a number is divisible by 5.
def num_div(num):
    return num%5==0
print(num_div(25))

#Write a function to check whether a number is prime.
def prime(num):
    for i in range(1, num + 1):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 2:
            print(i)

prime(7)

