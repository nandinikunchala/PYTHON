#Write a function to find the maximum of two numbers
def max(a,b):
    if a>b:
        return a
    else:
        return b
num1=8
num2=9
result=max(num1,num2)
print("Maximum number is",result)
#Write a function to check whether a number is even or odd
def even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
number=7
result=even_odd(number)
print("number is",result)
#Write a function to count vowels in a string
def count_vowels(text):
    count=0
    for char in text.lower():
        if char in "aeiou":
            count+=1
    return count
string="I am Nandini"
result=count_vowels(string)
print(result)
