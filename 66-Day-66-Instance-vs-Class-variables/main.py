class employee:
    companyName = "Apple"
    Nofemployee = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.002
        employee.Nofemployee += 1
    def showdetails(self):
        print(f"The employee name is {self.name} and raised amount in {self.companyName} of sized {self.Nofemployee} is {self.raise_amount}")

emp1= employee("alok")
emp1.raise_amount = 0.003
emp1.companyName = "Google"
emp1.showdetails()

emp2= employee("Manish")
emp2.showdetails()
# employee.showdetails(emp1)

emp3= employee("Dhiraj")
emp3.showdetails()

emp4= employee("Aman")
emp4.showdetails()