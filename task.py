import csv
with open('Crime.csv') as myfile:

 reader=csv.reader(myfile,delimiter=',')
 a=[]
 b=[] 
 for row in reader:
  a=strip(row)
  c=list(a)

  b.append(c[::1])
  print(b)
