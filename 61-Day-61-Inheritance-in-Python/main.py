class employee:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def showdetails(self):
        print(f"The details of {self.id} is {self.name} and age is {self.age}")

class programmer(employee):
    def showlang(self):
        print("The default languag is python")


e1 = employee(1,"Alok Bind",21)
e1.showdetails()
e2 = programmer(2,"Ravi Bind",18)
e2.showdetails()
e2.showlang()
e3 = employee(3,"Amit Bind",24)
e3.showdetails()

