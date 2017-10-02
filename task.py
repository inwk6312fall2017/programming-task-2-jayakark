import csv
with open('Crime.csv') as myfile:

 reader=csv.reader(myfile)
 a=[]
 b=[] 
 for row in reader:
  a=list(row)
  a.append(a)

  b.append(a[::1])
  print(b)
