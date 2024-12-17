# There are four types of arguments that we can provide in a function:

# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments

# Default arguments:
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.4
def average(a=3,b=8):
    print("The average is:", (a+b)/2)

average(44)

def name(fname,mname="indrajeet",lname="bind"):
    print("hello", fname,mname,lname)

name("amit","vikram")

# Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.
def naam(fname,mname,lname):
    print("hello",fname,mname,lname)

naam(lname="bind",fname="sumit",mname="vikram")

# Required arguments:
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.
# Example 1: when number of arguments passed does not match to the actual function definition.
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")
# Example 2: when number of arguments passed matches to the actual function definition.
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego","hel")

# Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
# Arbitrary Arguments:
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum +i
    print("The Average of numbers is:", sum / len(numbers))
    
average(1,2,3,4,5,6,7,8,9,10,11)

# Arbitrary Arguments:

def name(**name):
    print(type(name))
    print("hello",name["first"],name["middle"],name["last"])

name(last ="bind", first= "sumit", middle="vikram")

# return Statement
# The return statement is used to return the value of the expression back to the calling function.
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum +i
    return sum / len(numbers)
    
c = average(55,4,5,4,55,45)
print(c)