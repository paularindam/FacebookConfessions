from __future__ import division
from processUnis import *
from myTime import *
from collections import Counter
from scipy import mean,std,stats
from scipy.stats import sem

def processedCommentStats():
	postIDs = []
	unis = []
	posts = processCommentList()
	lines = open("processedComments.csv").readlines()[1:]

	#orig_stdout = sys.stdout
	f = open("StatsForLIWCComments.csv","w")
	f.write("commentID|postID|uni|post|username| date|time|comment|wordCount|numLikes|isViable|isMean|isProsocial|Taboo|Stigma|")
	for LIWCategory in LIWC.order():
		f.write(LIWCategory+"|")
	f.write("isCoded\n")
	tabooDict = {'A':"Race",'C':"Medical",'D':"Death",'E':"Excretions",'G':"Academics",'M':"Mental Health",'P':"Ignore",'S':"Sex",'U':"Drugs",'W':"Money",'Y':"Ignore"}
	#sys.stdout = f

	i = count = 0
	while i<len(lines):
		line = lines[i]

		cols = line.split("|")
		uni = cols[0]
		postID = cols[1]
		
		
		
		post = posts[uni][postID]

		
		

		for col in post:
			cols = lines[i].split("|")
			date, time = splitTime(col['time'])
			if "Y" in cols[5] and "N" in cols[6]:
				prosocial = "Y"
			else:
				prosocial = "N"
			if not col['likeCount'] or col['likeCount'] == " ":
				col['likeCount'] = 0
			col['message'] = col['message'].strip()
			wordCount = len(col['message'].split())
			if wordCount >0:
				count += 1
				f.write(col['commentID']+"|"+postID+"|"+uni+"|"+cols[2]+"|"+col['userName']+"|"+date+"|"+time+"|"+col['message']+"|"+str(wordCount) +"|"+col['likeCount']+"|"+cols[5]+"|"+cols[6]+"|"+prosocial+"|"+cols[7].strip()+"|"+cols[8]+"|")
				for LIWCategory in LIWC.order():
					f.write(processLIWCNum(col["message"],LIWCategory)+ "|")
				f.write("Y\n")
			
			i += 1

		if len(post) ==0:
			i += 1
	
	comments = processComment()
	lines = open("processedCommentsID.csv").readlines()[1:]
	for line in lines:
		cols = line.split("|")
		uni = cols[0]
		postID = cols[1]
		commentID = cols[5]
		cols[7] = cols[7].upper() #isViable
		cols[8] = cols[8].upper() #isMean
		if "Y" in cols[7] and "N" in cols[8]:
			prosocial = "Y"
		else:
			prosocial = "N"

		comment = comments[uni][commentID]
		comment['message'] = comment['message'].strip()
		date, time =  splitTime(comment['time'])
		wordCount = len(comment['message'].split())
		if wordCount >0:
			f.write(commentID+"|"+postID+"|"+uni+"|"+cols[2]+"|"+comment['userName']+"|"+date+"|"+time+"|"+comment['message']+"|"+str(wordCount) +"|"+comment['likeCount']+"|"+cols[7]+"|"+cols[8]+"|"+prosocial+"|"+cols[9]+"|"+cols[10]+"|")
			for LIWCategory in LIWC.order():
				f.write(processLIWCNum(col["message"],LIWCategory)+ "|")

			f.write("Y\n")

		
	print count

def percent(x,y):
	return (x/y)*100

#wordCount 8, likes 9
#viable 10, mean 11, prosocial 12, taboo 13
#Pronoun 16, PPron 17, IPron 23, Posemo 42, Negemo 43
def checkCommentStats():
	note = []
	tabooList = ['Race/Protected Groups', 'Death', 'Academics', 'Drugs', 'Medical', 'Mental Health', 'Money/Financial', 'Excretions', 'Sex']#,'None']
	stigmaList = ["Group","Character","External"]
	stigmas = []
	taboos = []
	tabooDict = {"A":"Race/Protected Groups","C":"Medical","D":"Death","E":"Excretions","G":"Academics","M":"Mental Health","S":"Sex","U":"Drugs","W":"Money/Financial","Y":"None","P":"None","N":"None"}
	stigmaDict = {}
	numLikes,wordCount= {},{}


	for ele in tabooDict.values():
		numLikes[ele] = []
		wordCount[ele] = []
	
	y = n = count = PPronY = PPronN = IPronY = IPronN = PosemoY = NegemoY = PosemoN = NegemoN = 0
	lines = open("StatsForComments.csv").readlines()[1:]
	for line in lines:
		cols = line.split("|")
		
		if "Y" in cols[12]:

			PPronY += int(cols[17])
			IPronY += int(cols[23])
			PosemoY += int(cols[42])
			NegemoY += int(cols[43])

			y += 1
		elif "N" in cols[12]:
			PPronN += int(cols[17])
			IPronN += int(cols[23])
			PosemoN += int(cols[42])
			NegemoN += int(cols[43])

			n += 1
		
		
		if not cols[13]:
			cols[13] = "N" # or "P" in cols[13] or "Y" in cols[13]:
		if "N" in cols[13] or "P" in cols[13] or "Y" in cols[13]:
			continue
		taboo = tabooDict[cols[13]]
		numLikes[taboo] +=[int(cols[9])]
		wordCount[taboo] +=[int(cols[8])]

		taboos += [taboo]

	taboos = Counter(taboos)
	
	Frequency = "x = c("
	for ele in tabooList:
		Frequency += str(len(numLikes[ele])) +","

	Frequency += ")"

	print tabooList
	Mean = "x = c("
	SE = "sd = c("
	for ele in tabooList:
		Mean += str(mean(numLikes[ele])) +","
		SE += str(sem(numLikes[ele])) +","

	Mean += ")"
	SE += ")"
	print "Frequency"
	print Frequency
	print
	print
	print "Mean"
	print Mean
	print
	print
	print "Stan.Error"
	print SE

	print "x = c(",
	for ele in tabooList:
		print meanNumLikes[ele],",",
	print ")"
	print "sd = c(",
	for ele in tabooList:
		print stdNumLikes[ele],",",
	print ")"
	
	print "********isProsocial*********"
	print "PPron :",percent(PPronY,y), percent(PPronN,n)
	print "IPron :",percent(IPronY,y), percent(IPronN,n)
	print "Posemo :",percent(PosemoY,y), percent(PosemoN,n)
	print "Negemo :",percent(NegemoY,y), percent(NegemoN,n)
	
	#print len(note)
	#for col in note:
	#	print col[0],col[1]
	

processedCommentStats()
#checkCommentStats()