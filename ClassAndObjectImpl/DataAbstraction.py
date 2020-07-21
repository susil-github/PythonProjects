class Employee:
    __count=0
    def __init__(self):
        Employee.__count=Employee.__count+1
    def display(self):
        print("count val is ",Employee.__count)

e1= Employee()
e2= Employee()

print(e1.display())
print(e2.display())
'''print(e2._count)'''
