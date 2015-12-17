import os
import string
import sys
import csv
import re
import labelNU

#schoolName is arg 1
#LIWC category is arg 2
#number of LIWC words to consider is arg 3

def myDictFilter(lst, index):
        return list(dict.fromkeys(filter(None, lst[index-1][3:])))
def main():
	schoolName = sys.argv[1]
	category = sys.argv[2]
	# count = sys.argv[3]

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
	wordSet = []
	taggedPost = []



	fileList = open("All/lenPosts.dat").readlines()
	for school in fileList:
		if schoolName in school:
			break
	totalPosts = school.split(":")[2]
	school = "All/"+school.rsplit(":",1)[0] + "posts.csv"
	data = open(school).readlines()
	data = data[1:]
	wordSet = LIWC[category]
	'''
	else:
	fileName = sys.argv[2] + ".dict"
	#for fileName in dictList
	wordList = open(fileName).read()
	#wordList = unicode(wordList, 'ascii', 'ignore')
	wordList = filter(lambda x: x in string.printable, wordList)
	wordList = wordList.split("|")
	for word in wordList:
		word = word.strip()
		if len(word) > 1:
			wordSet += [word]
	wordSet = list(set(wordSet))
	'''
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
		for word in wordSet:
			if word.endswith("*"):
				word = word[:-1]
			occur = re.search(word, pst)
			
			if occur is not None and (occur.start() ==0 or pst[occur.start()-1] == " ") and (occur.end() == len(pst) or pst[occur.end()] == " "):
				count += 1
				if count == int(sys.argv[3]):
					words += word + ")"
					#pst += words
					taggedWords += [words]
					taggedPost += [pst]
					continue
				else:
					words += word + ","
	
	rest = list(set(allPst) - set(taggedPost))
	catDict = {"sex":"Sexual","death":"Death"}
	totalLabeled = labelNU.label(catDict[category])
	catPosts[category] = taggedPost
	catPosts["words"] = taggedWords
	print "Total posts is ",int(totalPosts)
	avg = totalLength/int(totalPosts)
	print "Average length of post is ",avg," characters"
	poslabeledPosts = []
	labeledPosts = []
	count = 0
	for post in totalLabeled:
		if post[1] == "pos":
			poslabeledPosts += [post[0]]
			if post[0] in taggedPost:
				count +=1
	#print count
        #print labeledPosts
	#print catPosts[category]
	#print "Number of labeled posts in this category",len(poslabeledPosts)
	print "Number of LIWC-ed posts in this category",len(catPosts[category])
	#print catPosts["words"]
	

if __name__=='__main__':
	main()
