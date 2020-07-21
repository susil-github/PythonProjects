import pandas as p

name=['susil','sumit','sunil','anil','rajesh']
age=[22,34,33,45,22]
scr=[800,222,333,444,555]
dict={"name":name,"age":age,"score":scr}
dataset=p.DataFrame(dict)
dataset.to_csv("D://newmodifiedcsv.csv")
print("wrote successfully...")
dataset.to_csv("modifeddata.csv")