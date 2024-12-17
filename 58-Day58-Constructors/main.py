class person:
    def __init__(self,name,gender,age,occupation):
        print("Hey I am person")
        self.name = name
        self.gender = gender
        self.age = age
        self.occupation = occupation
    def info(self):
        z = 'his' if self.gender == 'Male' else 'her'
        print(f"{self.name} is {self.age} year old and {z} occupation is {self.occupation}")

a = person("Alok","Male",21,"CSE student")
b = person("Emily","Female",32,"actress")
a.info()
b.info()
    
