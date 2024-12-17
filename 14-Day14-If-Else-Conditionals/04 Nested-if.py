num = int(input("Enter Valid Number: "))
if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1 - 10")
    elif(num >10 and  num <=20):
        print("Number is between 11 - 20")
    else:
        print("Number is More than 20")
else:
    print("Zero is not a postive number")

print("Well Done") 