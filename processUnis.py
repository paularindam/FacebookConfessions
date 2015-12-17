# -*- coding: utf-8 -*-
import os
from manageExceptions import *
from processLIWC import *
from extractPercent import *
import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
import iso8601

def getScrapedUnis():
	unis = open("lenPosts.dat").readlines()
	uniList = []

	for uni in unis:
		uniList += [uni.split(":")[0]]

	uniList = univCorrect(uniList)

	return uniList

def processTextWithPostID(category, path, LIWCategory = None, numWords = 1):

	posts = open(path).readlines()[1:]
	allPosts = []
	catPosts = []
	postIDs = []

	inCategory = False
	for post in posts:
		
		elements = post.split("|")
		if category == "posts":
			message = elements[2]
		elif category == "comments":
			message = elements[6]

		message = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', message)
		
		if "?" not in message: 
			continue

		if LIWCategory != None:	
			inCategory = processLIWC(message, LIWCategory, numWords)
		
		dct = {}

		if category == "posts":
			dct["postID"] = elements[0].replace('"','')
			dct["time"] = elements[1] 
			dct["message"] = elements[2]
			dct["numLikes"] = elements[3]
			dct["numComments"] = elements[4]
			dct["type"] = elements[5]
			
			#allPosts.append(dct)
			#if LIWCategory == None or inCategory == True:
				#catPosts.append(dct)
		elif category == "comments":
			dct["postID"] = elements[0].replace('"','')
			dct["commentID"] = elements[1] 
			dct["userName"] = elements[2]
			dct["userID"] = elements[3]
			dct["time"] = elements[4]
			dct["likeCount"] = elements[5]
			dct["message"] = elements[6]

		allPosts.append(dct)
		if LIWCategory == None or inCategory == True:
			catPosts.append(dct)
			postIDs += [dct["postID"]]

	return catPosts, allPosts, postIDs

def processTextAll(category, path, LIWCategory = None, numWords = 1):

	posts = open(path).readlines()[1:]
	allPosts = []
	catPosts = []
	inCategory = False
	for post in posts:
		
		elements = post.split("|")
		if category == "posts":
			message = elements[2]
		elif category == "comments":
			message = elements[6]

		message = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', message)
		
		#if "?" not in message: 
		#	continue

		if LIWCategory != None:	
			inCategory = processLIWC(message, LIWCategory, numWords)
		
		dct = {}

		if category == "posts":
			dct["postID"] = elements[0]
			dct["time"] = elements[1] 
			dct["message"] = elements[2]
			dct["numLikes"] = elements[3]
			dct["numComments"] = elements[4]
			dct["type"] = elements[5]
			
			#allPosts.append(dct)
			#if LIWCategory == None or inCategory == True:
				#catPosts.append(dct)
		elif category == "comments":
			dct["postID"] = elements[0]
			dct["commentID"] = elements[1] 
			dct["userName"] = elements[2]
			dct["userID"] = elements[3]
			dct["time"] = elements[4]
			dct["likeCount"] = elements[5]
			dct["message"] = elements[6]

		allPosts.append(dct)
		if LIWCategory == None or inCategory == True:
			catPosts.append(dct)

	return catPosts, allPosts


#Remember that we are only considering posts/comments with questions

def processUnis(path = "USA/", LIWCategory = None):
	postDict = {}
	commentDict = {}
	numQposts = {}
	numQcomments = {}

	unis = []
	lst = os.listdir(path)

	for ele in lst:
		uni = ele
		if "post" in ele:
			
			uni = uni.split("post")[0]
			if ":" in uni:
				uni = uni.split(":")[0]

			uni = revCorrect(uni)
			if "Loyola" in uni or "UChicago" in uni or "Southwestern" in uni or "Rhodes" in uni:
				continue
			postDict[uni], numQposts[uni] = processText("posts",path+ele, LIWCategory)

		elif "comment" in ele:
		
			uni = uni.split("comment")[0]

			if ":" in uni:
				uni = uni.split(":")[0]
			uni = revCorrect(uni)
			if "Loyola" in uni or "UChicago" in uni or "Southwestern" in uni or "Rhodes" in uni:
				continue
			commentDict[uni], numQcomments[uni]  = processText("comments",path+ele, LIWCategory)
	return postDict, commentDict , numQposts, numQcomments

def processText(path):
	posts = open(path).readlines()[1:]
	allPosts = []
	catPosts = []
	for post in posts:
		elements = post.split("|")
		message = elements[2]
		message = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', message)
		dct = {}
		dct["postID"] = elements[0].replace('"','')
		dct["time"] = elements[1].replace('"','')
		dct["message"] = elements[2].replace('"','')
		dct["numLikes"] = elements[3].replace('"','')
		dct["numComments"] = elements[4].replace('"','')
		dct["type"] = elements[5].replace('"','')

		allPosts.append(dct)

		if "?" not in message: 
			continue
		catPosts.append(dct)
		
		#postIDs += [dct["postID"]]
	return catPosts,allPosts


def processTextDict(path):
	posts = open(path).readlines()[1:]
	allPosts = {}
	catPosts = {}
	for post in posts:
		elements = post.split("|")
		message = elements[2]
		message = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', message)
		dct = {}
		dct["postID"] = elements[0].replace('"','')
		dct["time"] = elements[1] 
		dct["message"] = elements[2]
		dct["numLikes"] = elements[3]
		dct["numComments"] = elements[4]
		dct["type"] = elements[5]

		allPosts[dct["postID"]] = dct

		if "?" not in message: 
			continue
		catPosts[dct["postID"]] = dct
		
		#postIDs += [dct["postID"]]
	return catPosts, allPosts

def processDict():
	postDict = {}
	allPostDict = {}
	postIDs = {}
	unis = []
	lst = os.listdir(path)

	for ele in lst:
		uni = ele

		if "post" in ele:
			
			uni = uni.split("post")[0]
			if ":" in uni:
				uni = uni.split(":")[0]
			if "\xef" in uni:
				uni = uni.split("\xef")[0]
		#uni = revCorrect(uni)
			uni = revCorrect(uni)
			if "Loyola" in uni or "UChicago" in uni or "Southwestern" in uni or "Rhodes" in uni:
				continue
			Posts, All,postID = processTextWithPostID("posts",path+ele, LIWCategory, numWords)


def processPostsForComments(path = "USA/", LIWCategory = None, numWords = 1):
	postDict = {}
	allPostDict = {}
	postIDs = {}
	unis = []
	lst = os.listdir(path)

	for ele in lst:
		uni = ele

		if "post" in ele:
			
			uni = uni.split("post")[0]
			if ":" in uni:
				uni = uni.split(":")[0]
			if "\xef" in uni:
				uni = uni.split("\xef")[0]
		#uni = revCorrect(uni)
			uni = revCorrect(uni)
			if "Loyola" in uni or "UChicago" in uni or "Southwestern" in uni or "Rhodes" in uni:
				continue
			Posts, All,postID = processTextWithPostID("posts",path+ele, LIWCategory, numWords)
			#Posts,All = processText(path+ele)
			if Posts and uni in postDict.keys():
				postDict[uni] += Posts
				allPostDict[uni] += All
				postIDs[uni] += postID
			elif Posts and uni not in postDict.keys():
				postDict[uni] = Posts
				allPostDict[uni] = All
				postIDs[uni] = postID

	return postDict, allPostDict, postIDs

def processPosts(path = "USA/", LIWCategory = None, numWords = 1):
	postDict = {}
	allPostDict = {}
	postIDs = {}
	unis = []
	lst = os.listdir(path)

	for ele in lst:
		uni = ele

		if "post" in ele:
			
			uni = uni.split("post")[0]
			if ":" in uni:
				uni = uni.split(":")[0]
			if "\xef" in uni:
				uni = uni.split("\xef")[0]
		#uni = revCorrect(uni)
			uni = revCorrect(uni)
			
			
			Posts,All = processText(path+ele)
			if Posts and uni in postDict.keys():
				postDict[uni] += Posts
				allPostDict[uni] += All
			elif Posts and uni not in postDict.keys():
				postDict[uni] = Posts
				allPostDict[uni] = All

	return postDict,allPostDict

def processPostsDict(path = "USA/", LIWCategory = None, numWords = 1):
	postDict = {}
	allPostDict = {}
	postIDs = {}
	unis = []
	lst = os.listdir(path)

	for ele in lst:
		uni = ele

		if "post" in ele:
			
			uni = uni.split("post")[0]
			if ":" in uni:
				uni = uni.split(":")[0]
			if "\xef" in uni:
				uni = uni.split("\xef")[0]
		#uni = revCorrect(uni)
			uni = revCorrect(uni)
			
			
			Posts,All = processTextDict(path+ele)
			if Posts and uni in postDict.keys():
				postDict[uni].update(Posts)
				allPostDict[uni].update(All)
			elif Posts and uni not in postDict.keys():
				postDict[uni] = Posts
				allPostDict[uni] = All

	return postDict

def processPostsUni(univ, path = "USA/", LIWCategory = None, numWords = 1):
	postDict = {}
	allPostDict = {}
	postIDs = {}
	unis = []
	lst = os.listdir(path)

	for ele in lst:
		if univ not in ele:
			continue
		uni = ele

		if "post" in ele:
			
			uni = uni.split("post")[0]
			if ":" in uni:
				uni = uni.split(":")[0]
			if "\xef" in uni:
				uni = uni.split("\xef")[0]
		#uni = revCorrect(uni)
			uni = revCorrect(uni)
			
			
			Posts,All = processTextDict(path+ele)
			if Posts:
				if not postDict:
					postDict = Posts
				else:
					postDict.update(Posts)
				
	

	return postDict

def processPostLikesComments(postID, uni):
	posts = processPostsUni(uni)
	try:
		post =  posts[postID]
		return post["numLikes"], post["numComments"]
	except:
		return -1,-1
	
	
def processCommentsAll(path = "USA/"):
	commentDict = {}
	allCommentDict = {}
	unis = []
	lst = os.listdir(path)
	for ele in lst:
		uni = ele
		if "comment" in ele:
		
			uni = uni.split("comment")[0]

			if ":" in uni:
				uni = uni.split(":")[0]
			if "\xef" in uni:
				uni = uni.split("\xef")[0]
			uni = revCorrect(uni)

		
			Comments, All  = processTextAll("comments",path+ele)


			if uni in commentDict.keys():
				commentDict[uni] += Comments
				allCommentDict[uni] += All
			else:
				commentDict[uni] = Comments
				allCommentDict[uni] = All

	return commentDict, allCommentDict

def processComments():
	commentDict, allCommentDict = processCommentsAll()
	return commentDict

def processCommentText(path,postIDs):

	allComments = open(path).readlines()[1:]
	comments = {}
	for comment in allComments:
		
		elements = comment.split("|")
		postID = elements[0].replace('"','')

		if postID in postIDs:
			
			dct = {}
			dct["commentID"] = elements[1] 
			dct["userName"] = elements[2]
			dct["userID"] = elements[3]
			dct["time"] = elements[4]
			dct["isotime"] = iso8601.parse_date(dct["time"])
			dct["likeCount"] = elements[5]
			dct["message"] = elements[6]

			if postID in comments:
				comments[postID].append(dct)
			else:
				comments[postID] = [dct]


	return comments

def processCommentDict(path,postIDs):

	allComments = open(path).readlines()[1:]
	comments = {}
	for comment in allComments:
		
		elements = comment.split("|")
		postID = elements[0].replace('"','')

		if postID in postIDs:
			
			dct = {}
			#dct["commentID"] = elements[1] 
			dct["userName"] = elements[2]
			dct["userID"] = elements[3]
			dct["time"] = elements[4]
			dct["isotime"] = iso8601.parse_date(dct["time"])
			dct["likeCount"] = elements[5]
			dct["message"] = elements[6]

			comments[elements[1]] = dct


	return comments

def processComment(path = "USA/"):
	posts, allPosts, postIDs = processPostsForComments()
	comments = {}
	lst = os.listdir(path)
	for ele in lst:
		uni = ele
		if "comment" in ele:
			uni = uni.split("comment")[0]
			if ":" in uni:
				uni = uni.split(":")[0]
			if "\xef" in uni:
				uni = uni.split("\xef")[0]
			uni = revCorrect(uni)

			if "Loyola" in uni or "UChicago" in uni or "Southwestern" in uni or "Rhodes" in uni:
				continue

			commentText = processCommentDict(path+ele,postIDs[uni])
			for postID in postIDs[uni]:
				if postID not in commentText.keys():
					commentText[postID] = []



			if uni in comments.keys():
				comments[uni].update(commentText)
			else:
				comments[uni]  = commentText

	return comments

def processCommentList(path = "USA/"):
	posts, allPosts, postIDs = processPostsForComments()
	comments = {}
	lst = os.listdir(path)
	for ele in lst:
		uni = ele
		if "comment" in ele:
			uni = uni.split("comment")[0]
			if ":" in uni:
				uni = uni.split(":")[0]
			if "\xef" in uni:
				uni = uni.split("\xef")[0]
			uni = revCorrect(uni)

			if "Loyola" in uni or "UChicago" in uni or "Southwestern" in uni or "Rhodes" in uni:
				continue

			commentText = processCommentText(path+ele,postIDs[uni])
			for postID in postIDs[uni]:
				if postID not in commentText.keys():
					commentText[postID] = []



			if uni in comments.keys():
				comments[uni].update(commentText)
			else:
				comments[uni]  = commentText

	return comments



def commentsSpecificPost(uni, postID):
	comments = processCommentsForQuestions()
	return comments[uni][postID]
		
	

def processUnisAll(path = "USA/", LIWCategory = None, ifPercent = False):
	postDict = {}
	commentDict = {}
	allPostDict = {}
	allCommentDict = {}
	percentPostDict = {}
	percentCommentDict = {}

	unis = []
	lst = os.listdir(path)

	for ele in lst:
		uni = ele

		if "post" in ele:
			
			uni = uni.split("post")[0]
			if ":" in uni:
				uni = uni.split(":")[0]
			if "\xef" in uni:
				uni = uni.split("\xef")[0]
		#uni = revCorrect(uni)
			uni = revCorrect(uni)
			if "Loyola" in uni or "UChicago" in uni or "Southwestern" in uni or "Rhodes" in uni:
				continue

			Posts, All = processTextAll("posts",path+ele, LIWCategory)

			if Posts and uni in postDict.keys():
				percentPostDict[uni] = simplePercent(len(Posts)+len(postDict[uni]), len(All)+len(allPostDict[uni]))
				postDict[uni] += Posts
				allPostDict[uni] += All
			elif Posts and uni not in postDict.keys():
				percentPostDict[uni] = simplePercent(len(Posts), len(All))
				postDict[uni] = Posts
				allPostDict[uni] = All

		elif "comment" in ele:
		
			uni = uni.split("comment")[0]

			if ":" in uni:
				uni = uni.split(":")[0]
			if "\xef" in uni:
				uni = uni.split("\xef")[0]
			uni = revCorrect(uni)
			if "Loyola" in uni or "UChicago" in uni or "Southwestern" in uni or "Rhodes" in uni:
				continue

			Comments, All  = processTextAll("comments",path+ele, LIWCategory)


			if uni in commentDict.keys():
				percentCommentDict[uni] = simplePercent(len(Comments)+len(commentDict[uni]), len(All)+len(allCommentDict[uni]))
				commentDict[uni] += Comments
				allCommentDict[uni] += All
			else:
				percentCommentDict[uni] = simplePercent(len(Comments), len(All))
				commentDict[uni] = Comments
				allCommentDict[uni] = All

	if ifPercent == False:
		return postDict, commentDict , allPostDict, allCommentDict
	else:
		return percentPostDict, percentCommentDict
