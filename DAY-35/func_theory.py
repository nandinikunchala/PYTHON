#function
# A function is a block of code which only runs when it is callled.
#A function can return data as result
# A function helps avoiding code repetiion.

#Creating a function
#A function is defined using the def keyword,followed by a function name and parentheses

#Calling a function
#To call a function,write its name followed by parentheses.
#We can call the same function multiple times.

#Function names/rules:
#1.Function names follow the same rules as variable names in python
#2.A function name must start with a letter or underscore.
#3.A function name can only contain letters,numbers and underscores.
#4.Function names are case-sensitive(myFunction and myfunction are different)

#Why use functions
#If we want to convert temp from farenheit to celsius several times in program without functions,we would 
#have to write the same calculation code multiple times
#With functions,we can write code one & reuse it.

#Return values
#functions can send data back to the code that called them using the return statement.When a function reaches a 
#return statement ,it stops executing and sends the result back.We can use the returned valye directly.
#If a function doesn't have a return statement, it returns none by default.

#Pass statement
#function definitions cannot be empty.If you need to create a function placeholder without any code,use the pass statement

#Python Arguments
#information can be passed into functions as arguments
#arguments are specified after the function name,inside the parenthesis.We can add as many arguments as,separate with comma.

#Parameters vs arguments
#the term parameter and argument can be used for the same thing:information that are passed into function
# A parameter is the variable listed inside the paranthesis in function definition
# An argument is the actual value that is sent to the function when it is called.

#No.of arguments
#a function must be called with the correct no.of argument
#if your function expects 2 arguments, you must call it with exactly 2 arguments
#if we try to call with wrong no.of arguments,it gives error.

#Default parameter values:
#We can assign default values to parameters.if the function is called without an argument, it uses default value.

#Keyword Arguments
#We can send arguments with thw key=value syntax.
#the order of the arguments does not matter.
#the phrase keyword arguments is often shortend to kwargs in python.

#Positional arguments
#when we calll a function without using keywords ,they are called positional arguments.
#positional arguments must be in correct order.

#Mixing positional and keyword arguments
#We can mix positional and keyword arguments in a functional cell.However,positional arguments come before keyword arguments.

#Passing different data types
#we can send any data type as an argument to a function(string,number,list,dictionary,etc)
#The data type will be preserved inside the function.

#Return values
#functions can return values using return statements

#Returning different data types
#functions can return any data type,including lists,tuples,dictionaries and more

