
# def 
# if, elif, else 
# for, while
# class 



x = 10
if x > 50:
    print("bigger")
else:
    print("smaller")


##for loop 
## pass do nothing 
#for val in my_string:
#    pass 

#Tuples - A type of data that is immutable (can't be modified after its creation) 
# and can hold a group of values. Tuples can contain mixed data types.
tuples = ("Hello", "abc def", 23, False)
print(tuples)
print(tuples[1])
#tuples[0] = "a"     # TypeError: 'tuple' object does not support item assignment


# print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))    # # output: Hello 42

total = 35
user_val = "26"
# total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61
print(total)