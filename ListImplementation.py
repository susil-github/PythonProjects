# this is for list implementation
emp = ["susil",32,"USA"]
Dep1 = ["CS",10]
Dep2 = ["IT",20]
print(emp)
print(Dep1)
print(Dep2)
print("teh employee values are : ")
print("Name : %s, Age: %d ,Country: %s"%(emp[0],emp[1],emp[2]))
print("the Department values are : ")
print("Dept name : %s , Dept Id : %d"%(Dep1[0],Dep1[1]))
print("Dept name : %s , Dept Id : %d"%(Dep2[0],Dep2[1]))
List = [1,2,3,4,5]
print(List)
print(List[0:3])
List[0]=9
List[1:3]=[98,90]
print(List)
del List[0]
print(List)
print(len(List))
l1=["susil","sujit","sunita","sangita"]
for i in l1:
    print(i,end=" ")
l1.append("sumit")
print()
print(l1)
'''newList = []
num = int(input("Enter the Number"))
for i in range(0,num):
    j=int(input("Enter the Number for List"))
    newList.append(j)
print()
print("printing the list items");
for i in newList:
    print(i)'''
list1=[1,2,34,5,6]
print(list1)
list1.remove(34)
print(list1)
print(max(list1))
print(min(list1))
