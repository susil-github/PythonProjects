import xlsxwriter

book=xlsxwriter.Workbook("D://Example1.xlsx")
sheet=book.add_worksheet()
row=0
col=0
content=['susil','sumit','sunil']
for item in content:
    sheet.write(row,col,item)
    row+=1
book.close()