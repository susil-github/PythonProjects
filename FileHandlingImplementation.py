# file examples
fileobject=open("D:\\fileinfo.txt","r")
if fileobject:
    print("file is open")

'''fileonject1=open("D:\\fileinfo.txt","r")
readFile=fileonject1.read()
print(readFile)
fileonject1.close()
newFile=open("D:\\fileinfo.txt","r")
fileReadMode=newFile.readline()
print(fileReadMode)
print("now looping........")
for i in fileobject:
    print(i)'''
fileWrite=open("D:\\fileinfo.txt","a")
fileWrite.write("this is susil sahoo")
fileWrite.close()
filemodified=open("D:\\fileinfo.txt","r")
filemoD=filemodified.read()
print(filemoD)
