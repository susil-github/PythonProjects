NewFile=open("D:\\demofile.txt","x")
if NewFile:
    print("file created successfully");
NewFile.close();
writeIntoFile=open("D:\\demofile.txt","w")
writeIntoFile.write("this is a new file and present in d drive")
writeIntoFile.close()

readFileInfo=open("D:\\demofile.txt","r")
print(readFileInfo.read())
readFileInfo.close()

