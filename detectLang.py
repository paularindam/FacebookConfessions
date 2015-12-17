from langDetector import *
import os
import sys
import random
import detectlanguage


path = "/Users/arindam/"+sys.argv[1]
fileList = os.listdir(path)
counter = 0
size = len(os.listdir(path+"Lang2"))
keys = ["1d452a27a04588cd8cf091471ceb721b","027908c5d0c860c04333d296a7e9d451","df306ebd3731b79075c61e29b2d5dca9"]
key = "27bf174064658198e63c727ac4e61e36"
for fileName in fileList:
	if ".csv" not in fileName:
		continue
	counter +=1
	data = open(path+"/"+fileName).readlines()
	if len(sys.argv) >2  and sys.argv[2] == "api":
		detectlanguage.configuration.api_key = key
		newCSV = open(path+"Lang2/"+fileName.replace(".csv","apiLang.csv"),'w')
	else:
		newCSV = open(path+"Lang/"+fileName.replace(".csv","Lang.csv"),'w')
	if len(data) < 1 :
		continue
	newCSV.write(data[0].strip()+"|language"+"\n")
	for row in data[1:]:
		if "|" in row:
			if "post" in fileName:
				post = row.split("|")[2]
			elif "comment" in fileName:
				post = row.split("|")[6]
			else:
				break
			if len(sys.argv)>2:
				try:
					language = detectlanguage.simple_detect(str(post.strip()))
					language = str(language)
					if language == "en":
						newCSV.write(row.strip()+"|"+"english\n")
					#elif language == "es":
					#	newCSV.write(row.strip()+"|"+"spanish\n")
					else:
						newCSV.write(row.strip()+"|"+"other\n")
				except:
					print post
					newCSV.write(row.strip()+"|"+"unknown\n")
			else:
				language = detect_language(post)
				if "english" in language:
					newCSV.write(row.strip()+"|"+language+"\n")
				elif "spanish" in language:
					newCSV.write(row.strip()+"|"+language+"\n")
				else:
					newCSV.write(row.strip()+"|other\n")
	newCSV.close()

	

