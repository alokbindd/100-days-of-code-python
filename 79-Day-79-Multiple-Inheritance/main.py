class Employee:
    def __init__(self,name):
        self.name = name
    
    def show(self):
        print(f"the name is {self.name}")

class Dancer:
    def __init__(self,type):
        self.type = type

    def show(self):
        print(f"the dance style is {self.type}")

class DancerEmployee(Dancer,Employee):
    def __init__(self,name,type):
        self.name = name
        self.type = type

o = DancerEmployee("Alok","Hip hop")
print(o.name)
print(o.type)
o.show()
print(DancerEmployee.mro())