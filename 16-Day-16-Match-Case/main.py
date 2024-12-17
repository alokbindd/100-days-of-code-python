#match case in python 3.10
x = int(input("Enter the value of x:"))
match x:
    case 0:
        print(x," is a zero")
    case _ if 10 < x <=20:
        print(x," is between 11 - 20") 
    case _ if 20 < x <=30:
        print(x,"is between 21 - 30")
    case _:
        print(x,"is out of range")
