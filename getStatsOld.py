from __future__ import division
import scipy
from scipy import stats
from scipy.stats import mode
from processUnis import *
from mapUnis import *
import sys

qPosts,allPosts = processPosts()
comments = processCommentsForQuestions()

def postStats(posts):
	stats = {}
	numLikes = []
	zeroLikes = 0
	numComments = []
	zeroComments = 0
	length = []
	neglected = 0
	for post in posts:
		try:
			numLikes += [int(post['numLikes'])]
			numComments += [int(post['numComments'])]
			if int(post['numComments']) == 0 :
				zeroComments += 1
			if int(post['numLikes']) == 0:
				zeroLikes  +=1
			length += [len(post['message'])]
		except:
			neglected += 1

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

#print commentStats(comments['New York University'])
def main():
	print "main"
	allStat = {}
	questionStat = {}
	commentStat = {}
	count = 0
	numLikes = []
	numAllLikes = []
	numComments = []
	numAllComments = []
	postAllLength = []
	postlength = []
	commentlength = []
	numUniqueCommentors = 0
	numAllPosts = numQPosts =  0
	uniStats = cleanUniDict()
	f = open("StatsByUnis2.csv","w")
	f.write("Uni| Population | Tuition Cost | Religious | State | R or D State (last election) | (All)Number of posts| (All) Total No. of Comments|(All) Mean Post Length | (All) S.D. Post Length | (All) Median Post Length | (All) Mode Post Length | (All) Mean No. of Comments | (All) S.D. No. of Comments | (All) Median No. of Comments | (All) Mode No. of Comments | (All) Mean No. of Likes | (All) S.D. No. of Likes | (All) Median No. of Likes | (All) Mode No. of Likes | (Question) Number of question posts | (Question) Percent % of posts which are questions| (Question) Total No.of Comments |(Question) Mean Post Length | (Question) S.D. Post Length | (Question) Median Post Length | (Question) Mode Post Length | (Question) Mean No. of Comments | (Question) S.D. No. of Comments | (Question) Median No. of Comments | (Question) Mode No. of Comments | (Question) Mean No. of Likes | (Question) S.D. No. of Likes | (Question) Median No. of Likes | (Question) Mode No. of Likes | (Question) No. of unique Commentors | (Question) No. of comments per unique commentor | (Question) Mean Length of comments| (Question) S.D. Length of comments | (Question) Median Length of comments | (Question) Mode Length of comments\n")

	for uni in qPosts.keys():
		total = len(allPosts[uni])
		questions = len(qPosts[uni])
		percent = (questions/total) * 100

		questionStat[uni] = postStats(qPosts[uni])
		allStat[uni] = postStats(allPosts[uni])
		commentStat[uni] = commentStats(comments[uni])
		if commentStat[uni]['numUniqueCommentors'] == 0 or commentStat[uni]['numComments'] ==0 :
			commentorPer = 0
		else:
			commentorPer = commentStat[uni]['numComments']/commentStat[uni]['numUniqueCommentors']

		f.write(uni + "|" + uniStats["size")+"|"+uniStats["tuition"]+"|"+uniStats["isReligious")+"|"+uniStats["state"]+"|"+uniStats["politics"]+"|"+str(len(allPosts[uni]) + "|"+str(sum(allStat[uni]['numComments']))+"|")
		f.write(allStat[uni]['meanLength']+"|"+allStat[uni]['stdLength']+"|"+allStat[uni]['medianLength']+"|"+allStat[uni]['modeLength']+"|")
		f.write(allStat[uni]['meanComments']+"|"+allStat[uni]['stdComments']+"|"+allStat[uni]['medianComments']+"|"+allStat[uni]['modeComments']+"|"+allStat[uni]['meanLikes']+"|"+allStat[uni]['stdLikes']+"|"+allStat[uni]['medianLikes']+"|"+allStat[uni]['modeLikes']+"|"+)
		f.write(len(qPosts[uni])+"|"+percent+"|"+sum(questionStat[uni]['numComments'])+"|"+questionStat[uni]['meanLength']+"|"+questionStat[uni]['stdLength']+"|"+questionStat[uni]['medianLength']+"|"+questionStat[uni]['modeLength']+"|")
		f.write(questionStat[uni]['meanComments']+"|"+questionStat[uni]['stdComments']+"|"+questionStat[uni]['medianComments']+"|"+questionStat[uni]['modeComments']+"|"+questionStat[uni]['meanLikes']+"|"+questionStat[uni]['stdLikes']+"|"+questionStat[uni]['medianLikes']+"|"+questionStat[uni]['modeLikes']+"|"+)
		f.write(commentStat[uni]['numUniqueCommentors']+"|"+commentorPer+"|"+commentStat[uni]['meanLength']+"|"+commentStat[uni]['stdLength']+"|"+commentStat[uni]['medianLength']+"|"+commentStat[uni]['modeLength']+"\n")
		break
		'''
		print "*******************"+uni+"*********************"
		print "Overall Stats (i.e. not just Questions but entire FCB) :-"
		print
		print "Total number of posts in "+uni+" FCB(/s) :",len(allPosts[uni])
		print "post length(number of characters in a post) : "
		print "Mean : ",allStat[uni]['meanLength']
		print "Standard Deviation :",allStat[uni]['stdLength']
		print "Median :",allStat[uni]['medianLength']
		print "Mode :",allStat[uni]['modeLength']
		print
		print "Total number of comments for posts in entire FCB",sum(allStat[uni]['numComments'])
		
		print
		print "No. of Comments :-"
		print "Mean : ", allStat[uni]['meanComments']
		print "Std. Dev. : ", allStat[uni]['stdComments']
		print "Median : ",allStat[uni]['medianComments']
		print "Mode : ",allStat[uni]['modeComments']
		print
		print "No. of Likes:-"
		print "Mean: ", allStat[uni]['meanLikes']
		print "Std. Dev:" , allStat[uni]['stdLikes']
		print "Median :",allStat[uni]['medianLikes']
		print "Mode :",allStat[uni]['modeLikes']
		print
		print "Number of posts with zero Comments",allStat[uni]['zeroComments']
		print "Number of posts with zero Likes",allStat[uni]['zeroLikes']

		print 
		print
		print "Question Stats :-"
		print 
		print
		print "Total number of question posts in "+uni+" FCB(/s) :",len(qPosts[uni])
		print "Percent of questions in the FCB :",percent
		print "Total number of comments for posts with questions in entire FCB(number of characters in a post)",sum(questionStat[uni]['numComments'])
		print 
		print "Length of posts (with questions) :- "
		print "Mean : ",questionStat[uni]['meanLength']
		print "Std.Dev :" , questionStat[uni]['stdLength']
		print "Median :",questionStat[uni]['medianLength']
		print "Mode :",questionStat[uni]['modeLength']
		print "No. of Comments :-"
		print "Mean : "+questionStat[uni]['meanComments']
		print "Std. Dev : ", questionStat[uni]['stdComments']
		print "Median :",questionStat[uni]['medianComments']
		print "Mode :",questionStat[uni]['modeComments']
		print "No. of Likes :-"
		print "Mean : ", questionStat[uni]['meanLikes']
		print "Std. Dev : ", questionStat[uni]['stdLikes']
		print "Median : ",questionStat[uni]['medianLikes']
		print "Mode : ",questionStat[uni]['modeLikes']
		print
		print "Number of unique Commentors", commentStat[uni]['numUniqueCommentors']
		print "Number of comments per unique commentor",commentorPer
		print
		print "Length of comments :-"
		print "Mean :",commentStat[uni]['meanLength']
		print "Std.Dev :",commentStat[uni]['stdLength']
		print "Median :",commentStat[uni]['medianLength']
		print "Mode :",commentStat[uni]['modeLength']
		print
		print "Number of question posts with zero Comments",questionStat[uni]['zeroComments']
		print "Number of question posts with zero Likes",questionStat[uni]['zeroLikes']
		print
		print "Note: The mean for number of Likes and Comments indicate the number of comments and likes per post.Also the high number of posts with zero Comments/Likes explains 0 Mode and sometimes 0 Median"

		
		print questionStat[uni]['stdLikes']
		print allStat[uni]['medianComments']
		print questionStat[uni]['neglected']
		print percent
		print commentorPer
		
		numAllLikes += allStat[uni]['numLikes']
		numAllComments += allStat[uni]['numComments']
		numLikes += questionStat[uni]['numLikes']
		numComments += questionStat[uni]['numComments']
		numAllPosts += len(allPosts[uni])
		numQPosts += len(qPosts[uni])
		postAllLength += allStat[uni]['length']
		postlength += questionStat[uni]['length']
		commentlength += commentStat[uni]['length']
		numUniqueCommentors += commentStat[uni]['numUniqueCommentors']

		count += 1
		print count

	commentorPer = sum(numAllComments)/numUniqueCommentors

	print "*****************************Overall Stats************************"
	print "All Posts (i.e. not only Questions) "
	print "------------------------------------"
	print
	print "Total posts :" ,numAllPosts
	print
	print "No. of Likes on Posts :-"
	print "Mean : ",scipy.mean(numAllLikes)
	print "Std.Dev : ",scipy.std(numAllLikes)
	print "Median : ",scipy.median(numAllLikes)
	print "Mode : ", mode(numAllLikes)[0][0]
	print
	print "No. of Comments on Posts :-"
	print "Mean : ",scipy.mean(numAllComments)
	print "Std.Dev : ",scipy.std(numAllComments)
	print "Median : ",scipy.median(numAllComments)
	print "Mode : ", mode(numAllComments)[0][0]
	print
	print "Length on Posts :-"
	print "Mean : ",scipy.mean(postAllLength)
	print "Std.Dev : ",scipy.std(postAllLength)
	print "Median : ",scipy.median(postAllLength)
	print "Mode : ", mode(postAllLength)[0][0]
	print
	print
	print "For Posts with Questions :"
	print "------------------------------------"
	print
	print "Total posts with Questions :" ,numQPosts
	print "% of questions ", (numQPosts/numAllPosts) * 100
	print
	print "No. of Likes on Posts :-"
	print "Mean : ",scipy.mean(numLikes)
	print "Std.Dev : ",scipy.std(numLikes)
	print "Median : ",scipy.median(numLikes)
	print "Mode : ", mode(numLikes)[0][0]
	print
	print "No. of Comments on Posts :-"
	print "Mean : ",scipy.mean(numComments)
	print "Std.Dev : ",scipy.std(numComments)
	print "Median : ",scipy.median(numComments)
	print "Mode : ", mode(numComments)[0][0]
	print
	print "Length of Posts with Questions:-"
	print "Mean : ",scipy.mean(postlength)
	print "Std.Dev : ",scipy.std(postlength)
	print "Median : ",scipy.median(postlength)
	print "Mode : ", mode(postlength)[0][0]
	print
	print "Length of Comments for Posts with Questions:-"
	print "Mean : ",scipy.mean(commentlength)
	print "Std.Dev : ",scipy.std(commentlength)
	print "Median : ",scipy.median(commentlength)
	print "Mode : ", mode(commentlength)[0][0]
	print
	print "Number of uniqueCommentors", numUniqueCommentors
	print "Avg. number of comments per uniqueCommentor : ", sum(numComments)/numUniqueCommentors

		'''
	

#Total Posts for a board
#Total number of questions for a board
#Percentage 
#main()








		


