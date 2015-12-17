import csv
f2 = open("newComm1.csv","w")

aList=[]
'''
with open('comm1.csv', 'r') as f:
    reader = csv.reader(f, skipinitialspace=False,delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
    	aList.append(row)
'''

with open('comm1.csv', 'rU') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    aList = [[x.strip() for x in row] for row in reader]

for line in aList:
	f2.write((str(line).replace("[","").replace("]",""))+"\n")



