class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class programmer(Employee):
    def __init__(self,name, age, salary,lang):
        super().__init__(name, age, salary)
        self.lang = lang

a = Employee("alok",20,200000)
print(a.name,a.age,a.salary)
b = programmer("Amisha",16,10000,"python")
print(b.name,b.age,b.salary,b.lang)

class parentclass:
    def parentmethod(self):
        print("This is parent class method")

class childclass(parentclass):
    def parentmethod(self):
        print("This is parent method of child class")
        super().parentmethod()
    def childmethod(self):
        print("This is child class method")
        super().parentmethod()

childobject = childclass()
childobject.parentmethod()
childobject.childmethod()

    