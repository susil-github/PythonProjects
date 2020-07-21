# this is for Tuple
T=(10,20,30,40,50)
print(T)
count=0;
for i in T:
    print("Tuple",count,"[%d] = %d"%(count,i))
    count=count+1

Employees = [(101, "Ayush", 22), (102, "john", 29), (103, "james", 45), (104, "Ben", 34)]
print("----Printing list----");
for i in Employees:
    print(i)
Employees[0] = (110, "David",22)
print();
print("----Printing list after modification----");
for i in Employees:
    print(i)