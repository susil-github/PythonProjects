class Employee:
    count=0
    def __init__(self):
        Employee.count = Employee.count+1

emp1=Employee()
emp2=Employee()
emp3=Employee()
print("the count value is ",Employee.count)