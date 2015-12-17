# -*- coding: utf-8 -*-
import re
import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
import iso8601
import operator
from processUnis import *

def codedPostIDs():
	lines = open("FCBQuestionsOnly.csv").readlines()
	allPostIDs = []
	postIDs = []
	count = 1
	uniDict = {}
	postDict = {}
	List = ["CommentsQuestionsPhase1.csv","CommentsQuestionsPhase2.csv","CommentsQuestionsPhase3.csv","CommentsQuestionsPhase4.csv","CommentsQuestionsPhase5.csv"]#,"CommentsQuestionsPhase6.csv"]
	for fileName in List:

		lines = open(fileName).readlines()
		lines = lines[1:]
		for line in lines:
			postIDs += [line.split("|")[1]]


def relevantIDs():
	lines = open("FCBQuestionsOnly.csv").readlines()
	lines = lines[1:]
	for line in lines[700:1580]:
		cols = line.split('|')
		uni = cols[3]
		postID = cols[2]
		message = cols[7]
		message = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', message)
		if "Rhodes" in uni or "Southwestern" in uni or  "University of California--Davis" in uni or "?" not in message:
			continue
		uniDict[postID] = uni
		postDict[postID] = message
		allPostIDs.append(postID)

postIDs = list(set(codedPostIDs()))
remaining = list(set(allPostIDs) -set(postIDs))

f = open("CommentsQuestionsPhase9.csv",'w')
f.write("university | postID | Post | Username | Time | CommentID | Comment\n")
for postid in remaining[:20]:
	
	try:
	
		comments = commentsSpecificPost(uniDict[postid], postid)
		
		if comments == None :
			print "continued"
			continue
		comments.sort(key=operator.itemgetter('isotime'))
		for comment in comments:
			comment['message'] = comment['message'].replace("|","")
			#print(uniDict[postid]+"|"+postid+"|"+postDict[postid] +"|"+comment['userName']+'|'+comment['time']+"|"+comment["commentID"]+"|"+comment['message'].strip()+"\n")
			f.write (uniDict[postid]+"|"+postid+"|"+postDict[postid] +"|"+comment['userName']+'|'+comment['time']+"|"+comment["commentID"]+"|"+comment['message'].strip()+"\n")
		print "here"		
	except:
	
		print "except"

#print len(remaining)



