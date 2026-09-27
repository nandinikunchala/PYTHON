#ENCAPSULATION
#Encapsulation is an OOP concept that means keeping data and the
#methods that work on that data together inside a class and controlling access to that data.

#Private Attributes
#In Python, we can use double underscore __ before an attribute to indicate that it should be treated as private.
class BankAccount: 
    def __init__(self, balance): 
        self.__balance = balance#self.__balance is private attribute
#It should normally be accessed through methods of the class rather than directly from outside.

#Data Hiding
# Encapsulation is commonly associated with data hiding.
# For example:
# self.__balance
# The double underscore tells Python to use name mangling, making direct access from outside more difficult.
# Normally, we should use methods such as:
# get_balance()
# deposit()
# instead of directly accessing the internal attribute.

#Getter and Setter
# Methods used to access or modify private data are commonly called:
# Getter:
# Used to read data.
def get_balance(self):
    return self.__balance
# Setter:
# Used to modify data.
def set_balance(self, balance):
    self.__balance = balance
# Example:
class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
# Here:
# __marks → private data
# get_marks() → getter
# set_marks() → setter
# The setter can also validate the data before changing it.

#Real-Life Example
# Think about a bank account.
# You should not directly change your bank balance.
# Instead, you use operations such as:
# Deposit
# Withdraw
# Check Balance
# The bank account controls how the balance is changed.
# Similarly, in Python:
# Private Data
#      ↓
# Methods
#      ↓
# Controlled Access