class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name} \nSpecies: {self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,species="Dog")
        self.breed = breed

    def show_details(self):
        super().show_details()
        print(f"Breed:{self.breed}")

class GoldenRetriever(Dog):
    def __init__(self,name,color):
        super().__init__(name,breed="Golden Retriever")
        self.color = color
    
    def show_details(self):
        super().show_details()
        print(f"Color: {self.color}")

o = GoldenRetriever("Buggu","Brown")
o.show_details()