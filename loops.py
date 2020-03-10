
for x in range(0, 10, 1):
    print(x)

for y in range(5, 10):      # increment of +1 is implied
    print(y)

for z in range(10):         # increment of +1 and start at 0 is implied
    print(z)

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8

for x in range(5, 1, -3):
    print(x)
# output: 5, 2




my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])        # output: 0 abc, 1 123, 2 xyz

for k in my_list:
    print(k)        # output: abc, 123, xyz

# dict #output oreder is not guarantee
my_dict = { "a": "value1", "a2": "val2", "a1": "val3" }
for key in my_dict:
    print(key)        # output: a, a1, a2 



capitals = {"key1": "value1", "key2": "value2", "key3": "value3"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
#to iterate through the values
for val in capitals.values():
    print(val)
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)



# while loop 
for count in range(0,5):
    print("looping - ", count)

# rewrite
count = 0
while count < 5:
    print("looping - ", count)
    count += 1



# We define parameters. We pass in arguments
def say_hi(name):
    print("Hi, " + name)

say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

# We define parameters. We pass in arguments
# 'name' is a parameter while "Michael", "Anna", and "Eli", are arguments.



