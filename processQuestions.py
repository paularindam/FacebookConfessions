from collections import Counter
from extractPercent import *
from processUnis import *
from mapUnis import *
from getProcessQuestions import *
import sys

questionDict = {"K":"Factual Knowledge", "R":"Rhetorical", "C":"Social Connection/Invitation", "P":"Opinion/Recommendation", "O":"Offer","N":"None"}
stigmaDict = {"E":"External", "C":"Character", "G": "Group","N":"None"}
tabooDict = {"S":"Sex","D":"Death", "E":"Excretions","U":"Drugs", "A":"Race/Protected Groups","M":
	"Mental Health", "G":"Academics","C":"Medical","W":"Money/Financial", "N":"None"}

def reconcile(File, cols, num):
	'''
	if "Fourth" not in File and cols == 23:
		if not cols[num-1]:
			return "N"
		else:
			return cols[num-1]
	if "Third" in File:
		if num>11:
			num = num - 1
		elif num == 11:
			if not cols[num-1]:
				return "N"
			else:
				return cols[num-1]
	'''

	if "-" in cols[num]:
		return "N"
	elif not cols[num]:
		if not cols[num-1]:
			return "N"
		elif cols[num-1] == cols[num-2]:
			return cols[num-1]
		else:
			return "N"
	else:
		return cols[num]

def processReconciled():
	List1 = ["Annotated/First100.csv", "Annotated/Second100.csv", "Annotated/Third100.csv"]
	List2 = ["Annotated/Fourth100.csv","Annotated/Fifth100.csv"] 
	posts = []
	questionType = []
	stigma = []
	taboo = []
	allPosts = open("FCBQuestionsOnly.csv").readlines()

	count = 700

	for File in List1:
		lines = open(File).readlines()
		lines = lines[1:101]
		for line in lines:
			cols = line.split('|')
			post = {}

			orgCols = allPosts[count].split("|")
			count += 1
			uni = orgCols[3]

			if "Rhodes" in uni or "Southwestern" in uni or  "University of California--Davis" in uni or uni == '':
				continue
			#like, comment = processPostLikesComments(orgCols[2],uni) 
			#if like <0 or comment<0:
				#continue
			post["PostID"] = orgCols[2]
			post["uni"] = orgCols[3]
			post["numLikes"], post["numComments"] = orgCols[4],orgCols[5]	
			post["message"] = cols[0]
			post["taboo"] = tabooDict[reconcile(File,cols,3)]
			post["stigma"] = stigmaDict[reconcile(File,cols,6)]
			post["isQuestion"] = reconcile(File,cols,11)
			post["questionType"] = questionDict[reconcile(File,cols,14)]
			post["loneliness"] = reconcile(File,cols,17)
			post["stress"] = reconcile(File,cols,20)
			post["victim"] = reconcile(File,cols,23)

			posts += [post]

	count = 3000

	for File in List2:
		lines = open(File).readlines()
		lines = lines[1:101]
		for line in lines:
			cols = line.split('|')
			post = {}

			orgCols = allPosts[count].split("|")
			count += 1
			uni = orgCols[3]

			if "Rhodes" in uni or "Southwestern" in uni or  "University of California--Davis" in uni:
				continue
			#like, comment = processPostLikesComments(orgCols[2],uni) 
			#if like <0 or comment<0:
			#	continue
			post["PostID"] = orgCols[2]
			post["uni"] = orgCols[3]
			if not orgCols[4]:
				orgCols[4] = "0"
			if not orgCols[5]:
				orgCols[5] = "0"
			post["numLikes"], post["numComments"] = orgCols[4],orgCols[5]	
			


			post["message"] = cols[0]
			post["taboo"] = tabooDict[reconcile(File,cols,3)]
			post["stigma"] = stigmaDict[reconcile(File,cols,6)]
			post["isQuestion"] = reconcile(File,cols,11)
			post["questionType"] = questionDict[reconcile(File,cols,14)]
			post["loneliness"] = reconcile(File,cols,17)
			post["stress"] = reconcile(File,cols,20)
			post["victim"] = reconcile(File,cols,23)
			posts += [post]

	return posts
			#print post["message"]+","+post["victim"]
			#break
		#break
def processIndividual():
	

	List = ["Annotated/Sei1000.csv", "Annotated/Sarah1000.csv"]#,"Annotated/SarahLast.csv"]
	allPosts = open("FCBQuestionsOnly.csv").readlines()
	count = 1000
	posts = []
	totalCount = 0
	for File in List:
		lines = open(File).readlines()
		lines = lines[1:]
		for line in lines:
			post = {}
			orgCols = allPosts[count].split("|")
			count += 1
			uni = orgCols[3]

			if "Rhodes" in uni or "Southwestern" in uni or  "University of California--Davis" in uni or uni == '':
				continue
			
			#like, comment = processPostLikesComments(orgCols[2],uni) 
			#if like <0 or comment<0:
			#	continue
			post["PostID"] = orgCols[2]
			post["uni"] = orgCols[3]
			if not orgCols[4]:
				orgCols[4] = "0"
			if not orgCols[5]:
				orgCols[5] = "0"
			post["numLikes"], post["numComments"] = orgCols[4],orgCols[5]	


			cols = line.split('|')

			post["message"] = cols[0]
			if not cols[1] or cols[1] == ' ':
				cols[1] = "N"
			post["taboo"] = tabooDict[cols[1].strip().upper()]
			if not cols[2] or cols[2] == ' ':
				cols[2] = "N"
			post["stigma"] = stigmaDict[cols[2].strip().upper()]
			if not cols[4]:
				cols[4] = "N"
			if "Y" not in cols[4]:
				cols[4] = "N"
			post["isQuestion"] = cols[4]
			if not cols[5] or cols[5] == ' ':
				cols[5] = "N"
			post["questionType"] = questionDict[cols[5].strip().upper()]
			if not cols[6] or cols[6] == ' ':
				cols[6] = "N"
			post["loneliness"] = cols[6]
			if not cols[7] or cols[7] == ' ' or "Y" not in cols[7]:
				cols[7] = "N"
			post["stress"] = cols[7]
			if not cols[8] or cols[8] == ' ' or "Y" not in cols[8]:
				cols[8] = "N"
			post["victim"] = cols[8]

			posts += [post]
				
	return posts

def processIndividualLast():
	#f.write("posts\n")
	main = getProcessQuestions()
	lines = open("Annotated/SarahLast.csv").readlines()[1:]
	count = 0
	posts = []
	idsmessages = []

	for line in lines:
		post = {}
		orgCols = main[count]
		count += 1
		#message,uni,postid = orgCols[7],orgCols[3],orgCols[2]
		uni = orgCols[3]

		if "Rhodes" in uni or "Southwestern" in uni or  "University of California--Davis" in uni or uni == '':
			continue

		post["PostID"] = orgCols[2]
		post["uni"] = orgCols[3]
		if not orgCols[4]:
				orgCols[4] = "0"
		if not orgCols[5]:
				orgCols[5] = "0"
		post["numLikes"], post["numComments"] = orgCols[4],orgCols[5]	
		#print orgCols[7]

		cols = line.split('|')
		post["message"] = cols[0]
		#print post["message"]
		#print
		if not cols[1] or cols[1] == ' ':
			cols[1] = "N"
		post["taboo"] = tabooDict[cols[1].strip().upper()]
		if not cols[2] or cols[2] == ' ':
			cols[2] = "N"
		post["stigma"] = stigmaDict[cols[2].strip().upper()]
		if not cols[4]:
			cols[4] = "N"
		if "Y" not in cols[4]:
			cols[4] = "N"
		post["isQuestion"] = cols[4]
		if not cols[5] or cols[5] == ' ':
			cols[5] = "N"
		post["questionType"] = questionDict[cols[5].strip().upper()]
		if not cols[6] or cols[6] == ' ':
			cols[6] = "N"
		post["loneliness"] = cols[6]
		if not cols[7] or cols[7] == ' ' or "Y" not in cols[7]:
			cols[7] = "N"
		post["stress"] = cols[7]
		if not cols[8] or cols[8] == ' ' or "Y" not in cols[8]:
			cols[8] = "N"
		post["victim"] = cols[8]

		posts += [post]

	return posts
		
	

def processQuestions():
	posts1,posts2,posts3 = [],[],[]
	posts1 += processReconciled()
	posts2 += processIndividual()
	posts3 += processIndividualLast()
	posts = posts1 + posts2 + posts3
	return posts

def printStats():
	posts = processQuestions()
	count = 0
	f = open("StatsForPosts.csv","w")
	f.write("PostID | uni | Size | Religious | State | Politics | Tuition | Post | numLikes | numComments | wordCount | ")
	f.write("isCoded | Taboo | Stigma | isQuestion | questionType | Loneliness | Stress | Victim\n")
	for post in posts:
		count += 1
		post["message"] = str(post["message"].replace('"',''))
		uniInfo = mapUniDict(post["uni"])
		f.write(post["PostID"]+"|"+post["uni"]+"|"+uniInfo["size"]+"|"+uniInfo["isReligious"]+"|"+ uniInfo["state"]+"|"+ uniInfo["politics"]+"|"+ uniInfo["tuition"]+ "|"+ post["message"]+"|"+post["numLikes"]+"|"+post["numComments"]+"|"+str(len(post["message"].split()))+"|")
		f.write("Y"+"|"+post["taboo"]+"|"+post["stigma"]+"|"+post["isQuestion"]+"|"+post["questionType"]+"|"+post["loneliness"]+"|"+post["stress"]+"|"+post["victim"]+"\n")


def printRestStats():
	allPosts = open("StatsForPosts.csv").readlines()
	f = open("StatsForPosts.csv","a")
	#f.write("PostID | uni | Size | Religious | State | Politics | Tuition | Post | numLikes | numComments | isCoded |  Taboo | Stigma | isQuestion | questionType | Loneliness | Stress | Victim\n")
	done = []
	
	for post in allPosts[1:]:
		done += [post.split("|")[0]]
	#print done
	posts = processPosts()
	postIDs = []
	for uni in posts.keys():
		for post in posts[uni]:
			uniInfo = mapUniDict(uni)
			if post["postID"] not in done:
				postIDs += [post["postID"]]
				if "527813577257803_630067583699068" in post["postID"] or "599429153419231_113350488871762" in post["postID"]:
					continue
				f.write(post["postID"]+"|"+uni+"|"+uniInfo["size"]+"|"+uniInfo["isReligious"]+"|"+ uniInfo["state"]+"|"+ uniInfo["politics"]+"|"+ uniInfo["tuition"]+ "|"+post["message"] + "|"+post["numLikes"]+"|"+post["numComments"]+"|"+str(len(post["message"].split()))+"|")
				f.write("N\n")

def printLIWCRest():
	allPosts = open("StatsForLIWCPosts.csv").readlines()
	f = open("StatsForLIWCPosts.csv","a")
	#f.write("PostID | uni | Size | Religious | State | Politics | Tuition | Post | numLikes | numComments | isCoded |  Taboo | Stigma | isQuestion | questionType | Loneliness | Stress | Victim\n")
	done = []
	
	for post in allPosts[1:]:
		done += [post.split("|")[0]]
	#print done
	posts = processPosts()
	postIDs = []
	for uni in posts.keys():
		for post in posts[uni]:
			uniInfo = mapUniDict(uni)
			if post["postID"] not in done:
				postIDs += [post["postID"]]
				if "527813577257803_630067583699068" in post["postID"] or "599429153419231_113350488871762" in post["postID"]:
					continue
				f.write(post["postID"]+"|"+uni+"|"+uniInfo["size"]+"|"+uniInfo["isReligious"]+"|"+ uniInfo["state"]+"|"+ uniInfo["politics"]+"|"+ uniInfo["tuition"]+ "|"+post["message"] + "|"+post["numLikes"]+"|"+post["numComments"]+"|"+str(len(post["message"].split()))+"|")
				for LIWCategory in LIWC.order():
					f.write(processLIWCNum(post["message"],LIWCategory)+ "|")

				f.write("N\n")

def printLIWCStats():
	posts = processQuestions()
	count = 0
	f = open("StatsForLIWCPosts.csv","w")
	f.write("PostID | uni | Size | Religious | State | Politics | Tuition | Post | numLikes | numComments | wordCount | ")
	for LIWCategory in LIWC.order():
		f.write(LIWCategory+"|")
	f.write("isCoded | Taboo | Stigma | isQuestion | questionType | Loneliness | Stress | Victim\n")
	for post in posts:
		count += 1
		post["message"] = str(post["message"].replace('"',''))
		uniInfo = mapUniDict(post["uni"])
		f.write(post["PostID"]+"|"+post["uni"]+"|"+uniInfo["size"]+"|"+uniInfo["isReligious"]+"|"+ uniInfo["state"]+"|"+ uniInfo["politics"]+"|"+ uniInfo["tuition"]+ "|"+ post["message"]+"|"+post["numLikes"]+"|"+post["numComments"]+"|"+str(len(post["message"].split()))+"|")
		for LIWCategory in LIWC.order():
			f.write(processLIWCNum(post["message"],LIWCategory)+ "|")

		f.write("Y"+"|"+post["taboo"]+"|"+post["stigma"]+"|"+post["isQuestion"]+"|"+post["questionType"]+"|"+post["loneliness"]+"|"+post["stress"]+"|"+post["victim"]+"\n")


		
printLIWCStats()
printLIWCRest()
#processAllQuestions()
'''
questions,numQuestions,questionType, taboo, stigma, truePos, trueNeg, falsePos, falseNeg, truePos2, trueNeg2, falsePos2, falseNeg2, truePosD, trueNegD, falsePosD, falseNegD, truePos2D, trueNeg2D, falsePos2D, falseNeg2D= processQuestions("combined")
numPosts = len(questions)
print "Number of legitimate questions : "+str(numQuestions)
print "Number of posts with question mark : "+str(numPosts)
print Counter(questionType)
print Counter(stigma)
print Counter(taboo)

print "Sex with 1 LIWC word truePos, trueNeg, falsePos, falseNeg",simplePercent(truePos, numPosts), simplePercent(trueNeg,numPosts), simplePercent(falsePos, numPosts), simplePercent(falseNeg, numPosts)
print "Sex with 2 LIWC word truePos, trueNeg, falsePos, falseNeg",simplePercent(truePos2, numPosts), simplePercent(trueNeg2,numPosts), simplePercent(falsePos2, numPosts), simplePercent(falseNeg2, numPosts)
print "Death with 1 LIWC word truePos, trueNeg, falsePos, falseNeg",simplePercent(truePosD, numPosts), simplePercent(trueNegD,numPosts), simplePercent(falsePosD, numPosts), simplePercent(falseNegD, numPosts)
print "Death with 2 LIWC word truePos, trueNeg, falsePos, falseNeg",simplePercent(truePos2D, numPosts), simplePercent(trueNeg2D,numPosts), simplePercent(falsePos2D, numPosts), simplePercent(falseNeg2D, numPosts)




for line in lines:
	cols = line.split('|')
	post["PostID"] = cols[2]
	post["school"] = cols[3]
	post["message"] = cols[7]
	post["sex"] = processLIWC(post["message"], "sex")
	post["religious"] = processLIWC(post["message"], "religious")
'''
