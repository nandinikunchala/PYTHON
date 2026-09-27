#RECURSION
#Recursion means a function calling itself.
#Recursion means a function calls itself to solve a problem.
#Print numbers from 5 down to 1.
def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)
count(5)
#Recursion = Function calling itself + a stopping condition

#BASE CASE(stops recursion)
# The base case tells recursion:
# "STOP! Don't call the function again."
def count(n):
    if n == 0:#base case because when n becomes 0 we stop
        return

#RECURSIVE CASE(continuos recursion)
#The recursive case is where the function calls itself.
def count(n):
    if n == 0:
        return

    print(n)
    count(n - 1)#RECURSIVE CASE because it is calling itself

#FIBONACCI SEQUENCE
#Find the 7th number in the Fibonacci sequence:
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))

