class Animal:
    def __init__(self,name,species, color):
        self.name = name
        self.species = species
        self.color = color

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog",color="black")
        self.breed = breed
    
    def make_sound(self):
        print("Bark!")

class cat(Animal):
    def __init__(self, name, age):
        Animal.__init__(self,name,color="white",species="cat")
        self.age = age
    
    def info(self):
        print(f"i have {self.name} which is {self.color} and {self.age} year old")

d  = Dog("Dog","street")
d.make_sound()  # Outputs: Bark!

c = cat("cat",5)
c.info()

a = Animal("dog","kuuta","red")
a.make_sound()

