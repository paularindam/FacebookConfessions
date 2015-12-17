import sys
import os
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter

nltkStop = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')
path = "FCBPosts"
filesDone = os.listdir(path)
allFiles = os.listdir("/Users/arindam/FCB")
files = list(set(allFiles) - set(filesDone))
for fileName in files:
	print fileName
	if ".csv" not in fileName or fileName == "Georgetown University:409149419153181posts.csv":
		continue
	if "post" in fileName:
		colNum = 2
		newPath = "FCBPostWords/"
	elif "comment" in fileName:
		colNum = 6
		newPath = "FCBCommentWords/"

	print newPath
	newFileName = newPath+fileName.split(":")[0]+"uniqueWords.dat"
	f = open(newFileName,'w')

	data = open("/Users/arindam/FCB"+"/"+fileName).readlines()
	posts = []

	myStop = ["me","it's","&","and","i'm","i'd", "i've","didn't"]
	for i in range(10000):
		myStop += [str(i+1)]
		myStop += ['#'+str(i+1)+':']
	stop = nltkStop + myStop

	for row in data:
		posts += [row.split("|")[colNum]]

	uniqueWords = []
	for sentence in posts:
		#uniqueWords +=  [i for i in sentence.lower().split() if i not in stop]
		uniqueWords +=  [i for i in tokenizer.tokenize(sentence.lower()) if i not in stop]
		
	wordCounter = Counter(uniqueWords)
	for word in wordCounter.keys():
        	f.write(str(word)+":"+str(wordCounter[word])+"\n")
		
