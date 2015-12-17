from __future__ import division
import scipy
from scipy import mean, std, stats
from scipy.stats import sem

lines = open("StatsForPosts.csv").readlines()[1:]

meanTabooDictLikes,stdTabooDictLikes,meanStigmaDictLikes,stdStigmaDictLikes = {},{},{},{}
meanTabooDictComments,stdTabooDictComments,meanStigmaDictComments,stdStigmaDictComments = {},{},{},{}
tabooDictLikes = {}
tabooDictComments = {}

stigmaDictLikes = {}
stigmaDictComments = {}

questionDictLikes = {}
questionDictComments = {}
wordTaboo, wordStigma, wordQuestion = {},{},{}
characterOverall, wordOverall,totalComments = [],[],[]
countTaboo = countStigma = countLoneliness = countStress = countVictim = 0

for line in lines:
	
#Postid 0, uni 1, size 2, reli 3, st 4, pol 5, tui 6, post 7, numLikes 8, numComments 9, wordCount 10, isCoded 11
#taboo 12, stigma 13, isQuestion 14, questionType 15, Loneliness 16, Stress 17, Victim 18
	'''
	 [1] "Uni"                                               
	 [2] "Population"                                        
	 [3] "Tuition.Cost"                                      
	 [4] "Religious"                                         
	 [5] "State" 
	'''
	cols = line.split("|")
	try:
		if not cols[8]:
			cols[8] = "0"
		if not cols[9]:
			cols[9] = "0"

		try:
			totalComments += [int(cols[9])]
		except:
			print lines.index(line)
			print cols[9]	

	except:
		print lines.index(line)
		print line
		print len(cols)
	
	if "Y" not in cols[11] or "Y" not in cols[14]:
		continue

	taboo = cols[12]
	stigma = cols[13]
	question = cols[15]
	loneliness = cols[16]
	stress = cols[17]
	victim = cols[18]
	
	 #numComments

	if "Y" in loneliness:
		countLoneliness += 1
	if "Y" in stress:
		countStress += 1
	if "Y" in victim:
		countVictim += 1

	numLikes = cols[8]
	numComments = cols[9]
	wordCount = cols[10]
	characterCount = len(cols[7])

	

	characterOverall += [characterCount]
	wordOverall += [int(wordCount)]
	#[1] "Academics"       "Death"           "Drugs"          
 	#[4] "Excretion"       "Medical"         "Mental Health"  
 	#[7] "Money/Financial" "None"            "Race"           
	#[10] "Sex"
	if stigma in wordStigma.keys():
		wordStigma[stigma] += [int(wordCount)]
	else:
		wordStigma[stigma] = [int(wordCount)]

	if taboo in wordTaboo.keys():
		wordTaboo[taboo] += [int(wordCount)]
	else:
		wordTaboo[taboo] = [int(wordCount)]

	if question in wordQuestion.keys():
		wordQuestion[question] += [int(wordCount)]
	else:
		wordQuestion[question] = [int(wordCount)]


	if question in questionDictLikes.keys():
		questionDictLikes[question] += [int(numLikes)]
	else:
		questionDictLikes[question] = [int(numLikes)]

	
	if question in questionDictComments.keys():
		questionDictComments[question] += [int(numComments)]
	else:
		questionDictComments[question] = [int(numComments)]


	if taboo in tabooDictLikes.keys():
		tabooDictLikes[taboo] += [int(numLikes)]
	else:
		tabooDictLikes[taboo] = [int(numLikes)]

	
	if taboo in tabooDictComments.keys():
		tabooDictComments[taboo] += [int(numComments)]
	else:
		tabooDictComments[taboo] = [int(numComments)]
	

	if stigma in stigmaDictLikes.keys():
		stigmaDictLikes[stigma] += [int(numLikes)]
	else:
		stigmaDictLikes[stigma] = [int(numLikes)]

	if stigma in stigmaDictComments.keys():
		stigmaDictComments[stigma] += [int(numComments)]
	else:
		stigmaDictComments[stigma] = [int(numComments)]
	
'''

for key in tabooDictLikes.keys():
	meanTabooDictLikes[key] = mean(tabooDictLikes[key])
	stdTabooDictLikes[key] = std(tabooDictLikes[key])
	meanTabooDictComments[key] = mean(tabooDictComments[key])
	stdTabooDictComments[key] = std(tabooDictComments[key])

for key in stigmaDictLikes.keys():
	meanStigmaDictLikes[key] = mean(stigmaDictLikes[key])
	stdStigmaDictLikes[key] = std(stigmaDictLikes[key])
	meanStigmaDictComments[key] = mean(stigmaDictComments[key])
	stdStigmaDictComments[key] = std(stigmaDictComments[key])
'''

tabooList = ['Race/Protected Groups', 'Death', 'Academics', 'Drugs', 'Medical', 'Mental Health', 'Money/Financial', 'Excretions', 'Sex']#,'None']
stigmaList = ["Group","Character","External"]#,"None"]
questionList = ['Social Connection/Invitation', 'Opinion/Recommendation', 'Offer', 'Factual Knowledge', 'Rhetorical']#,'None']

print "Avg. Comments", mean(totalComments)
print "Taboo"

print "x = c(",
for ele in tabooList:
	print mean(wordTaboo[ele]),",",
print ")"

print "se = c(",
for ele in tabooList:
	countTaboo += len(tabooDictLikes[ele])
	print sem(wordTaboo[ele]),",",
print ")"
print
print "Stigma"

print "x = c(",
for ele in stigmaList:
	print mean(wordStigma[ele]),",",
print ")"

print "se = c(",
for ele in stigmaList:
	countStigma += len(stigmaDictComments[ele])
	print sem(wordStigma[ele]),",",
print ")"
print

print "questionType"

print "x = c(",
for ele in questionList:
	print mean(wordQuestion[ele]),",",
print ")"

print "se =c(",
for ele in questionList:
	print sem(wordQuestion[ele]),",",
print ")"
print
print "Overall"
print "c(",
print countTaboo,",",
print countStigma,",",
print countLoneliness,",",
print countStress,",",
print countVictim,",",
print ")"
'''
print "wordCount Mean"
print "Overall",mean(wordOverall)

print "(",
for ele in stigmaList:
	print ele
	print mean(word[ele]),",",
print ")"
print "wordCount Std"
print "(",
for ele in stigmaList:
	print std(word[ele]),",",
print ")"

print
print
print "characterCount Mean"
print "Overall",mean(characterOverall)
print
print "(",
for ele in stigmaList:
	print mean(character[ele]),",",
print ")"
print "characterCount Std"
print "(",
for ele in stigmaList:
	print std(character[ele]),",",
print ")"


print "(",
for ele in stigmaDictList():
	print stigmaDictLikes[ele],",",
print ")"

print "***********Taboo**********"
print tabooDictLikes	
print tabooDictLikes.keys()
print tabooDictComments.keys()
print tabooDictLikes.values()
print tabooDictComments.values()

print "***********Stigma**********"
print stigmaDictLikes
print stigmaDictLikes.keys()
print stigmaDictComments.keys()
print stigmaDictLikes.values()
print stigmaDictComments.values()

print 
print "+++++++++++++++++++++++++++++++++++"
print "Comments Taboo"
print
print "***Mean***"
print "(",
for ele in tabooList:
	print meanTabooDictComments[ele],",",
print ")"
print "***Std***"
print "(",
for ele in tabooList:
	print stdTabooDictComments[ele],",",
print ")"

print
print "Comments Stigma"
print
print "***Mean***"
print "(",
for ele in stigmaList:
	print meanStigmaDictComments[ele],",",
print ")"
print "***Std***"
print "(",
for ele in stigmaList:
	print stdStigmaDictComments[ele],",",
print ")"

'''
