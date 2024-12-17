x = 10 #global variable
print(f"The Global variable X is {x}")

def hello():
    global x
    x = 20 #local Variable 
    y = 30
    print(f"The local variable X is {x}")
    print(f"The Local variable Y is {y}")

hello()
print(f"The Global variable X is {x}")
# print(y)