from __future__ import division
from collections import Counter
from scipy import mean, std, stats 
from scipy.stats import sem

def assignCommentCode():	

	lines = open("StatsForComments.csv").readlines()[1:]
	comments = {}

	for line in lines:
		cols = line.split("|")

		commentID = cols[0]
		postID = cols[1]
		viable = cols[11]
		mean = cols[12]
		if "Y" not in mean and "Y" in viable:
			prosocial = "Y"
		else:
			prosocial = "N"
		taboo = cols[14]
		stigma = cols[15]

		comment = {}

		if taboo:
			comment["taboo"] = [taboo]
		else:
			comment["taboo"] = []
		
		if stigma:
			comment["stigma"]  = [stigma]
		else:
			comment["stigma"] = []

		comment["isMean"] = [mean]
		comment["isViable"] = [viable]
		comment["isProsocial"] = [prosocial]

		if postID not in comments.keys():

			comments[postID] = comment

		else:
			comments[postID]["taboo"] += comment["taboo"]
			comments[postID]["stigma"] += comment["stigma"]
			comments[postID]["isMean"] += comment["isMean"]
			comments[postID]["isProsocial"] += comment["isProsocial"]
			comments[postID]["isViable"] += comment["isViable"]

	return comments


def processQuestionsComments():
	tabooDict = {'A':"Race",'C':"Medical",'D':"Death",'E':"Excretions",'G':"Academics",'M':"Mental Health",'S':"Sex",'U':"Drugs",'W':"Money"}
	stigmaDict = {"E":"External", "C":"Character", "G": "Group"}

	f = open("StatsForPostsWithCodedComments.csv","w")
	comments = assignCommentCode()
	lines = open("StatsForPosts.csv").readlines()
	header = lines[0][:-1]+"|"
	lines = lines[1:]

	for key in tabooDict:
		header += tabooDict[key]+"|"

	for key in stigmaDict:
		header += stigmaDict[key]+"|"

	header += "unKind|kind|viable|notViable|prosocial|notProsocial\n"
	f.write(header)

	for line in lines:
		comment = {}
		cols = line.split("|")
		postID = cols[0]

		if postID not in comments:
			continue

		if "taboo" not in comments[postID]:
			commentTaboo = {}
		else:
			commentTaboo = Counter(comments[postID]["taboo"])

		if "stigma" not in comments[postID]:
			commentStigma = {}
		else:
			commentStigma = Counter(comments[postID]["stigma"])

		if "isMean" not in comments[postID]:
			commentMean = {}
		else:
			commentMean = Counter(comments[postID]["isMean"])

		if "isViable" not in comments[postID]:
			commentViable = {}
		else:
			commentViable = Counter(comments[postID]["isViable"])

		if "isProsocial" not in comments[postID]:
			commentProsocial = {}
		else:
			commentProsocial = Counter(comments[postID]["isProsocial"])

		newLine = line[:-1]+"|"
		

		for key in tabooDict:
			if key not in commentTaboo:
				newLine += "0|"
			else:
				newLine += str(commentTaboo[key])+"|"

		for key in stigmaDict:
			if key not in commentStigma:
				newLine += "0|"
			else:
				newLine += str(commentStigma[key])+"|"

		if "Y" not in commentMean:
			newLine += "0|"
		else:
			newLine += str(commentMean["Y"])+"|"

		if "N" not in commentMean:
			newLine += "0|"
		else:
			newLine += str(commentMean["N"])+"|"

		if "Y" not in commentViable:
			newLine += "0|"
		else:
			newLine += str(commentViable["Y"])+"|"

		if "N" not in commentViable:
			newLine += "0|"
		else:
			newLine += str(commentViable["N"])+"|"

		if "Y" not in commentProsocial:
			newLine += "0|"
		else:
			newLine += str(commentProsocial["Y"])+"|"

		if "N" not in commentProsocial:
			newLine += "0\n"
		else:
			newLine += str(commentProsocial["N"])+"\n"

		f.write(newLine)

def extractInfo():
	lines = open("StatsForPostsWithCodedComments.csv").readlines()[1:]

	tabooColDict = {"Race":19,"Medical":20, "Excretions":21, "Death":22, "Academics":23,"Money":24, "Drugs":25, "Mental Health":26, "Sex":27}
	stigmaColDict = {"Character":28, "External":29, "Group":30}
	tabooList = ['Race', 'Death', 'Academics', 'Drugs', 'Medical', 'Mental Health', 'Money', 'Excretions', 'Sex']#,'None']
	stigmaList = ["Group","Character","External"]#,"None"]
	questionList = ['Social Connection/Invitation', 'Opinion/Recommendation', 'Offer', 'Factual Knowledge', 'Rhetorical']#,'None']


	commentSumTaboo1,commentSumStigma1,commentSumTaboo0,commentSumStigma0 = {}, {}, {}, {}
	commentSumTaboo2, commentSumStigma2, commentSumStigma,commentSumTaboo = {},{},{}, {}
	totalComments,totalViable, totalUnkind, totalProsocial, numViable, numUnkind, numProsocial = {},{},{},{},{},{}, {}
	'''
	for key in tabooColDict.keys():
		commentSumTaboo1[key] = 0
		commentSumTaboo0[key] = 0
		commentSumTaboo2[key] = 0
		commentSumTaboo[key] = []
		totalComments[key] = []
		numViable[key] = []
		numUnkind[key] = []
		numProsocial[key] = []
		totalViable[key] = []
		totalUnkind[key] = []
		totalProsocial[key] = []
	'''
	for key in stigmaList:
		totalComments[key] = []
		numViable[key] = []
		numUnkind[key] = []
		numProsocial[key] = []

	commentSumStigma = {}
	for key in stigmaColDict.keys():
		commentSumStigma1[key] = 0
		commentSumStigma0[key] = 0
		commentSumStigma2[key] = 0
		commentSumStigma[key] = []
	#x = []
	'''
	commentSumTaboo0["None"]=commentSumTaboo1["None"]=commentSumTaboo2["None"] = 0
	colmmentSumStigma0["None"]=commentSumStigma1["None"] = commentSumStigma2["None"] = 0
	'''
	for line in lines:
		numSimilar = 0
		numOtherTaboos = 0
		cols = line.split("|")
		taboo = cols[12]
		stigma = cols[13]
		numComments = int(cols[9])
		questionType = cols[15]
		#x += [questionType]

		if 'Race/Protected Groups' in taboo:
			taboo = 'Race'
		elif 'Money/Financial' in taboo:
			taboo = 'Money'
		'''
		if questionType in questionList:
			totalComments[questionType] += [numComments]

			numUnkind[questionType] += [int(cols[31])] #unkind or mean
			numViable[questionType] += [int(cols[33])] #viable
			numProsocial[questionType] += [int(cols[35])] #prosocial
		
		if taboo in tabooColDict.keys():
			totalComments[taboo] += [numComments]

			numUnkind[taboo] += [int(cols[31])] #unkind or mean
			numViable[taboo] += [int(cols[33])] #viable
			numProsocial[taboo] += [int(cols[35])] #prosocial

			numSimilar = int(cols[tabooColDict[taboo]])
			
			numOther = numComments - numSimilar
			commentSumTaboo[taboo] += [numSimilar]
			commentSumTaboo1[taboo] += numSimilar
			commentSumTaboo0[taboo] += numOther
			other = list(set(tabooColDict.values()) - set([tabooColDict[taboo]]))
			
			print taboo, tabooColDict[taboo],other
			print taboo
			print numComments
			print tabooColDict[taboo],cols[tabooColDict[taboo]]
			print "++++++++++++++++++++"
			
			for key in other:
				numOtherTaboos += int(cols[key])
				#print key,cols[key]

			commentSumTaboo2[taboo] += numOtherTaboos
			
			print "**************"
			print commentSumTaboo1
			print commentSumTaboo2
			print
			
		'''
		numSimilar = 0

		if stigma in stigmaList:

			totalComments[stigma] += [numComments]

			numUnkind[stigma] += [int(cols[31])] #unkind or mean
			numViable[stigma] += [int(cols[33])] #viable
			numProsocial[stigma] += [int(cols[35])] #prosocial

			numSimilar = int(cols[stigmaColDict[stigma]])

			numOther = numComments - numSimilar
			commentSumStigma[stigma] += [numSimilar]
			commentSumStigma1[stigma] += numSimilar
			commentSumStigma0[stigma] += numOther
		
	#print list(set(x))
	print commentSumStigma1
	print commentSumStigma0
	print commentSumStigma2
	print
	print "Stats"
	

	Mean, Sem, Std,Percent = [],[],[],[]

	for key in stigmaList:
		
		Mean += [mean(commentSumStigma[key])]
		Sem += [sem(commentSumStigma[key])]
		#Mean += [mean(commentSumTaboo[key])]
		#Sem += [sem(commentSumTaboo[key])]
		#Std += [std(commentSumTaboo[key])]
		
		
		#Percent += [100 *(mean(numProsocial[key])/mean(totalComments[key]))]
		

	print Mean
	print Sem
	#print Std
	#print Percent



#assignCommentCode()
processQuestionsComments()


		
		









		















	