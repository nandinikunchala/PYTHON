#Variables
#Variables are containers for storing data values
#To get the data type of a variable, use the type() function.
#String variables are declared by using quotes, either single or double.
#To specify the data type of a variable, we can use casting.
#variables are not dynamic.


#RULES FOR PYTHON VARIABLES
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# Cannot use python keywords as variable names (e.g., if, else, while, for, etc.)


#MULTI WORDS VARIABLES NAMES
#Variable names with more than one word can be difficult to read.
#There are several techniques you can use to make them more readable:
#Camel Case: Each word, except the first, starts with a capital letter: myVariableName
#Pascal Case: Each word starts with a capital letter: MyVariableName
#Snake Case: Each word is separated by an underscore character: my_variable_name


#UNPACK A COLLECTION
#If we have a collection of values in a list, tuple etc.
#Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#GLOBAL VARIABLES
#Variables that are created outside of a function are known as global variables.
#To create a global variable inside a function, you can use the global keyword.