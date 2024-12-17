# class employee:
#     def __init__(self):
#         self.__name = "ALOK"

# a = employee()
# # print(a.name) # Cannot be called be directly
# print(a._employee__name) # Can be called be indirectly
# print(a.__dir__())
class Student:
    def __init__(self):
        self._name = "ALOK"

    def _funName(self):      # protected method
        return "BIND"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName()) 