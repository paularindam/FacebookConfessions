from __future__ import division
import math
import scipy
from scipy import mean, stats
from scipy.stats import mode
from processUnis import *
from mapUnis import *
import sys

qPosts,allPosts = processPosts()
comments = processCommentList()
f = open("StatsByUnis.csv","w")
f.write("Uni| School Category | Ranking | Population | Tuition Cost | Religious | State | R or D State (last election) | (All)Number of posts| (All) Total No. of Comments|(All) Mean Post Length | (All) S.D. Post Length | (All) Median Post Length | (All) Mode Post Length | (All) Mean No. of Comments | (All) S.D. No. of Comments | (All) Median No. of Comments | (All) Mode No. of Comments | (All) Mean No. of Likes | (All) S.D. No. of Likes | (All) Median No. of Likes | (All) Mode No. of Likes | (Question) Number of question posts | (Question) Percent % of posts which are questions| (Question) Total No.of Comments |(Question) Mean Post Length | (Question) S.D. Post Length | (Question) Median Post Length | (Question) Mode Post Length | (Question) Mean No. of Comments | (Question) S.D. No. of Comments | (Question) Median No. of Comments | (Question) Mode No. of Comments | (Question) Mean No. of Likes | (Question) S.D. No. of Likes | (Question) Median No. of Likes | (Question) Mode No. of Likes | (Question) No. of unique Commentors | (Question) No. of comments per unique commentor | (Question) Mean Length of comments| (Question) S.D. Length of comments | (Question) Median Length of comments | (Question) Mode Length of comments\n")
g = open("SimpleStatsByUnis.csv","w")
g.write("Uni| (All) Mean Word Count |(All)Std Word Count |(questions) Mean Word Count |(questions)Std Word Count |(Comments) Mean Word Count |(Comments)Std Word Count \n")
#g.write("Uni| School Category | Ranking | Population | Tuition Cost | Religious | State | R or D State (last election) | (All)Number of posts| (All) Total No. of Comments|(All) Mean Post Length | (All) S.D. Post Length | (All) ")
def postStats(posts):
	stats = {}
	numLikes = []
	zeroLikes = 0
	numComments = []
	zeroComments = 0
	length = []
	neglected = 0
	for post in posts:
		#try:
		
		#print post
		numLike = post['numLikes'].replace('"','')
		numComment = post['numComments'].replace('"','')
		if numLike.isdigit() == True:
			numLike = int(numLike)
		else:
			numLike = 0
		if numComment.isdigit() == True:
			numComment = int(numComment)
		else:
			numComment = 0
		numLikes += [numLike]
		numComments += [numComment]
		if numComment == 0 :
			zeroComments += 1
		if numLike == 0:
			zeroLikes  +=1
		length += [len(post['message'])]
		#except:
		#	neglected += 1

	stats['meanLikes'] = str(scipy.mean(numLikes))
	stats['meanComments'] = str(scipy.mean(numComments))
	stats['meanLength'] = str(scipy.mean(length))
	stats['stdLikes'] = str(scipy.std(numLikes))
	stats['stdComments'] = str(scipy.std(numComments))
	stats['stdLength'] = str(scipy.std(length))
	stats['medianLikes'] = str(scipy.median(numLikes))
	stats['medianComments'] = str(scipy.median(numComments))
	stats['medianLength'] = str(scipy.median(length))
	
	try:
		stats['modeLikes'] = str(mode(numLikes)[0][0])
	except:
		stats['modeLikes'] = "0"
	try:
		stats['modeComments'] = str(mode(numComments)[0][0])
	except:
		stats['modeComments'] = "0"
	try:
		stats['modeLength'] = str(mode(length)[0][0])
	except:
		stats['modeLength'] = "0"
	
	stats['numLikes'] = numLikes
	stats['numComments'] = numComments
	stats['zeroLikes'] = zeroLikes
	stats['zeroComments'] = zeroComments
	stats['length'] = length
	stats['neglected'] = neglected

	return stats


def commentStats(comments):
	numLikes = []
	numComments = []
	uniqueCommentors = []
	uniqueNames = []
	length = []
	wordCount = []
	stats = {}
	count = 0
	for postID in comments:
		count += 1
		try:
			commentsPost = comments[postID]

			for comment in commentsPost:
				uniqueCommentors += [comment['userID']]
				uniqueNames += [comment['userName']]
				numLikes += [int(comment['likeCount'])]
				length += [len(comment['message'])]
				wordCount += [len(comment['message'].split())]

			numComments += [len(commentsPost)]
		except:
			print postID
	
	uniqueCommentors = list(set(uniqueCommentors))
	stats['numUniqueCommentors'] = len(uniqueCommentors)
	stats['numComments'] = len(numComments)
	stats['meanLikes'] = str(scipy.mean(numLikes))
	stats['stdLikes'] = str(scipy.std(numLikes))
	stats['medianLikes'] = str(scipy.median(numLikes))
	
	try:
		stats['modeLikes'] = str(mode(numLikes)[0][0])
	except:
		stats['modeLikes'] = "0"
	
	stats['meanWordCount'] = str(scipy.mean(wordCount))
	stats['stdWordCount'] = str(scipy.std(wordCount))

	stats['meanLength'] = str(scipy.mean(length))
	stats['stdLength'] = str(scipy.std(length))
	stats['medianLength'] = str(scipy.median(length))
	
	try:
		stats['modeLength'] = str(mode(length)[0][0])
	except:
		stats['modeLength'] = "0"
	
	stats['numLikes'] = numLikes
	stats['uniqueCommentors'] = uniqueCommentors
	stats['length'] = length

	return stats


def allStats():
	allStat = {}
	questionStat = {}
	commentStat = {}
	uniStats = cleanUniDict()
	for uni in qPosts.keys():
		if "Davis" in uni:
			continue
		total = len(allPosts[uni])
		questions = len(qPosts[uni])
		percent = (questions/total) * 100
		print "here1"
		questionStat[uni] = postStats(qPosts[uni])
		allStat[uni] = postStats(allPosts[uni])
		commentStat[uni] = commentStats(comments[uni])
		if commentStat[uni]['numUniqueCommentors'] == 0 or commentStat[uni]['numComments'] ==0 :
			commentorPer = "0"
		else:
			commentorPer = str(commentStat[uni]['numComments']/commentStat[uni]['numUniqueCommentors'])
		totalComments =  sum(allStat[uni]['numComments'])
		questionComments = sum(questionStat[uni]['numComments'])
	

		if commentStat[uni]['meanLength'] == "nan":
			commentStat[uni]['meanLength'] = "0"
		if commentStat[uni]['stdLength'] == "nan":
			commentStat[uni]['stdLength'] = "0"
		if commentStat[uni]['medianLength'] == "nan":
			commentStat[uni]['medianLength'] = "0"
		
		f.write(uni + "|" + str(uniStats[uni]["category"])+ "|"+str(uniStats[uni]["rank"])+"|"+str(uniStats[uni]["size"])+"|"+uniStats[uni]["tuition"]+"|"+uniStats[uni]["isReligious"]+"|"+uniStats[uni]["state"]+"|"+uniStats[uni]["politics"]+"|"+str(len(allPosts[uni])) + "|"+str(totalComments)+"|")
		f.write(allStat[uni]['meanLength']+"|"+allStat[uni]['stdLength']+"|"+allStat[uni]['medianLength']+"|"+allStat[uni]['modeLength']+"|")
		f.write(allStat[uni]['meanComments']+"|"+allStat[uni]['stdComments']+"|"+allStat[uni]['medianComments']+"|"+allStat[uni]['modeComments']+"|"+allStat[uni]['meanLikes']+"|"+allStat[uni]['stdLikes']+"|"+allStat[uni]['medianLikes']+"|"+allStat[uni]['modeLikes']+"|")
		f.write(str(len(qPosts[uni]))+"|"+str(percent)+"|"+str(questionComments)+"|"+questionStat[uni]['meanLength']+"|"+questionStat[uni]['stdLength']+"|"+questionStat[uni]['medianLength']+"|"+questionStat[uni]['modeLength']+"|")
		f.write(questionStat[uni]['meanComments']+"|"+questionStat[uni]['stdComments']+"|"+questionStat[uni]['medianComments']+"|"+questionStat[uni]['modeComments']+"|"+questionStat[uni]['meanLikes']+"|"+questionStat[uni]['stdLikes']+"|"+questionStat[uni]['medianLikes']+"|"+questionStat[uni]['modeLikes']+"|")
		f.write(str(commentStat[uni]['numUniqueCommentors'])+"|"+commentorPer+"|"+commentStat[uni]['meanLength']+"|"+commentStat[uni]['stdLength']+"|"+commentStat[uni]['medianLength']+"|"+commentStat[uni]['modeLength']+"\n")
	

def simplePostStats(posts):
	stats = {}
	numLikes = []
	zeroLikes = 0
	numComments = []
	zeroComments = 0
	length = []
	neglected = 0
	wordCount = []
	for post in posts:
		#try:
		
		#print post
		numLike = post['numLikes'].replace('"','')
		numComment = post['numComments'].replace('"','')
		if numLike.isdigit() == True:
			numLike = int(numLike)
		else:
			numLike = 0
		if numComment.isdigit() == True:
			numComment = int(numComment)
		else:
			numComment = 0
		numLikes += [numLike]
		numComments += [numComment]
		if numComment == 0 :
			zeroComments += 1
		if numLike == 0:
			zeroLikes  +=1
		length += [len(post['message'])]
		wordCount += [len(post['message'].split())]
		#except:
		#	neglected += 1

	stats['meanLikes'] = str(scipy.mean(numLikes))
	stats['meanComments'] = str(scipy.mean(numComments))
	stats['meanLength'] = str(scipy.mean(length))
	stats['stdLikes'] = str(scipy.std(numLikes))
	stats['stdComments'] = str(scipy.std(numComments))
	stats['stdLength'] = str(scipy.std(length))
	stats['meanWordCount'] = str(scipy.mean(wordCount))
	stats['stdWordCount'] = str(scipy.std(wordCount))
	
	
	stats['numLikes'] = numLikes
	stats['numComments'] = numComments
	stats['zeroLikes'] = zeroLikes
	stats['zeroComments'] = zeroComments
	stats['length'] = length
	stats['wordCount'] = wordCount
	stats['neglected'] = neglected

	return stats


def simpleCommentStats(comments):
	numLikes = []
	numComments = []
	uniqueCommentors = []
	uniqueNames = []
	length = []
	wordCount = []
	stats = {}
	count = 0
	for postID in comments:
		count += 1
		try:
			commentsPost = comments[postID]

			for comment in commentsPost:
				uniqueCommentors += [comment['userID']]
				uniqueNames += [comment['userName']]
				numLikes += [int(comment['likeCount'])]
				length += [len(comment['message'])]
				wordCount += [len(comment['message'].split())]

			numComments += [len(commentsPost)]
		except:
			print postID
	
	uniqueCommentors = list(set(uniqueCommentors))
	stats['numUniqueCommentors'] = len(uniqueCommentors)
	stats['numComments'] = len(numComments)
	stats['meanLikes'] = str(scipy.mean(numLikes))
	stats['stdLikes'] = str(scipy.std(numLikes))
	
	stats['meanWordCount'] = str(scipy.mean(wordCount))
	stats['stdWordCount'] = str(scipy.std(wordCount))

	stats['meanLength'] = str(scipy.mean(length))
	stats['stdLength'] = str(scipy.std(length))
	
	stats['numLikes'] = numLikes
	stats['uniqueCommentors'] = uniqueCommentors
	stats['length'] = length
	stats['wordCount'] = wordCount

	return stats


def simpleStats():
	allStat = {}
	questionStat = {}
	commentStat = {}
	allWordCount,allLength, questionWordCount,questionLength = [],[],[],[]
	allLikes,allComments, qLikes,qComments = [],[],[],[]
	allZLikes = allZComments = qZLikes = qZComments = 0
	uniStats = cleanUniDict()
	for uni in qPosts.keys():
		total = len(allPosts[uni])
		questions = len(qPosts[uni])
		percent = (questions/total) * 100
		questionStat[uni] = simplePostStats(qPosts[uni])
		allStat[uni] = simplePostStats(allPosts[uni])
		commentStat[uni] = simpleCommentStats(comments[uni])
		if commentStat[uni]['numUniqueCommentors'] == 0 or commentStat[uni]['numComments'] ==0 :
			commentorPer = "0"
		else:
			commentorPer = str(commentStat[uni]['numComments']/commentStat[uni]['numUniqueCommentors'])
		totalComments =  sum(allStat[uni]['numComments'])
		questionComments = sum(questionStat[uni]['numComments'])
	

		if commentStat[uni]['meanLength'] == "nan":
			commentStat[uni]['meanLength'] = "0"
		if commentStat[uni]['stdLength'] == "nan":
			commentStat[uni]['stdLength'] = "0"
		
		#question and all word count & length
		allWordCount += allStat[uni]['wordCount']
		questionWordCount += questionStat[uni]['wordCount']
		allLength += allStat[uni]['length']
		questionLength += questionStat[uni]['length']

		allLikes += allStat[uni]['numLikes']
		allComments += allStat[uni]['numComments']

		qLikes += questionStat[uni]['numLikes']
		qComments += questionStat[uni]['numComments']

		g.write(uni + "|")
		g.write(allStat[uni]['meanWordCount']+"|"+allStat[uni]['stdWordCount']+"|")
		g.write(questionStat[uni]['meanWordCount']+"|"+questionStat[uni]['stdWordCount']+"|")
		g.write(commentStat[uni]['meanWordCount']+"|"+commentStat[uni]['stdWordCount']+"\n")
		# + str(uniStats[uni]["category"])+ "|"+str(uniStats[uni]["rank"])+"|"+str(uniStats[uni]["size"])+"|"+uniStats[uni]["tuition"]+"|"+uniStats[uni]["isReligious"]+"|"+uniStats[uni]["state"]+"|"+uniStats[uni]["politics"]+"|"+str(len(allPosts[uni])) + "|"+str(totalComments)+"|")
		#g.write(allStat[uni]['meanLength']+"|"+allStat[uni]['stdLength']+"|")
		#g.write(allStat[uni]['meanComments']+"|"+allStat[uni]['stdComments']+"|"+allStat[uni]['meanLikes']+"|"+allStat[uni]['stdLikes']+"|")
		#g.write(str(len(qPosts[uni]))+"|"+str(percent)+"|"+str(questionComments)+"|"+questionStat[uni]['meanLength']+"|"+questionStat[uni]['stdLength']+"|"+questionStat[uni]['meanWordCount']+"|"+questionStat[uni]['stdWordCount']+"|")
		#g.write(questionStat[uni]['meanComments']+"|"+questionStat[uni]['stdComments']+"|"+questionStat[uni]['meanLikes']+"|"+questionStat[uni]['stdLikes']+"|")
		#g.write(str(commentStat[uni]['numUniqueCommentors'])+"|"+commentorPer+"|"+commentStat[uni]['meanLength']+"|"+commentStat[uni]['stdLength']+"|"+commentStat[uni]['meanWordCount']+"|"+commentStat[uni]['stdWordCount']+"\n")
	

	numPosts = len(allWordCount)
	numQuestions = len(questionWordCount)

	restLikes = (sum(allLikes) - sum(qLikes))/(numPosts - numQuestions)
	restComments = (sum(allComments) - sum(qComments))/(numPosts - numQuestions)


	'''
	restZLikes = (allZLikes - qZLikes)/(numPosts - numQuestions)
	restZComments = (allZComments - qZComments)/(numPosts - numQuestions)


	restWordCount = (sum(allWordCount) - sum(questionWordCount))/(len(allWordCount)- len(questionWordCount))
	restLength = (sum(allLength) - sum(questionLength))/(len(allLength)- len(questionLength))
	'''
	print "num Likes"
	print "All", mean(allLikes)#allLikes/numPosts
	print "Rest", restLikes
	print "Questions",mean(qLikes)#qZLikes/numQuestions
	
	print
	print
	print "num Comments"
	print "All",mean(allComments)#allZComments	/numPosts
	print "Rest", restComments
	print "Questions",mean(qComments)#/numQuestions
	
	

allStats()
