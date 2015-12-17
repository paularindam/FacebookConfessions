from collections import Counter
from string import ascii_uppercase as letters
import os
import csv

def gen(L):
    c = Counter(L)
    for elt, count in c.items():
        if count == 1:
            yield elt
        else:
            for letter in letters[:count]:
                yield elt + letter

lst = os.listdir("FCBPosts")

lines = open("FCBCollegeList.txt").readlines()
if len(lines) == 1:
	lines = lines[0].split("\r")
dictionary = {}
lines = lines[1:]
for line in lines:
	line = line.split("\t")
	if "Rutgers" in line[3]:
		dictionary.setdefault(line[3].replace('"',''),[]).append(line[0])
	else:
		dictionary.setdefault(line[3],[]).append(line[0])
csvwriter = csvreader = None

count = 0
'''
with open("FCBPosts/Auburn University:149244371900507posts.csv", 'rb') as f,open("allPosts.csv", 'wb') as outf:
	csvreader = csv.DictReader(f,delimiter='|')
	fieldnames = ['school_id'] + csvreader.fieldnames  # add column name to beginning
	csvwriter = csv.DictWriter(outf, fieldnames, delimiter="|")
	csvwriter.writeheader()

	for fileName in lst:
		if "DS_Store" not in fileName:
			ID  = str(dictionary[fileName.split(":")[0]]).replace("[","").replace("]","")
			if "," in ID and count == 0:
				count = 1
				ID = ID.split(",")[0]
			elif "," in ID and count == 1:
				count = 0
				ID = ID.split(",")[1]
			ID  = ID.replace("'","")
			ID = str(ID)
			with open("FCBPosts/"+fileName, 'rb') as inf:
				csvreader = csv.DictReader(inf,delimiter='|')
				for row in csvreader:
	        			csvwriter.writerow(dict(row,school_id=ID))		
'''
with open("FCBComments/Auburn University:149244371900507comments.csv", 'rb') as f,open("allComments.csv", 'wb') as outf:
	csvreader = csv.DictReader(f,delimiter='|')
	fieldnames = ['school_id'] + csvreader.fieldnames  # add column name to beginning
	csvwriter = csv.DictWriter(outf, fieldnames, delimiter="|")
	csvwriter.writeheader()

	for fileName in lst:
		if "DS_Store" not in fileName:
			ID  = str(dictionary[fileName.split(":")[0]]).replace("[","").replace("]","")
			ID  = ID.replace("'","")
			if "," in ID and count == 0:
				count = 1
				ID = ID.split(",")[0]
			elif "," in ID and count == 1:
				count = 0
				ID = ID.split(",")[1]
			fileName = fileName.replace("posts","comments")
			with open("FCBComments/"+fileName, 'rb') as inf:
				csvreader = csv.DictReader(inf,delimiter='|')
				for row in csvreader:
	        			csvwriter.writerow(dict(row,school_id=ID))		

'''
lst = os.listdir("FCBPosts")
fileList = []
for fileName in lst:
	fileList += [fileName.split(":")[0]]
fileList = list(gen(fileList))
print fileList
lst = os.listdir("FCBComments")
fileList = []
for fileName in lst:
        fileList += [fileName.split(":")[0]]
fileList = list(gen(fileList))
print fileList
'''
