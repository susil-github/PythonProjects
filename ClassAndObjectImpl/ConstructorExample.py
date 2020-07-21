class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def display(self):
        print("ID: %d \nName: %s"%(self.id,self.name))

emp1=Employee(101,"susil")
emp2=Employee(102,"sumit")

emp1.display()
emp2.display()
