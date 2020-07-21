import pandas
fileData = pandas.read_csv("D://hrdata.csv", engine='python')
print(fileData)
# we can use enigine or encoding='ISO-8859-1'