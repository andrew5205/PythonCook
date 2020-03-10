msg = "hello world"
print(msg)


name = "Anthony"
print("My name is", name)
print("My name is " + name)


# F-Strings (Literal String Interpolation)
first_name = "Anthony"
last_name = "Davis"
age = 27
print("My name is {} {} ,and I am {} years old" .format(first_name, last_name, age))

# %-formatting
print("My name is %s %s, and I am %d years old" %(first_name, last_name, age))



# string method in py
# String.upper()
x = "Have a nice day!!!"
print(x.upper())

# String.lower()
y = "TODAY IS THE DAY"
print(y.lower())

# string.count(substring)       # returns number of occurrences of substring in string.
print(y.count("O"))

# string.split(char)        # returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
print(y.split())            # ['TODAY', 'IS', 'THE', 'DAY']
print(y.split("T"))         # ['', 'ODAY IS ', 'HE DAY']

# string.find(substring)        # returns the index of the start of the first occurrence of substring within string.
print(y.find("a"))          # -1 nothing found 
print(y.find("T"))          # 0 
print(y.find("A"))          # 3

# string.isalnum()          # returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method.
z = " Test for 123"
z1 = "Test 1@#$"
z2 = "123455"
print(z.isalnum())
print(z2.isalnum())
# .isalpha()
print(z.isupper())
# .isdigit()
print(z2.isdigit())
# .islower()
print(z.islower())
# .isupper()
print(y.isupper())







