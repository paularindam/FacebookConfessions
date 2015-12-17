from __future__ import division
from processUnis import *
from scipy import mean, std, stats 
from scipy.stats import sem
from processFacebook import *
import pickle

def selectCodedPosts():
	lines = open("StatsForPosts.csv").readlines()[1:]
	postIDs = []
	for line in lines:
		postIDs += [line.split("|")[0]]
	comments =  processCommentList()
	selectedComments = {}
	restComments = {}
	for uni in comments.keys():
		for postID in comments[uni].keys():
			if postID in postIDs:
				selectedComments[postID] = comments[uni][postID]
			else:
				restComments[postID]= comments[uni][postID]

	return selectedComments

def codedGenderStuff():
	lines = open("StatsForPostsGender.csv").readlines()
	emptyComments = {}

	posts = {}
	for line in lines[1:]:
		uni = line.split("|")[1]
		if uni in posts.keys():
			posts[uni] += 1
		else:
			posts[uni] = 1

		
	for uni in posts.keys():
		emptyComments[uni] = 0
	lines = lines[1:]
	for line in lines:
		col = line.split("|")
		uni = col[1]
		numComments = col[9]
		if not numComments or "0" in numComments:
			if "0|0|0|N" in line or "0|0|0|Y" in line:	
				emptyComments[uni] += 1

	for uni in posts.keys():
		print uni, (100 *(emptyComments[uni]/posts[uni]))
		print

def Mean(dct):
	if len(dct) == 0:
		return 0
	else:
		return mean(dct)

def Sem(dct):
	if len(dct) == 0:
		return 0
	else:
		return sem(dct)

def assignCommentSentiment():

	userGender = pickle.load(open('genderDict.pkl', 'rb'))
	lines = open("StatsForCodedComments.csv").readlines()
	totalDictM, totalDictF, meanDictM,viableDictM,meanDictF,viableDictF = {},{},{},{},{},{}
	
	for line in lines[1:]:

		col = line.split("|")
		postID = col[1]
		userID = col[4]
		isMean = col[12]
		isViable = col[11]
		gender = userGender[userID]
		
		if postID not in meanDictM.keys():
			totalDictM[postID], totalDictF[postID],meanDictM[postID], viableDictM[postID], meanDictF[postID], viableDictF[postID] = [],[],[],[],[],[]#0,0,0,0,0,0

		if "Y" in isMean and "Female" in gender:
			meanDictF[postID] += [userID]#1
		elif "Y" in isMean and "Male" in gender:
			meanDictM[postID] += [userID]#1

		if "Y" in isViable and "Female" in gender:
			viableDictF[postID] += [userID]#1
		elif "Y" in isViable and "Male" in gender:
			viableDictM[postID] += [userID]#1

		if "Male" in gender:
			totalDictM[postID] += [userID]#1
		elif "Female" in gender:
			totalDictF[postID] += [userID]#1
	
	for postID in totalDictM.keys():
		totalDictM[postID] = str(len(list(set(totalDictM[postID]))))
		totalDictF[postID] = str(len(list(set(totalDictF[postID]))))
		meanDictM[postID] = str(len(list(set(meanDictM[postID]))))
		meanDictF[postID] = str(len(list(set(meanDictF[postID]))))
		viableDictM[postID] = str(len(list(set(viableDictM[postID]))))
		viableDictF[postID] = str(len(list(set(viableDictF[postID]))))

	return totalDictM, totalDictF, meanDictM,viableDictM,  meanDictF,viableDictF

def commentSentimentStats():
	lines = open("StatsForPostsWithCodedComments.csv").readlines()[1:]
	totalDictM, totalDictF, meanDictM,viableDictM,  meanDictF,viableDictF = assignCommentSentiment()
	f = open("StatsForPostsWithCodedCommentsGender.csv","w")
	f.write("PostID | uni | Size | Religious | State | Politics | Tuition | Post | numLikes | numComments | wordCount | isCoded | Taboo | Stigma | isQuestion | questionType | Loneliness | Stress | Victim|Race|Medical|Excretions|Death|Academics|Money|Drugs|Mental Health|Sex|Character|External|Group|unKind|kind|viable|notViable|prosocial|notProsocial|No. of Male Commentors|No. of Female Commentors|No. of Male Mean Commentors|No. of Female Mean Commentors|No. of Male Viable Commentors|No. of Female Viable Commentors\n")
	for line in lines[1:]:
		line = line.replace("\n","")
		col = line.split("|")
		postID = col[0]
		newLine = line+"|"+ totalDictM[postID]+"|"+ totalDictF[postID]+"|"+ viableDictM[postID]+"|"+ viableDictF[postID]+"|"+ meanDictM[postID]+"|"+ meanDictF[postID]+"\n"
		f.write(newLine)


def genderStatsCoded():
	lines = open("StatsForPostsWithCodedCommentsWithoutGender.csv").readlines()
	f = open("StatsForPostsWithCodedComments.csv","w")

	first = lines[0].rsplit("|",18)[0]
	second = lines[0].split("|",19)[-1]
	newLine = first + "|No. of Male Commentors|No. of Female Commentors|No. of None Commentors|"+second
	f.write(newLine)

	genderPosts = open("StatsForCodedPostsGender.csv").readlines()[1:]
	genderDict = {}
	for post in genderPosts:
		col = post.split("|")
		postID = col[0]
		genderDict[postID] = [col[19], col[20], col[21].replace("\n","")]
		
	
	for line in lines[1:]:
		col = line.split("|")
		postID = col[0]
		if postID in genderDict.keys():
			male, female, none = genderDict[postID][0],genderDict[postID][1],genderDict[postID][2]
			#print male, female, none
		first = line.rsplit("|",18)[0]
		second = line.split("|",19)[-1]
		newLine = first + "|"+male+"|"+female+"|"+none+"|"+second
		f.write(newLine)



def processGenderStats():
	#lines = open("StatsForCodedPostsGender.csv").readlines()[1:]
	lines = open("StatsForPostsWithCodedCommentsGender.csv").readlines()[1:]
	#count = 0
	tabooList = ['Race/Protected Groups', 'Death', 'Academics', 'Drugs', 'Medical', 'Mental Health', 'Money/Financial', 'Excretions', 'Sex']
	stigmaList = ["Group","Character","External"]
	questionList = ['Social Connection/Invitation', 'Opinion/Recommendation', 'Factual Knowledge', 'Rhetorical','Offer', ]

	tabooDictM, stigmaDictM, questionDictM = {}, {}, {}
	tabooDictF, stigmaDictF, questionDictF = {}, {}, {}
	lonelinessMale, lonelinessFemale, stressMale, stressFemale, victimMale, victimFemale = [],[],[],[],[],[]

	male, female = [],[]

	for line in lines:
		#count += 1
		col = line.split("|")
		taboo = col[12]
		stigma = col[13]
		question = col[15]
		isQuestion = col[14]

		

		numMale = int(col[-6])
		
		numFemale = int(col[-5])
		loneliness = col[16]
		stress = col[17]
		victim = col[18]

		male += [numMale]
		female += [numFemale]

		if 'Y' not in isQuestion:
			continue

		
		if taboo in tabooList:
			if taboo in tabooDictM.keys():
				tabooDictM[taboo] += [numMale]
				tabooDictF[taboo] += [numFemale]
			else:
				tabooDictM[taboo] = [numMale]
				tabooDictF[taboo] = [numFemale]

		if stigma in stigmaList:
			if stigma in stigmaDictM.keys():
				stigmaDictM[stigma] += [numMale]
				stigmaDictF[stigma] += [numFemale]
			else:
				stigmaDictM[stigma] = [numMale]
				stigmaDictF[stigma] = [numFemale]

		if question in questionList:
			if question in questionDictM.keys():
				questionDictM[question] += [numMale]
				questionDictF[question] += [numFemale]
			else:
				questionDictM[question] = [numMale]
				questionDictF[question] = [numFemale]

		

		if "Y" in victim:
			victimMale += [numMale]
			victimFemale += [numFemale]

		if "Y" in stress:
			stressMale += [numMale]
			stressFemale += [numFemale]

		if "Y" in loneliness:
			lonelinessMale += [numMale]
			lonelinessFemale += [numFemale]

	MeanM, SEMM, MeanF, SEMF = [],[],[],[]
	print "Taboo, Mean No. of Male Mean Commentors (S.D. for same),Mean No. of Female Mean Commentors (S.D. for same)"
	for taboo in tabooList:
		MeanM = Mean(tabooDictM[taboo])
		SEMM = Sem(tabooDictM[taboo])
		MeanF = Mean(tabooDictF[taboo])
		SEMF = Sem(tabooDictF[taboo])
		if MeanF ==0:
			avg = 0
		else:
			avg = MeanM/MeanF
		print taboo, "Male",MeanM,"(", SEMM, ") Female", MeanF,"(", SEMF, ")", avg

	for stigma in stigmaList:
		MeanM = Mean(stigmaDictM[stigma])
		SEMM = Sem(stigmaDictM[stigma])
		MeanF = Mean(stigmaDictF[stigma])
		SEMF = Sem(stigmaDictF[stigma])
		if MeanF ==0:
			avg = 0
		else:
			avg = MeanM/MeanF
		print stigma, "Male",MeanM,"(", SEMM, ") Female", MeanF,"(", SEMF, ")",avg

	for question in questionList[:-1]:
		MeanM = Mean(questionDictM[question])
		SEMM = Sem(questionDictM[question])
		MeanF = Mean(questionDictF[question])
		SEMF = Sem(questionDictF[question])
		if MeanF ==0:
			avg = 0
		else:
			avg = MeanM/MeanF
		print question, "Male",MeanM,"(", SEMM, ") Female", MeanF,"(", SEMF, ")",avg

	print "loneliness", "Male",Mean(lonelinessMale),"(", Sem(lonelinessMale), ") Female",Mean(lonelinessFemale) ,"(", Sem(lonelinessFemale) , ")"
	print "stress", "Male",Mean(stressMale),"(", Sem(stressMale), ") Female",Mean(stressFemale) ,"(", Sem(stressFemale) 
	print "victim", "Male",Mean(victimMale),"(", Sem(victimMale), ") Female",Mean(victimFemale) ,"(", Sem(victimFemale) 

	avg = Mean(male)/Mean(female)
	print Mean(male), Sem(male), Mean(female), Sem(female), avg

def noGender(userID,graph, communities):
	
	try:
		fbDetails = graph.get_object(userID)
		if "gender" in fbDetails.keys():
			if "female" in fbDetails["gender"]:
				return "Female",communities
			elif "male" in fbDetails["gender"]:
				return "Male",communities
			else:
				return "None",communities
		else:
			if "first_name" not in fbDetails:
				communities += [fbDetails]
				return "Communities", communities
			else:
				return "No gender", communities
						
	except:
		return "No account", communities

def getGenderQuestionPosts():
	comments = processCommentList()
	communities = []
	graph = facebook.GraphAPI("CAAGljQ0ymaQBAAuZCf7ZASA00BDYS43yXdYfkPlvDPtL7FzFa6lGAKUvi0J9ZCwRqe42jwO5ACEiz1YzB3Czd0yS29RqLJp1nWZBNcjliZAr1o2jjWwakGIJw4ctsEZBmMZBL329AZB73RZAixjsmB51P8sg6GWvccM25TxprAoBwVsNer6D7MJagGrkGOXCS1Ku8FFLsZB0xkglvpW5jZCgMDKCGitj2NbkEIZD")
	userGender = pickle.load(open('genderDict.pkl', 'rb'))
	noGenderList,noGenderDict = [],{}
	for userID in userGender:
		if "None" in userGender[userID]:
			noGenderList += [userID]
	
	for userID in noGenderList:
		noGenderDict[userID],communities = noGender(userID, graph, communities)

	return noGenderDict, communities











		

		
