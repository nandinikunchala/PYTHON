#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

#An "if statement" is written by using the if keyword.
a = 33
b = 200
if b > a:
  print("b is greater than a")

# The if statement evaluates a condition (an expression that results in True or False). 
# If the condition is true, the code block inside the if statement is executed. 
# If the condition is false, the code block is skipped.
number = 15
if number > 0:
  print("The number is positive")
# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
# Other programming languages often use curly-brackets for this purpose.

# Multiple Statements in If Block
# You can have multiple statements inside an if block. All statements must be indented at the same level.
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

# Using Variables in Conditions
# Boolean variables can be used directly in if statements without comparison operators.
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
# Python can evaluate many types of values as True or False in an if statement.
# Zero (0), empty strings (""), None, and empty collections are treated as False.Everything else is treated as True.
# This includes positive numbers (5), negative numbers (-3), and any 
# non-empty string (even "False" is treated as True because it's a non-empty string).

#Elif Keyword
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#The elif keyword allows you to check multiple expressions for True and 
#execute a block of code as soon as one of the conditions evaluates to True.
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#Multiple Elif Statements
#You can have as many elif statements as you need. 
#Python will check each condition in order and execute the first one that is true.
score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#When you use elif, Python evaluates the conditions from top to bottom. 
#As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.

age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

# Use elif when you have multiple mutually exclusive conditions to check. 
#This is more efficient than using multiple separate if statements because Python 
#stops checking once it finds a true condition.
day = 3
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#Else Statements
#The else keyword catches anything which isn't caught by the preceding conditions.
# The else statement is executed when the if condition (and any elif conditions) evaluate to False.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Else Without Elif
# You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# The else statement provides a default action when none of the previous conditions are true. 
#Think of it as a "catch-all" for any scenario not covered by your if and elif statements.
# The else statement must come last. You cannot have an elif after an else.
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

# Complete If-Elif-Else Chain
# You can combine if, elif, and else to create a comprehensive decision-making structure.
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

# Else as Fallback
# The else statement acts as a fallback that executes when none of the preceding conditions are true. 
# This makes it useful for error handling, validation, and providing default values.
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

# Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression
a = 2
b = 330
print("A") if a > b else print("B")
# This is called a conditional expression (sometimes known as a "ternary operator").

# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# The syntax follows this pattern:
# variable = value_if_true if condition else value_if_false

# Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print(B)


# Ternary operators are particularly useful for simple assignments and return statements.
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

# When to Use Shorthand If
# Shorthand if statements and ternary operators should be used when:

# The condition and actions are simple
# It improves code readability
# You want to make a quick assignment based on a condition
# Important: While shorthand if statements can make code more concise, avoid overusing them for complex conditions. 
# For readability, use regular if-else statements when dealing with multiple lines of code or complex logic.

#Python Logical Operators
# Logical operators are used to combine conditional statements. Python has three logical operators:

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

# The and Operator
# The and keyword is a logical operator, and is used to combine conditional statements. 
# Both conditions must be true for the entire expression to be true.
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# The or Operator
# The or keyword is a logical operator, and is used to combine conditional statements. 
# At least one condition must be true for the entire expression to be true.
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# The not Operator
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Nested If Statements
#You can have if statements inside if statements. This is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#he pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content,
#  put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass
# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.

# Why Use pass?
# The pass statement is useful in several situations:
# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later
# pass in Development

