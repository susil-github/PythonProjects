import csv
fieldNames=["first_name","last_name","Rank"]

with open("D://writefile.csv","w") as csvfile:
        writeFile=csv.DictWriter(csvfile,fieldnames=fieldNames)
        writeFile.writeheader()
        writeFile.writerow({'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'})
        writeFile.writerow({'Rank': 'A', 'first_name': 'Smith',
                     'last_name': 'Rodriguez'})
        writeFile.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
        writeFile.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
        print("prints successfully....")
