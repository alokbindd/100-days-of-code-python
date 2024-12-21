class Animal:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def info(self):
		return f"Name: {self.name}\nAge:{self.age}"

class Mammal(Animal):
	def __init__(self,name,age,isWarm=True):
		super().__init__(name,age)
		self.isWarm = isWarm
	
	def info(self):
		return super().info() + f" It is a Warm blooded animal:{self.isWarm}"

class Bird(Animal):
	def __init__(self,name,age,canFly=True):
		super().__init__(name,age)
		self.canFly = canFly
	
	def info(self):
		return super().info() + f" It can fly:{self.canFly}"

class Reptile(Animal):
	def __init__(self,name,age,hasScales=True):
		super().__init__(name,age)
		self.hasScales = hasScales
	
	def info(self):
		return super().info() + f" It is has scale:{self.hasScales}"

class Dog(Mammal):
	def __init__(self,name,age,isWarm=True, breed="Unknown"):
		super().__init__(name,age,isWarm)
		self.breed = breed

	def info(self):
		return super().info() + f" It is a {self.breed} breed"

class Parrot(Bird):
	def __init__(self,name,age,canFly=True,color="Unknown"):
		super().__init__(name,age,canFly)
		self.color = color

	def info(self):
		return super().info() + f" It is  {self.color} in color"

class Snake(Reptile):
	def __init__(self,name,age,hasScale=True,length=0.0):
		super().__init__(name,age,hasScale)
		self.length = length

	def info(self):
		return super().info() + f" It is {self.length} meter long"

d = Dog("buggu",5,True,"Street")
print(d.info())

p = Parrot("Polly",2,True,"Green")
print(p.info())

s = Snake("Python",1,True,2.5)
print(s.info())
