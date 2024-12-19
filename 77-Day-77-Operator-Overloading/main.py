class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        # return f"{self.i+x.i}i+ {self.j+x.j}j + {self.k+x.k}k"
        return vector(self.i+x.i ,self.j+x.j , self.k+x.k)
    
    def __sub__(self,x):
        # return f"{self.i+x.i}i+ {self.j+x.j}j + {self.k+x.k}k"
        return vector(self.i-x.i ,self.j-x.j , self.k-x.k)
    
v1 = vector(3,2,5)
print(v1)
v2 = vector(5,6,8)
print(v2)

R = v1+v2
print(R)
R = v1-v2
print(R)
print(type(R))


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self,x):
        return point(self.x+x.x, self.y+x.y)
    
p1 = point(1, 2)
p2 = point(3, 4)
p3 = p1 + p2
print(p3.x,p3.y) # prints 4, 6
