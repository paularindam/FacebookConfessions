from __future__ import division
from orderedDict import *
import os
import string
import sys
import csv
import re


#number of LIWC words to consider is arg 1

def extractLIWCdict():
	with open('Excel_Data/LIWCdict.csv', 'rU') as f:
    		reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    		lst = [[x.strip() for x in row] for row in reader]

	lst = zip(*lst)
	return lst

def Dict(index):
	lst = extractLIWCdict()
    	return list(dict.fromkeys(filter(None, lst[index-1][3:])))


LIWC = ordered_dict()
'''
LIWC["sex"] = Dict(78) #before ingest
LIWC["religious"] = Dict(100) + Dict(101)
LIWC["death"] = Dict(102)
LIWC["sad"] = Dict(50)
LIWC["anger"] = Dict(48) + Dict(49)

LIWC["swear"] = Dict(27)
LIWC["social"] = Dict(28)+Dict(29)+ Dict(30)
LIWC["family"] = Dict(31)
LIWC["friends"] = Dict(32)
LIWC["humans"] = Dict(33)
LIWC["anxiety"] = Dict(47)
LIWC["body"] = Dict(74)+ Dict(75)
LIWC["health"] = Dict(76) + Dict(77)
LIWC["ingest"] = Dict(79)
LIWC["time"] = Dict(88)+ Dict(89)
LIWC["work"] = Dict(90) + Dict(91) + Dict(92)
LIWC["achievment"] = Dict(93) + Dict(94)
LIWC["leisure"] = Dict(95) + Dict(96)
LIWC["home"] = Dict(97)
LIWC["money"] = Dict(98) + Dict(99)
'''

LIWC["Funct"] = Dict(1) + Dict(2) + Dict(3)
LIWC["Pronoun"] = Dict(4)
LIWC["Ppron"] = Dict(5)
LIWC["I"] = Dict(6)
LIWC["We"] = Dict(7)
LIWC["You"] = Dict(8)
LIWC["SheHe"] = Dict(9)
LIWC["They"] = Dict(10)
LIWC["Ipron"] = Dict(11)
LIWC["Article"] = Dict(12)
LIWC["Verbs"] = Dict(13) + Dict(14) + Dict(15)
LIWC["AuxVb"] = Dict(16)

LIWC["Past"] = Dict(17)
LIWC["Present"] = Dict(18)+ Dict(19)
LIWC["Future"] = Dict(20)
LIWC["Adverbs"] = Dict(21)
LIWC["Prep"] = Dict(22)
LIWC["Conj"] = Dict(23)
LIWC["Negate"] = Dict(24)
LIWC["Quant"] = Dict(25)
LIWC["Numbers"] = Dict(26)
LIWC["Swear"] = Dict(27)
LIWC["Social"] = Dict(28) + Dict(29) + Dict(30)

LIWC["Family"] = Dict(31)
LIWC["Friends"] = Dict(32)
LIWC["Humans"] = Dict(33)
LIWC["Affect"] = Dict(34) + Dict(35) + Dict(36) + Dict(37) + Dict(38) + Dict(39)
LIWC["Posemo"] = Dict(40) + Dict(41) + Dict(42)
LIWC["Negemo"] = Dict(43) + Dict(44) + Dict(45) + Dict(46)
LIWC["Anx"] = Dict(47)
LIWC["Anger"] = Dict(48) + Dict(49)
LIWC["Sad"] = Dict(50)
LIWC["CogMech"] = Dict(51) + Dict(52) + Dict(53) + Dict(54) + Dict(55)
LIWC["Insight"] = Dict(56) + Dict(57)

LIWC["Cause"] = Dict(58)
LIWC["Discrep"] = Dict(59)
LIWC["Tentat"] = Dict(60)
LIWC["Certain"] = Dict(61)
LIWC["Inhib"] = Dict(62)
LIWC["Incl"] = Dict(63)
LIWC["Excl"] = Dict(64)
LIWC["Percept"] = Dict(65) + Dict(66)
LIWC["See"] = Dict(67)
LIWC["Hear"] = Dict(68)
LIWC["Feel"] = Dict(69)
LIWC["Bio"] = Dict(70) + Dict(71) + Dict(72) + Dict(73)
LIWC["Body"] = Dict(74) + Dict(75)

LIWC["Health"] = Dict(76) + Dict(77)
LIWC["Sexual"] = Dict(78)
LIWC["Ingest"] = Dict(79)
LIWC["Relativ"] = Dict(80) + Dict(81) + Dict(82) + Dict(83) + Dict(84)
LIWC["Motion"] = Dict(85)
LIWC["Space"] = Dict(86) + Dict(87)
LIWC["Time"] = Dict(88) + Dict(89)
LIWC["Work"] = Dict(90) + Dict(91) + Dict(92)
LIWC["Achiev"] = Dict(93) + Dict(94)
LIWC["Leisure"] = Dict(95) + Dict(96)
LIWC["Home"] = Dict(97)
LIWC["Money"] = Dict(98) + Dict(99)
LIWC["Relig"] = Dict(100) + Dict(101)
LIWC["Death"] = Dict(102)
LIWC["Assent"] = Dict(103)
LIWC["Nonflu"] = Dict(104)
LIWC["Filler"] = Dict(105)






def LIWCPosts(school, category, path = "USA/"):

	posts = []
	catPosts = {}
	dictionary = {}
	wordSet = []
	taggedPost = []

	totalPosts = school.split(":")[2]
	school = path+school.rsplit(":",1)[0] + "posts.csv"
	data = open(school).readlines()
	data = data[1:]
	wordSet = LIWC[category]
	taggedWords = []
	dictionary[category] = wordSet
	totalLength = 0
	allPst = []
	for post in data:
		post = post.split("|")
		pst = str(post[2])
		allPst += [pst]
		length = len(pst)
		totalLength += length
		count = 0
		words = " ("

		if len(sys.argv) <2:
			numWords = 1
		else:
			numWords = int(sys.argv[1])
		for word in wordSet:
			if word.endswith("*"):
				word = word[:-1]
			occur = re.search(word, pst)
			
			if occur is not None and (occur.start() ==0 or pst[occur.start()-1] == " ") and (occur.end() == len(pst) or pst[occur.end()] == " "):
				count += 1
				if count == numWords:
					words += word + ")"
					#pst += words
					taggedWords += [words]
					taggedPost += [pst]
					continue
				else:
					words += word + ","
	
	rest = list(set(allPst) - set(taggedPost))
	catDict = {"sex":"Sexual","death":"Death"}
	catPosts[category] = taggedPost
	catPosts["words"] = taggedWords
	#print "Total posts is ",int(totalPosts)
	totalPosts = int(totalPosts)
	avg = totalLength/totalPosts
	#print "Average length of post is ",avg," characters"
	poslabeledPosts = []
	labeledPosts = []
	#print count
        #print labeledPosts
	#print catPosts[category]
	#print "Number of labeled posts in this category",len(poslabeledPosts)
	#print "Number of LIWC-ed posts in this category",len(catPosts[category])
	#print catPosts["words"]
	#return totalPosts, avg, len(taggedPost)
	return totalPosts, avg, len(catPosts[category])

def processLIWC(text, category, numWords=1):
	pst = text
	wordSet = LIWC[category]
	#length = len(pst)
	#totalLength += length
	count = 0
	words = " ("

	for word in wordSet:
		if word.endswith("*"):
			word = word[:-1]
			#print word
		occur = re.search(word, pst)
		
		if occur is not None and (occur.start() ==0 or pst[occur.start()-1] == " ") and (occur.end() == len(pst) or pst[occur.end()] == " "):
			count += 1
			if count == numWords:
				words += word + ")"
				return True

			else:
				words += word + ","
	return False

def processLIWCNum(text, category):
	wordSet = LIWC[category]
	#length = len(pst)
	#totalLength += length
	Count = 0
	words = " ("
	for word in wordSet:
		if word.endswith("*"):
			word = word[:-1]
			Count += len(re.findall(word, text))
			#print word
		else:
			Count += re.split(r'\W', text).count(word)

	return str(Count)

def LIWCComments(school, category, path = "USA/"):


	#cogmech, posemo, negemo ?
	
	posts = []
	catPosts = {}
	dictionary = {}
	wordSet = []
	taggedPost = []

	totalPosts = school.split(":")[2]
	school = path+school.rsplit(":",1)[0] + "comments.csv"
	data = open(school).readlines()
	data = data[1:]
	wordSet = LIWC[category]
	taggedWords = []
	dictionary[category] = wordSet
	totalLength = 0
	allPst = []
	for post in data:
		post = post.split("|")
		pst = str(post[2])
		allPst += [pst]
		length = len(pst)
		totalLength += length
		count = 0
		words = " ("

		if len(sys.argv) <2:
			numWords = 1
		else:
			numWords = int(sys.argv[1])
		for word in wordSet:
			if word.endswith("*"):
				word = word[:-1]
			occur = re.search(word, pst)
			
			if occur is not None and (occur.start() ==0 or pst[occur.start()-1] == " ") and (occur.end() == len(pst) or pst[occur.end()] == " "):
				count += 1
				if count == numWords:
					words += word + ")"
					#pst += words
					taggedWords += [words]
					taggedPost += [pst]
					continue
				else:
					words += word + ","
	
	rest = list(set(allPst) - set(taggedPost))
	catDict = {"sex":"Sexual","death":"Death"}
	catPosts[category] = taggedPost
	catPosts["words"] = taggedWords
	#print "Total posts is ",int(totalPosts)
	totalPosts = int(totalPosts)
	avg = totalLength/totalPosts
	#print "Average length of post is ",avg," characters"
	poslabeledPosts = []
	labeledPosts = []
	#print count
        #print labeledPosts
	#print catPosts[category]
	#print "Number of labeled posts in this category",len(poslabeledPosts)
	#print "Number of LIWC-ed posts in this category",len(catPosts[category])
	#print catPosts["words"]
	#return totalPosts, avg, len(taggedPost)
	return totalPosts, avg, len(catPosts[category])




def main():
	categories = ["sex","religious","death","sad","anger", "swear", "social", "family", "friends", "humans", "anxiety", "body", "health", "ingest", "time", "work", "achievment", "leisure", "home", "money"]
	fileList = open("lenPosts.dat").readlines()
	path = "LIWCPosts/"
	for school in fileList:
		schoolPrefix = school.rsplit(":",1)[0] 
		
		for category in categories:
			totalPosts, avg, numLIWCPosts = LIWCPosts(school, category)
			percent = (int(str(numLIWCPosts))/int(str(totalPosts).strip())) * 100
			#print(category+","+str(totalPosts).strip()+","+str(avg)+","+str(numLIWCPosts)+"\n")	
			print(category+","+str(percent) + "%")
	
		print
		print schoolPrefix+"completely processed!!!!!!!!!!!!!!!!!!"
		print
		print
			
if __name__=='__main__':
	main()
