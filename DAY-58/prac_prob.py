#1.Write a python program to print company anme,product name,and service name on separate lines
print("Company name:DELL")
print("Product name:Laptop")
print("Service name:Repair")
#2.Write a python program that prints a formatted message using print() with multiple arguments.
print("Hello","I'm Nandini")
#3.Write a python program to print the following output exactly:Product:AI Resume Builder|Status:Active.
print("Product:AI Resume Builder|Status:Active.")
#4.Write a Python program that takes a user's name and prints a personalized welcome message.
a=input("Enter a name:")
print("Hi",a,"Welcome!")
# 5.Write a Python program to read a product name, price, and quantity from the user and display them.
a=input("Enter product name:")
b=input("Enter product price:")
c=input("Enter quantity:")
print(a,b,c)
# 6.Write a Python program that calculates the total price of a product using price and quantity entered by the user.
a=input("Enter product name:")
b=int(input("Enter product price:"))
c=int(input("Enter quantity:"))
total=b*c
print(total)
# 7.Write a Python program to swap two variables without using a third variable.
a=1
b=2
a,b=b,a
print(a,b)
# 8.Write a Python program to create variables for customer_name, product_name, quantity, and price, then display an invoice line.
q="Nandini"
w="Laptop"
e=1
r=50000
print(q,"purchased a",w,"of quantity",e,"price of",r)
# 9.Write a Python program that checks the type of each of these values: 100, 99.99, 'Python', True.
print(type(100))
print(type(99.99))
print(type('Python'))
print(type(True))
# 10.Write a Python program that stores a service name and service fee in variables and prints them in a readable format.
k="Ac repair"
l=10000
print("Service name is",k,"and service price is",l)
#Numbers, Casting & Operators
# 11.Write a Python program to calculate the final bill amount after applying a percentage discount to a product price.
# Write a Python program to calculate GST for a service fee and display the final amount.
# Write a Python program to calculate the monthly subscription cost for a service from a yearly subscription price.
# Write a Python program that calculates the average rating from five customer ratings.
# Write a Python program to calculate profit or loss from cost price and selling price.
# Write a Python program to calculate the percentage increase in a product's price.
# Write a Python program to convert an integer product ID stored as a string into an integer and add 100 to it.
# Write a Python program that accepts a string price such as '1499.50', converts it to a float, and calculates a 10% discount.
# Write a Python program to convert total minutes of customer support usage into hours and remaining minutes.
# Write a Python program to calculate the area and perimeter of a rectangular product package.
# Write a Python program to calculate compound growth of monthly users for one year using a given growth rate.
# Write a Python program that uses arithmetic operators to calculate subtotal, discount, tax, and final bill.
# Write a Python program to check whether a product price is greater than a given budget using comparison operators.
# Write a Python program to check whether a customer is eligible for a service based on age and a minimum score.
# Write a Python program to determine whether a user qualifies for a premium plan using multiple conditions with and/or.
# Strings
# Write a Python program to take a product name and print its first character, last character, and length.
product_name=input("Enter a product name:")
print(product_name[0])
print(product_name[-1])
print(len(product_name))
# Write a Python program to extract the first five characters of a service description using string slicing.
l=input("Enter service description:")
print(l[0:5])
# Write a Python program to print the last three characters of an order ID using negative indexing.
j=input("Enter order ID:")
print(j[-3:])
# Write a Python program to reverse a product name using string slicing.
k=input("Enter a product name")
print(k[::-1])
# Write a Python program to check whether a customer email contains '@'.
h=input("Enter email:")
if "@" in h:
    print("Contains @")
else:
    print("Does not contain")
# Write a Python program to convert a product name to uppercase and lowercase.
f="MCAFFEIN"
print(f.lower())
t="mcaffein"
print(t.upper())
# Write a Python program to remove leading and trailing spaces from a customer-entered product name.
w=input("Enter product name:")
print(w.strip())
# Write a Python program to replace the word 'Basic' with 'Premium' in a service plan name.
y="We have Basic plan"
print(y.replace("Basic","Premium"))
# Write a Python program to count how many times the letter 'a' appears in a product description.
u=input("Enter product description:")
count=0
for x in u:
    if x=='a':
        count+=1
print(count)
# Write a Python program to find the position of the word 'AI' in a service description.
l=input("Enter service description:")
print(l.find('AI'))
# Write a Python program to split a comma-separated list of product names into separate values.
n="Hi,Hello,Hola"
for x in n.split(","):
    print(x)
# Write a Python program to join three service names into one string separated by ' | '.
a="Phone Repair"
b="Laptop Repair"
c="TV Repair"
print("|".join([a,b,c]))
# Write a Python program to check whether a product code starts with 'PRO'.
s=input("Enter product name:")
if s[:3]=="PRO":
    print("starts with PRO")
else:
    print("Doesn't start")
# Write a Python program to check whether a service code ends with '2026'.
d=input("Enter service code:")
if d[-4:]=="2026":
    print("Service code ends with 2026")
else:
    print("Doesn't end with 2026")
# Write a Python program to capitalize the first letter of each word in a customer name.
f=input("Enter name:")
print(f.title())
# Write a Python program to format a customer invoice using an f-string with customer name, product, quantity, and total.
customer_name=input("Enter name:")
product=input("Enter product:")
price=int(input("Enter price:"))
quantity=int(input("Enter quantity:"))
total=price*quantity
print(f"{customer_name} purchased {product} of quantity {quantity} and total is {total}.")
# Write a Python program to generate a product summary using the format() method.

# Write a Python program to display a price with exactly two decimal places using string formatting.
# Write a Python program to mask a customer phone number so that only the last four digits are visible.
# Write a Python program to extract the domain name from an email address such as 'user@company.com'.
# Write a Python program to check whether a given string is a palindrome using slicing.
# Write a Python program to count the number of words in a service description.
# Write a Python program to remove all spaces from a product code.
# Write a Python program to create a URL-friendly product slug from a product name.
# Write a Python program to compare two product names after converting them to lowercase and removing extra spaces.
# Booleans & Product/Service Logic
# Write a Python program that returns True if a product is in stock and False otherwise.
product=input("Enter product:")
stock=["Laptop","Tv","Phone","Watch"]
if product in stock:
    print("True")
else:
    print("False")
# Write a Python program to check whether a customer can access a premium service based on subscription status.
customer_service=input("Enter service:")
subscription_status={"Premium":799,"Basic":599}
if customer_service in subscription_status:
    if customer_service=="Premium":
        print("True")
    else:
        print("False")
else:
    print("False")
# Write a Python program to check whether a coupon is valid when the coupon code matches and the order value meets the minimum amount.
coupon_code=input("Enter coupon code:")
total_amount=int(input("Enter total amount:"))
coupon="NANDY21"
min_amount=400
if coupon_code==coupon and total_amount>=min_amount:
    print("True")
else:
    print("False")
# Write a Python program to determine whether free delivery should be applied using boolean conditions.
amount=int(input("Enter amount:"))
if amount>=500:
    print("True")
else:
    print("False")
# Write a Python program to check whether a user qualifies for a product warranty based on purchase amount and warranty status.

# Write a Python program to determine whether a service request can be accepted when the customer is active and payment is completed.
# Write a Python program that checks whether a product is eligible for a return using purchase days and return policy status.
# Write a Python program to determine whether a customer gets a premium discount if they are a member or their purchase exceeds a threshold.
# Write a Python program to check whether a product launch can proceed when development is complete, testing is passed, and approval is received.
# Write a Python program to create Boolean variables for payment_success, stock_available, and address_valid, then calculate whether an order can be placed.
# Write a Python program that checks whether a service booking is valid based on available slots and customer payment status.
# Write a Python program to determine whether a support ticket should be marked urgent using priority and customer plan.
# Write a Python program that accepts a product rating and returns whether the product qualifies as highly rated using comparison operators.
# Write a Python program to validate a service registration using username, email, and password conditions.
# Write a Python program that checks whether a user is eligible for a free trial based on account status and previous trial usage.
# Mixed Interview Coding
# Write a Python program to build a simple product bill calculator using only variables, numbers, strings, casting, and operators.
# Write a Python program to create a service quotation that accepts customer name, service name, hours, hourly rate, discount, and tax, then prints the final quotation.
# Write a Python program to parse an order string such as 'Laptop,2,55000' and calculate the order value.
# Write a Python program to validate a product code with a required prefix, length, and numeric suffix.
# Write a Python program to calculate the final subscription amount after converting a monthly price entered as text into a number and applying a discount.
# Write a Python program to generate a customer-facing message containing customer name, product name, quantity, total amount, and payment status.
# Write a Python program to compare two service plans by price and display which one is cheaper.
# Write a Python program to calculate a salesperson's commission from product sales using percentage operators.
# Write a Python program to split a full customer name into first name and last name and create a username from them.
# Write a Python program to create a short product identifier from the first three letters of a product name and the last four digits of its product code.
# Write a Python program to calculate a service SLA deadline in hours and display the result as hours and minutes.
# Write a Python program to validate an order before payment using stock, budget, customer status, and payment amount conditions.
# Write a Python program to generate a formatted receipt for three products using variables and string formatting.
# Write a Python program to normalize customer input by stripping spaces, converting to lowercase, and checking whether it matches a stored product category.
# Write a Python program to calculate the total annual revenue from a service using monthly customers, monthly fee, and number of months.

