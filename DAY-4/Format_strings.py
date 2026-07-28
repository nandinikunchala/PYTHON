#1.Take a name and age as input and print them using an f-string.
name="Nandini"
age="20"
txt=f"I'm {name} and I'm {age}yrs old."
print(txt)

#2.Take a product name and price and display a formatted sentence.
product = "Laptop"
price = "50000"
print(f"{product} costs ₹{price}.")

#3.Print the multiplication table of a number using f-strings.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#4.Print marks of three subjects using formatted strings.
maths = 90
python = 95
english = 85

print(f"Maths: {maths}")
print(f"Python: {python}")
print(f"English: {english}")

#5.Display employee details (name, ID, salary) using string formatting.
name = "Nandini"
employee_id = 101
salary = 50000

print(f"Employee Name: {name}, ID: {employee_id}, Salary: ₹{salary}")
