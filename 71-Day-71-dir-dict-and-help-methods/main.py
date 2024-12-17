class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 1
    
a = person("alok",20)
print(dir(a))
print(a.__dict__)
# print(p.__class__)
# print(help(str))
print(help(person))

x = [1,2,3]
print(dir(x))
