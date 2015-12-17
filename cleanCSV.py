import csv
import string
def remove_quotes(s):
    return ''.join(c for c in s if c not in ('"', "'"))

'''
with open('FCBCollegeList.csv', 'rU') as f, open("fixedCollegeList.csv","wb") as g:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    writer = csv.writer(g, quoting=csv.QUOTE_ALL)
    for line in reader:
            writer.writerow([remove_quotes(elem) for elem in line])


with open('fixedCollegeList.csv', 'rU') as f:
	reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
	aList = [[x.strip() for x in row] for row in reader]
'''
lines = open('FCBCollegeList.txt').readlines()
f2 = open('FCBCollegeList.txt',"w")
for line in lines:
	ele = line.split("\t")
	line = ""
	for i in range(len(ele)): 
	
		if "\xff" in ele[i]:
			ele[i] = ele[i].replace("\xff","")
		line += ele[i] +"\t"
	#line = line.replace("\xEF\xBF\xBD","")
	line = filter(lambda x: x in string.printable, line)
	f2.write(line)
