class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name} \nAge: {self.age}")
 
class Person(Human):
    def __init__(self,name,age,address):
        super().__init__(name,age)
        self.address = address

    def info(self):
        super().info()
        print(f"Address: {self.address}")

class Program:
    def __init__(self,program_name, duration):
        self.program_name = program_name
        self.duration = duration
    
    def info(self):
        print(f"Program Name: {self.program_name} \nDuration: {self.duration}")
        
class Student(Person):
    def __init__(self,name,age,address,program):
        super().__init__(name,age,address)
        self.program = program

    def info(self):
        super().info()
        self.program.info()

program = Program("Python Programming", "6 months")
student = Student("Alok", 22, "New Mumbai", program)
student.info()