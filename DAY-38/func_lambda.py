#LAMBDA FUNCTION
#A lambda is basically a small anonymous function.
# "Anonymous" means it normally doesn't have a regular function name.
#Lambda syntax is "lambda arguments: expression"
#Ex:lambda x: x + 10

#Why use lambda?
# Lambda becomes especially useful when we need a small function temporarily.
# One of the most common places you'll see it is with:
# map()
# filter()
# sorted()

#Lambda + map()
numbers = [1, 2, 3, 4]
result = map(lambda x: x ** 2, numbers)
print(list(result))
#map()=Apply that function to every element in numbers

#Lambda + filter()
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)#want only even numbers
print(list(result))
#filter() keeps the values for which the condition is True.

#Lambda + sorted()
students = [("A", 80), ("B", 60), ("C", 90)]
result = sorted(students, key=lambda x: x[1])#We want to sort based on marks.

#Problems
#Write a lambda function that takes a number and returns its square.
square=lambda x:x**2
print(square(2))

#Write a lambda function that takes two numbers and returns their sum.
sum=lambda x,y:x+y
print(sum(2,3))

#Write a lambda function that takes a number and checks whether it is even.
numbers=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0,numbers)
print(tuple(even))

#Use map() + lambda to double every number.
numbers = [1, 2, 3, 4, 5]
double=map(lambda x:x*2,numbers)
print(list(double))

#Use filter() + lambda to get only the even numbers.
numbers = [1, 2, 3, 4, 5, 6]
square=filter(lambda x:x%2==0,numbers)
print(list(square))

#Use map() + lambda to calculate the square of every number.
numbers = [1, 2, 3, 4, 5]
square=map(lambda x:x**2,numbers)
print(list(square))

#Use filter() + lambda to get numbers greater than 20.
numbers = [10, 15, 20, 25, 30]
num=filter(lambda x:x>20,numbers)
print(list(num))

#Use map() + lambda to find the length of every word.
words = ["python", "ai", "machine", "data"]
length=map(lambda x:len(x),words)
print(list(length))

#Use sorted() + lambda to sort the students according to their marks.
students = [("A", 80), ("B", 60), ("C", 90), ("D", 70)]
sort=sorted(students,key=lambda x:x[1])
print(sort)

#Use sorted() + lambda to sort the words according to their length.
words = ["python", "ai", "machine", "data", "code"]
length=sorted(words,key=lambda x:len(x))
print(length)

#Use sorted() + lambda to sort the numbers in descending order.
numbers = [5, 2, 8, 1, 9, 3]
des=sorted(numbers,key=lambda x:x,reverse=True)
print(des)

#Use filter() + lambda to get numbers that are divisible by 3.
numbers = [10, 15, 22, 33, 40, 51]
res=filter(lambda x:x%3==0,numbers)
print(list(res))

#Use map() + lambda to add 10 to every number.
numbers = [2, 5, 8, 11, 14, 17]
result=map(lambda x:x+10,numbers)
print(list(result))

#Use filter() + lambda to get numbers that are greater than 8 and less than 14.
numbers = [3, 6, 9, 12, 15]
num=filter(lambda x:x>8 and x<14,numbers)
print(list(num))

#Use sorted() + lambda to sort the students by marks in descending order.
students = [("A", 80), ("B", 60), ("C", 90), ("D", 70)]
descen=sorted(students,key=lambda x:x[1],reverse=True)
print(descen)