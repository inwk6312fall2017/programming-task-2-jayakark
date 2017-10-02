import csv
with open('Crime.csv') as myfile:

reader=csv.reader(myfile)
for row in reader:
 print(row)
