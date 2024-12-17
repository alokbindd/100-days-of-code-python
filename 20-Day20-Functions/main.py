def area(a,b):
    res = a * b
    print(res)

def isbigger(a,b):
    if a>b:
        print("length is bigger than breadth")
    else:
        print("both are equal or breadth is bigger than length")

def islesser(e,f):
    if e<f:
        print("length is lesser than breadth")
    else:
        print("both are equal or breadth is greater than length")

def bolbhai():
    pass


c = int(input("Enter length of rectangle:"))
d = int(input("Enter breadth of rectangle:"))
area(c,d)
isbigger(c,d)
islesser(c,d)