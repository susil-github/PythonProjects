class Calculation1:
    def add(self,a,b):
        return a+b

class Calculation2:
    def mul(self,x,y):
        return x*y

class Calculation3(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b

c= Calculation3()
print(c.add(10,20))
print(c.mul(3,20))
print(c.divide(20,10))
print(issubclass(Calculation3,Calculation2))
print(issubclass(Calculation3,Calculation1))
print(issubclass(Calculation1,Calculation2))
print(isinstance(c,Calculation3))