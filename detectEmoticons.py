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

def list_emotions(KeyValue):
	smileyDict = {'(:': 'Happy face (mirror)', ':-(': 'Unhappy', ':o': '"Shock', ':(': 'Sad face', ':)': 'Happy face', '=D': 'Laugh', ':D': 'Laugh', ':P': 'Tongue out', ':/': '"Uneasy', '=/': '"Uneasy', 'XD': 'Big grin', ':]': 'Happy face', ':-)': 'Happy face (with nose)', 'D:': 'Grin (mirror)', ';D': 'Wink and grin', ';)': 'Wink', '=]': 'Happy face', '=)': 'Happy face', '=(': 'Unhappy', ';-)': 'Wink (with nose)'}
	if KeyValue == "keys":
		smileys = smileyDict.keys()
	else:
		smileys = smileyDict.values()
	pattern = "|".join(map(re.escape, smileys))
	return pattern

def detect_emoticon(text):
	return str(re.findall(pattern, text))
	

path = sys.argv[1]
fileList = os.listdir(path)
counter = 0
keyValue = sys.argv[2]
#pattern = list_emoticon()
pattern = list_emotions(keyValue)
for fileName in fileList:
	if ".csv" not in fileName:
		continue

	counter +=1
	data = open(path+"/"+fileName).readlines()
	#newCSV = open(path+"Emoticons/"+fileName.replace(".csv","Emoticon.csv"),'w')
	newCSV = open(path+"Emotions/"+fileName.replace(".csv",keyValue+"Emotions.csv"),'w')
	if len(data) < 1 :
		continue
	newCSV.write(data[0].strip()+"|emoticon"+"\n")
	for row in data[1:]:
		if "|" in row:
			if "post" in fileName:
				post = row.split("|")[2]
			elif "comment" in fileName:
				post = row.split("|")[6]
			else:
				break
			emoticon = detect_emoticon(post)
			newCSV.write(row.strip()+"|"+emoticon+"\n")
	newCSV.close()

	

