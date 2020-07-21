class Student:
    def __init__(self, id, age, name):
        self.id =id
        self. age=age
        self. name=name
s= Student(1,23,"susil")

print("Student details ",getattr(s,'id'),getattr(s,'age'),getattr(s,'name'))
setattr(s,'id',2)
setattr(s,'age',33)
setattr(s,'name','sumit')
print("modified details...\n",getattr(s,'id'),getattr(s,'age'),getattr(s,'name'))