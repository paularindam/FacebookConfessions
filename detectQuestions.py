import os
import sys
import re

def list_emoticon():
	lines = open("Excel_Data/emoticons.csv").readlines()
	lines = lines[:]
	smileys = []
	for line in lines:
		smileys += [line.split(",")[1]]
	
	smileys += ['=3']
	pattern = "|".join(map(re.escape, smileys))
	return pattern

def detect_question(text):
	if "?" in text:
		return True
	else:
		return False
	

path = sys.argv[1]
fileList = os.listdir(path)
counter = 0
count = {}
for fileName in fileList:
	if ".csv" not in fileName:
		continue

	counter +=1
	data = open(path+"/"+fileName).readlines()
	if "posts" in fileName:
		prefix = fileName.split("posts.csv").pop()
	else:
		prefix = fileName.split("comments.csv").pop()
	count[prefix] = 0
	newCSV = open(path+"Questions/"+fileName.replace(".csv","Questions.dat"),'w')
	if len(data) < 1 :
		continue
	total = 0
	for row in data[1:]:
		if "|" in row:
			total += 1
			if "post" in fileName:
				post = row.split("|")[2]
			elif "comment" in fileName:
				post = row.split("|")[6]
			else:
				break

			if detect_question(post) == True:
				count[prefix] += 1
			
				newCSV.write(post)
			
	newCSV.close()

