import csv

def myDictFilter(lst, index):
	return dict.fromkeys(filter(None, lst[index-1][3:]))

with open('Excel_Data/LIWCdict.csv', 'rU') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    aList = [[x.strip() for x in row] for row in reader]

lst = list(zip(*aList))

sexual = myDictFilter(lst,78)
religious = myDictFilter(lst,100) + myDictFilter(lst, 101)
death = myDictFilter(lst, 102)
sad = myDictFilter(lst, 50)
anger = myDictFilter(lst, 48) + myDictFilter(lst, 49)
'''
posts = []
lines = open("FCBPosts/University of Wisconsin--Madison:504557926250083posts.csv").readlines()
for line in lines[1:]:
	post = line.split("|")[2]
	word = 
#print posts
#posts = zip(*lines[1:])
#print posts
'''
print sexual
