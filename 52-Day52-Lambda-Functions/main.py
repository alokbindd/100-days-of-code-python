# lambda arguments: expression
def avg(x,y):
    return (x+y)/2

print(avg(55,53))

cube = lambda x:x*x*x
print(cube(2))

double = lambda x: x*2
print(double(5))  # Outputs: 10

def apply(fx,value):
    return 6 + fx(value)

print(apply(cube,3))
print(apply(lambda x: x * x,4))

mul = lambda x , y : print(f"the multiplicaion of {x} and {y} is {x*y}")
mul(3,4)