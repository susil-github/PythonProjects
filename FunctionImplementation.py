# this is for function implementation in python
def heloWorld():
    return "Hello World";

print(heloWorld())

'''def add(a,b):
    return a+b;

num1=int(input("Enter the first Number"))
num2=int(input("Enter the second number"))
print("sum is : ",add(num1,num2))'''

def addToList(list):
    list.append(50);
    list.append(60);
    print("inside funstion the list is : ",list)
print()
list=[10,20,30,40,50]
addToList(list)
print("the new List values are : ",list)

def stringAdd(str):
    newStr=str+"susil sahoo"
    print("insiide function the string value is : ",newStr);
str="this is"
stringAdd(str);
print("outside string value is : ",str)

def helloMSG(msg):
    return msg;
print(helloMSG("Hello MSG"))

def printData(name,age):
    msgPrint="the age details of : "+name+" is ",age
    return msgPrint;
print(printData("susil",18))

def keywordFunction(name,age):
    print("printing name is ",name,"And age is",age)
keywordFunction(name="sujit",age=45)
def getData(name,age=22):
    print("the values are ",name,"And",age)
getData("susil")
def printNames(*names):
    print("the names are : ")
    for name in names:
        print(name);
printNames("susil","sujit","sumit","sunil")
i=-20
print(abs(i))
l1=[1,2,3,4]
print("the all value is",all(l1))
l2=[1,23,4,0]
print("the second all value is",all(l2))
b=10
c=11
print("the binary values are ",bin(b)," ",bin(c))
test=[]
print(test,"is",bool(test))
test=[0]
print(test,"is",bool(test))
string="helloWorld"
print(bytes(string,'utf-8'))


class Details:
    age = 22
    name = "Phill"


details = Details()
print('The age is:', getattr(details, "age"))
print('The age is:', details.age)

class Student:
    id = 101
    name = "Pranshu"
    email = "pranshu@abc.com"
# Declaring function
    def getinfo(self):
        print(self.id, self.name, self.email)
s = Student()
s.getinfo()

result = enumerate([1,2,3])
# Displaying result
print(result)
result=set("12")
result1=set("helloworld")
result4=set(["susil",1,20.3,"sujit"])
result3=set()
print(result)
print(result1)
print(result3)
print(result4)
class Student:
    id=0;
    name="";
student=Student();
print(getattr(student,'id'))
print(getattr(Student,'name'))
setattr(student,'id','102')
setattr(student,'name','susil')
setattr(student,'email','sbc@gmail.com')
print(student.id)
print(student.name)
print(student.email)
if isinstance("str",Student):
    print("this is an instance")
else:
    print("not an instance")
print(oct(0))
print(pow(4,2))
print(pow(-4,3))
print(pow(4,-2))
print(pow(-4,-2))