import csv
header=['id','name','address','zip']
rows=[
    [1, 'Hannah', '4891 Blackwell Street, Anchorage, Alaska', 99503],
    [2, 'Walton', '4223 Half and Half Drive, Lemoore, California', 97401],
    [3, 'Sam', '3952 Little Street, Akron, Ohio', 93704],
    [4, 'Chris', '3192 Flinderation Road, Arlington Heights, Illinois', 62677],
    [5, 'Doug', '3236 Walkers Ridge Way, Burr Ridge', 61257],
]
with open('newfile.csv','wt') as writer:
    csv_writer=csv.writer(writer)
    csv_writer.writerow(header)
    for row in rows:
        csv_writer.writerow(row)
    print("writes successfully.....")
