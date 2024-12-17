# @staticmethod is used to 
# define a static method, which is a method that belongs to a class rather than an instance of
# the class. Static methods do not have access to the instance variables of the class.
class Math:

    def __init__ (self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n
    
    @staticmethod
    def add(a,b):
        return a + b


a = Math(5) 
print(a.num)
a.addtonum(10)
print(a.num)
print(Math.add(8,9))