# this is used for string manipulation
str = "hELLO";
str1 = "WORLD"
print(str);
print(str1)
print(str[:])
print(str[1:3])
print(str+str1)
print(str*2)
print('h' in str)
print('WO' in str1)
print(r'C://susil')
print("the value of String is : %s"%(str))

a=100;
b=200.89;
c="susil"
print("Am integer and value : %d\nHi am float and value : %f\nHi am String and value : %s"%(a,b,c))
s="susil kumar sahoo"
s1="JAVA- β"
s2=s1.casefold();
print(s.capitalize())
print(s2)
s3="Hello susil"
s4=s3.center(20,'@')
print("old value is : ",s3)
print("new value is :",s4)
s5="HËLLO"
s6=s5.encode('ascii',"ignore")
print(s6)
isEnds=s.endswith("sahoo")
print(isEnds)
s7="welcome \t to \t my \t world";
print(s7)
news7=s7.expandtabs()
print(news7)
news3=s3.find("s")
print(news3)
#python formatting
s8="java"
s9="python and c#"
print("{0} and {1} are two pragrmming language".format(s8,s9))
val=100000
print("decimal value is {:,}".format(val))
print(s8.isalnum())
strr="java is a programming language";
newSTR=strr.partition("is")
print(newSTR)
stVal=strr.rsplit();
print(stVal)
print(stVal[::-1])
list=stVal[::-1]
for l in list:
    print(l,end=" ")