from scipy import mean, std, stats 
from scipy.stats import sem

tabooList = ['Race/Protected Groups', 'Death', 'Academics', 'Drugs', 'Medical', 'Mental Health', 'Money/Financial', 'Excretions', 'Sex']
stigmaList = ["Group","Character","External"]
questionList = ['Social Connection/Invitation', 'Opinion/Recommendation', 'Offer', 'Factual Knowledge', 'Rhetorical']#,'None']

def complexStats():
	lines = open("StatsForPosts.csv").readlines()[1:]
	count = {}
	

	for stigma in stigmaList:
		count[stigma] = {}
		
		for questionType in questionList:
			count[stigma][questionType] = 0


	for line in lines:
		cols = line.split("|")

		isCoded = cols[11]

		if "Y" not in isCoded: 
			continue

		taboo = cols[12]
		stigma = cols[13]
		isGenuineQuestion = cols[14]
		questionType = cols[15]

		if "Y" not in isGenuineQuestion:
			continue

		if "None" in stigma or "None" in questionType:
			continue
		
		#count[taboo][stigma] += 1
		count[stigma][questionType] += 1

	x = []
	#for stigma in stigmaList:
	for questionType in questionList:
		for stigma in stigmaList:
			print stigma, questionType
			x += [count[stigma][questionType]]
	print "Taboo and Questions"
	print "x = c( [2, 0, 0, 2, 1, 2, 0, 0, 2, 118, 4, 26, 30, 16, 26, 23, 41, 130, 0, 0, 0, 0, 0, 0, 0, 0, 1, 10, 2, 1, 3, 3, 1, 0, 3, 6, 62, 8, 13, 26, 12, 9, 24, 41, 82]"
	print "Stigma and Questions"
	print "x = c(",x

def LIWCStats():
	lines = open("StatsForLIWCPosts.csv").readlines()[1:]
	tabooList = ['Race/Protected Groups', 'Death', 'Academics', 'Drugs', 'Medical', 'Mental Health', 'Money/Financial', 'Excretions', 'Sex']
	category  = {}
	for taboo in tabooList:
		category[taboo] = []

	for line in lines:
		cols = line.split("|")
		if "Y" not in cols[75]: #isCoded
			continue

		taboo = cols[76]
		stigma = cols[77]

		if "None" in taboo:
			continue
		category[taboo] += [int(cols[19])] #Ppron

	Mean, SEM = [],[]
	for taboo in tabooList:
		Mean += [mean(category[taboo])]
		SEM += [sem(category[taboo])]

	print "Ipron"
	print Mean
	print SEM

def CategoryStats():
	lines = open("StatsForPosts.csv").readlines()[1:]


#LIWCStats()
