import csv
fileopen= open("D://csvfile.txt")
csv_fileReader=csv.reader(fileopen, delimiter=',')
count = 0
for row in csv_fileReader:
    if count == 0:
     print(f'Column names are {", ".join(row)}')
     count += 1
    else:
        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        count += 1




print(f'Processed {count} lines.')