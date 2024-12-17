class MyClass:
    def __init__(self,x):
        self._value = x
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, y):
        self._value = y/100
    
obj = MyClass(10)
print(obj.value)
obj.value = 20
print(obj.value)