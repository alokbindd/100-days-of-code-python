class person():
    Name = "Alok Bind"
    Occupation = "CSE Student"
    Networth = 0
    def info(self):
        print(f"{self.Name} is a {self.Occupation} and Networth is {self.Networth}")

a = person()
a.Name = "Manish Prajapati"
a.Occupation = "Software Devop"
a.Networth = 1000000

b = person()
b.Name = "Amol jadhav"
b.Occupation = "sales"
b.Networth = 92223

c = person()

# print(a.Name,a.Occupation)
a.info()
b.info()
c.info()