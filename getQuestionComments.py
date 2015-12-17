# -*- coding: utf-8 -*-
import re
import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
import iso8601
import operator
from processUnis import *

def getQuestionComments():
	lines = open("FCBQuestionsOnly.csv").readlines()
	messages = []

	f = open("CommentsQuestionsPhase9.csv",'w')
	f.write("university | postID | Post | Username | Time | CommentID | Comment\n")
	#f.write("sdsd|sdsd|Sdsds|sdsd|sdsd|\n")
	g = open("Discarded.csv","w")
	g.write("uni|Post\n")
	#f = open("FCBRealQuestions.csv",'w')
	lines = lines[1:]
	count = 0
	#for line in lines[801:3779]:
	#for line in lines[700:]
	start = 1685
	stop = 3779
	index = start
	for line in lines[start:stop]:
		
		postID = line.split('|')[2]
		uni = line.split('|')[3]
		index += 1
		if "Rhodes" in uni or "Southwestern" in uni or "University of California--Davis" in uni:
			continue
		
		#urls = re.findall(r'https?://\S+', message)
		message = line.split('|')[7]
		message = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', message)
		
		if "?" in message:
			try:
				comments = commentsSpecificPost(uni, postID)
				if comments == None :
					print "except"
					continue
				comments.sort(key=operator.itemgetter('isotime'))
				for comment in comments:
					
					comment['message'] = comment['message'].replace("|","")
					f.write (uni+"|"+postID+"|"+message +"|"+comment['userName']+'|'+comment['time']+"|"+comment["commentID"]+"|"+comment['message'].strip()+"\n")
					print "here	"
					count += 1
				#f.write(message+"\n")
			except:
				print "except"
				g.write(uni+"|"+postID+"\n")
			#if len(messages)+2327 == 3000:
			#	return len(messages), count

	print "Coded Till", index
	'''
	f = open("SarahPhase2.csv",'a')
	#f.write("posts\n")
	lines = lines[1:]
	count = 0
	postID = {}
	unis = []
	for line in lines[700:3200]:
		#count += 1
		#if count <=700 or count>3200:
		#	continue
		uni = line.split('|')[3]
		unis += [uni]

	#unis = list(set(unis))
	#return unis

		#postID[uni] = line.split('|')[2]
		if "Rhodes" in uni or "Southwestern" in uni:
			continue

		message = line.split('|')[7]
		message = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', message)
		if "?" in message:
			messages += [message]
		
			if len(messages) ==13:
				print message
				break
			

	#len1 = len(messages)
	#len2 = len(lines[3000:3200])

	return (len(lines[700:3200]) - len(messages)), len(lines[700:3200])


#len1, len2 = getQuestions()
#print len1
#print len2
	'''



getQuestionComments()
