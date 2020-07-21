# this is for lambda function
num=lambda x:x+10
print("value is : ",num(10))
num1=lambda x,y:x*y
print("the value is : ",num1(10,8))
def multiplyTable(n):
    return lambda x:n*x
num=10
b=multiplyTable(num)
for i in range(1,11):
    print(i," * ",num,"=",b(i))
List=[1,2,3,10,123,88]
Oddlist = list(filter(lambda x:(x%3 == 0),List)) # the list contains all the items of the list for which the lambda function evaluates to true
print(Oddlist)

List1=[1,2,3,4,5]
newMap=list(map(lambda x:(x*3),List1))
print(newMap)