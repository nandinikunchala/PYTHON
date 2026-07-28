#String
#Strings in python surrounded by either single quotation marks, or double quotation marks.
print("I'm Nandini")#Observe the use of single quote inside double quotes


#Assign string to a variable
name = "Nandini"
print(name)


#Multiple Strings
x='''Hi I'm Nandini
I love dance
I love to travel'''
print(x)

#Strings are arrays
a="Nandini"
print(a[3])#Prints the character at index 3 (remember indexing starts at 0)


#Since strings are arrays, we can loop through them
for x in "Nandini":
    print(x)


#String length
#To get the length of a string, use the len() function
a="Nandini"
print(len(a))#Prints the length of the string


#Check String
txt = "The best things in life are free!"
print("free" in txt)
#Use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


#Check if NOT
#To check if a certain phrase or character is NOT present in a string, use the keyword not in.
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
#Use it in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")


#Slicing Strings
#We can return a range of characters by using the slice syntax.
a = "Nandini"
print(a[2:5])#Prints the characters from index 2 to 5 (not included)

#Slice From the Start
print(a[:3])#Prints the characters from the beginning to index 3 (not included)

#Slice To the End
print(a[2:])#Prints the characters from index 2 to the end

#Negative Indexing
#Use negative indexes to start the slice from the end of the string
a = "Nandini"
print(a[-5:-2])#Prints the characters from index -5 to -2 (not included)

#Modify Strings
#Upper Case
#To convert a string to upper case, use the upper() method.
a = "nandini"
print(a.upper())

#Lower Case
#To convert a string to lower case, use the lower() method.
a = "NANDINI"
print(a.lower())

#Remove Whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
a = "   Nandini   "
print(a.strip())#Returns "Nandini"

#Replace String
#To replace a string, use the replace() method.
a = "I love Nandini"
print(a.replace("Nandini", "Dance"))#Replaces "Nandini"      


#Format Strings
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "I am {} years old."#gives error
#But we can combine strings and numbers by using the format() method!
age = 36
txt = "I am {} years old."
print(txt.format(age))#Prints "I am 36 years old."


#f-Strings
#Python also has a method called f-strings, which is an easier way to format strings.
age = 36
txt = f"I am {age} years old."
print(txt)


#Placeholder and Modifiers
#You can use placeholders when you want to concatenate a variable with a string.
price = 49
txt = f"The price is {price} dollars"
print(txt)

#A placeholder can include a modifier to format the result:
price = 49
txt = f"The price is {price:.2f} dollars"
print(txt)#Prints "The price is 49.00 dollars"

#A placeholder can contain Python code, like math operations
txt = f"The price is {2* 5} dollars"
print(txt)

#Escape Characters
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
# \'-Single Quote
# \"-Double Quote
# \\-Backslash
# \n-New Line
# \t-Tab
# \b-Backspace
# \f-Form Feed
# \ooo-Octal value
# \xhh-Hex value
# \r-Carriage Return

#String Methods
#Python has a set of built-in methods that you can use on strings.

# capitalize()-Converts the first character to upper case
# casefold()-Converts string into lower case
# center()-Returns a centered string
# count()-Returns the number of times a specified value occurs in a string
# encode()-Returns an encoded version of the string
# endswith()-Returns true if the string ends with the specified value
# expandtabs()-Sets the tab size of the string
# find()-Searches the string for a specified value and returns the position of where it was found
# format()-Formats specified values in a string
# format_map()-Formats specified values in a string
# index()-Searches the string for a specified value and returns the position of where it was found
# isalnum()-Returns True if all characters in the string are alphanumeric
# isalpha()-Returns True if all characters in the string are in the alphabet
# isascii()-Returns True if all characters in the string are ascii characters
# isdecimal()-Returns True if all characters in the string are decimals
# isdigit()-Returns True if all characters in the string are digits
# isidentifier()-Returns True if the string is an identifier
# islower()-Returns True if all characters in the string are lower case
# isnumeric()-Returns True if all characters in the string are numeric
# isprintable()-Returns True if all characters in the string are printable
# isspace()-Returns True if all characters in the string are whitespaces
# istitle()-Returns True if the string follows the rules of a title
# isupper()-Returns True if all characters in the string are upper case
# join()-Joins the elements of an iterable to the end of the string
# ljust()-Returns a left justified version of the string
# lower()-Converts a string into lower case
# lstrip()-Returns a left trim version of the string
# maketrans()-Returns a translation table to be used in translations
# partition()-Returns a tuple where the string is parted into three parts
# replace()-Returns a string where a specified value is replaced with a specified value
# rfind()-Searches the string for a specified value and returns the last position of where it was found
# rindex()-Searches the string for a specified value and returns the last position of where it was found
# rjust()-Returns a right justified version of the string
# rpartition()-Returns a tuple where the string is parted into three parts
# rsplit()-Splits the string at the specified separator, and returns a list
# rstrip()-Returns a right trim version of the string
# split()-Splits the string at the specified separator, and returns a list
# splitlines()-Splits the string at line breaks and returns a list
# startswith()-Returns true if the string starts with the specified value
# strip()-Returns a trimmed version of the string
# swapcase()-Swaps cases, lower case becomes upper case and vice versa
# title()-Converts the first character of each word to upper case
# translate()-Returns a translated string
# upper()-Converts a string into upper case
# zfill()-Fills the string with a specified number of 0 values at the beginning
