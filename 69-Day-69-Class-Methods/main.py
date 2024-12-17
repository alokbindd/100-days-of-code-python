class Employee:
    company = "APPLE"
    def show(self):
        print(f"The Name is {self.name} and Company is {self.company}")

    @classmethod
    def changecompany(cls,newcompany):
        cls.company = newcompany

e1=Employee()
e1.name="Alok"
print(Employee.company)
e1.show()
e1.changecompany("TESLA")
e1.show()
print(Employee.company)