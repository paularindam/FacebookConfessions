import os
import string
import sys
import csv
import re
import labelNU

#number of LIWC words to consider is arg 1

def myDictFilter(lst, index):
        return list(dict.fromkeys(filter(None, lst[index-1][3:])))
def LIWCPosts(path, school, category):
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
		for word in wordSet:
			if word.endswith("*"):
				word = word[:-1]
			occur = re.search(word, pst)
			
			if occur is not None and (occur.start() ==0 or pst[occur.start()-1] == " ") and (occur.end() == len(pst) or pst[occur.end()] == " "):
				count += 1
				if count == int(sys.argv[1]):
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
	avg = totalLength/int(totalPosts)
	#print "Average length of post is ",avg," characters"
	poslabeledPosts = []
	labeledPosts = []
	#print count
        #print labeledPosts
	#print catPosts[category]
	#print "Number of labeled posts in this category",len(poslabeledPosts)
	#print "Number of LIWC-ed posts in this category",len(catPosts[category])
	#print catPosts["words"]
	return totalPosts, avg, len(catPosts[category])
	
def main():
	categories = ["sex","religious","death","sad","anger"]
	fileList = open("lenPosts.dat").readlines()
	path = "LIWCPosts/"
	for school in fileList:
		schoolPrefix = school.rsplit(":",1)[0] 
		f = open(path+schoolPrefix+".csv",'w')
		f.write("category, totalPosts, averageLength, numLIWCPosts \n")
		for category in categories:
			totalPosts, avg, numLIWCPosts = LIWCPosts("USA/",school, category)
			f.write(category+","+str(totalPosts).strip()+","+str(avg)+","+str(numLIWCPosts)+"\n")	
			print schoolPrefix + ":"+category+"processed..............." 
		f.close()
		print
		print schoolPrefix+"completely processed!!!!!!!!!!!!!!!!!!"
		print
		print
			
if __name__=='__main__':
	main()
