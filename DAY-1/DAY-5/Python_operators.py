#Python Operators
#operators are used to perform operations on variables and values

#Arithmetic operators:
#arithmetic operators are used with numeric values to perform common mathematical operations
x = 15
y = 4
print(x + y)#Addition
print(x - y)#Subtraction
print(x * y)#Multiplication
print(x / y)#Division
print(x % y)#Modulus
print(x ** y)#Exponentiation
print(x // y)#Floor division

#Assignment operators
# =	    x = 5    x = 5	
# +=	x += 3	 x = x + 3	
# -=	x -= 3	 x = x - 3	
# *=	x *= 3	 x = x * 3	
# /=	x /= 3	 x = x / 3	
# %=	x %= 3	 x = x % 3	
# //=	x //= 3	 x = x // 3	
# **=	x **= 3	 x = x ** 3	
# &=	x &= 3	 x = x & 3	
# |=	x |= 3	 x = x | 3	
# ^=	x ^= 3	 x = x ^ 3	
# >>=	x >>= 3	 x = x >> 3	
# <<=	x <<= 3	 x = x << 3	
# :=	print(x := 3) #walrus operator

#Ternary operator
#Allows to assign one value if a condition is true,and other if it is false
num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)

#The ternary operator can be used instead of elif in longer if statements
num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print(x)

#Comparision operators
#used to compare two values
x = 5
y = 3

print(x == y)#equal
print(x != y)#not equal
print(x > y)#greater than
print(x < y)#less than
print(x >= y)#greater than or equal to
print(x <= y)#less than or equal to

#Chaining operators
#python allows to chain comparision operator
x = 5
print(1 < x < 10)
print(1 < x and x < 10)

#Logical operators
#used to combine conditional statements
x = 5
print(x > 0 and x < 10)#returns true if both statements are true
print(x < 5 or x > 10)#returns true if one statement is true
print(not(x > 3 and x < 10))#reverse the the result (boolean value)

#Identity operators
#used to compare the objects,not if they are eual,but if they are actually the same object,with same memory location
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)#returns true both variables are same
print(x is y)#returns false both variables are not same 
print(x == y)#returnd true both variables are same
print(x is not y)#returns true both variables are not equal

#Difference between is and ==
#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

#Membership operators
#used to test if a sequence is presented in an object
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)#return true
print("pineapple" not in fruits)#returns true

#Membership in Strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#Bitwise operators
# & 	AND		
# |	OR	
# ^	XOR	
# ~	NOT	
# <<  left shift	
# >>  right shift

#operator precedence
# ()	
# **		
# +x  	
# *  /  //  %		
# +  -		
# <<  >> 	
# &		
# ^		
# |	 
# ==  !=  >  >=  <  <=  
# not		
# and	
# or
#left to right evaluation