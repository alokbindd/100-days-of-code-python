class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary = salary

    @classmethod
    def from_string(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])


e1 = Employee("Alok",12000)
print(e1.name)
print(e1.salary)


string = "Ankit-12000"
e2 = Employee.from_string(string)
print(e2.name)
print(e2.salary)