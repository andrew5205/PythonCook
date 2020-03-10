
# class is like a blueprint that ensures the consistent creation of instances.

# Attributes: 
# Class attributes belong to the class itself they will be shared by all the instances. 
# Such attributes are defined in the class body parts usually at the top, for legibility.
# declare a variable 
# var x = 10
# x is instance attribute 

# Attributes are a fundamental part of objects in Python.



# Methods:

class Foo(object):
    def __init__(self, x, y):       # define instance variables x, y
        self.x = x
        self.y = y

f = Foo(100, 'abc')         # f is an instance of Foo

print(type(f))      #<class '__main__.Foo'>

print(f.x)      # 100
print(f.y)      # abc


# Every object in Python has attributes.
# dir() - return a list of valid attributes for that object.
s = 'abc'
print(len(dir(s)))      # 71
print(dir(s)[:5])       # ['__add__', '__class__', '__contains__', '__delattr__', '__doc__']

i = 123
print(len(dir(i)))      # 64
print(dir(i)[:6])       # ['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__']

# getattr() - Return the value of the named attribute of object.
t = (1,2,3)
len(dir(t))             # 64
print(dir(t)[:5])       # ['__add__', '__class__', '__contains__', '__delattr__', '__doc__']
print(getattr(t, '__class__'))  # <type 'tuple'>
print(getattr(t, '__add__'))  # <method-wrapper '__add__' of tuple object at 0x1058ef870>



class User:             # declare a class and give it name User
    def __init__(self):     # attributes: __name__ , __email__ , __account_balance__ 
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

guido = User()      # guido is an instance of User class
monty = User()      # monty is an instance of User class

print(guido.name)	# output: Michael
print(monty.name)	# output: Michael


# set value to instance attributes  
guido.name = "Guido"
monty.name = "Monty"

print(guido.name)	# output: Guido
print(monty.name)	# output: Monty


# *********************************************************************************************** #
class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter


# pass arguements
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python



# Methods - function belong to a class 
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received


# __init__() takes exactly 3 arguments (1 given)
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

# *********************************************************************************************** #


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line

class User:
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
        print(self.account.balance)		# or access its attributes



# __init__() takes exactly 3 arguments (1 given)
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")




