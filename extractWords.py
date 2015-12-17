import os
import string
import sys
import csv
import re

def myDictFilter(lst, index):
        return list(dict.fromkeys(filter(None, lst[index-1][3:])))

with open('Excel_Data/LIWCdict.csv', 'rU') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    lst = [[x.strip() for x in row] for row in reader]

lst = zip(*lst)
LIWC = {}
LIWC["sex"] = myDictFilter(lst,78)
LIWC["religious"] = myDictFilter(lst,100) + myDictFilter(lst, 101)
LIWC["death"] = myDictFilter(lst, 102)
LIWC["sad"] = myDictFilter(lst, 50)
LIWC["anger"] = myDictFilter(lst, 48) + myDictFilter(lst, 49)


posts = []
catPosts = {}
dictionary = {}
category = sys.argv[2]
wordSet = []
taggedPost = []
'''
arg1: Labelled or not
arg2: category (sex/anger/death/...)
arg3: number of category words
arg4(optional): LIWC (or not)
'''
if sys.argv[1] == "Labeled" or sys.argv[1] == "Labelled":
	with open('Excel_Data/myNUData2.csv', 'rU') as f:
		reader = csv.reader(f, delimiter='|', lineterminator='\r\n', quotechar='"', quoting=csv.QUOTE_NONE)
		aList = [[x.strip() for x in row] for row in reader]
	labelledPosts = []
	for item in aList[1:]:
		labelledPosts += [[item[0]]+item[1:35:3]]
else:
	files = os.listdir("FCBPosts")
	for fileName in files:
		if sys.argv[1] in fileName:
			data = open("FCBPosts/Georgetown University:409149419153181posts.csv").readlines()
			data = data[1:]


if len(sys.argv) == 5 and sys.argv[4] == "LIWC":
	wordSet = LIWC[category]
else:
	fileName = sys.argv[2] + ".dict"
	wordList = open(fileName).read()
	wordList = filter(lambda x: x in string.printable, wordList)
	wordList = wordList.split("|")
	for word in wordList:
		word = word.strip()
		if len(word) > 1:
			wordSet += [word]
	wordSet = list(set(wordSet))

dictionary[category] = wordSet

for post in labelledPosts:
	print post
	count = 0
	words = " ("
	for word in wordSet:
		if word.endswith("*"):
			occur = re.search(word[:-1], post[0])
			if occur is not None and (occur.start() ==0 or post[0][occur.start()-1] == " "):
				count += 1
				if count == int(sys.argv[3]):
					words += word + ")"
					post[0] += words
					taggedPost += [post[0]]
					continue
				else:
					words += word + ","

		else:
			occur = re.search(word, post[0])

			if occur is not None and (occur.start() ==0 or post[0][occur.start()-1] == " ") and (occur.end() == len(post[0]) or post[0][occur.end()] == " "):
				count += 1
				if count == int(sys.argv[3]):
					words += word + ")"
					post[0] += words
					taggedPost += [post[0]]
					continue
				else:
					words += word + ","

catPosts[category] = taggedPost

print len(labelledPosts)
print len(taggedPost)
	

