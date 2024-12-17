class Employee:
    def __init__(self,name):
        self.name = name
    
    def __len__(self):
        i = 0
        for c in self.name:
            i =i+1
        return i
    
    # def __str__(self):
        # return (f"The name of employee is {self.name}")
    
    def __repr__(self):
        return (f"The name of employee is {self.name}")
    
    def __call__(self):
        print ("Hello")

class shop:
    def __init__(self,sales,expenditure):
        self.sales = sales
        self.expenditure = expenditure
    def __call__(self):
        print(f"The Total Sales: {self.sales} and Expenditure: {self.expenditure}")
        print(f"the total Profit is {self.sales-self.expenditure}")