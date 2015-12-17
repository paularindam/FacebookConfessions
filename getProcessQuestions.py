# -*- coding: utf-8 -*-
import re
def getProcessQuestions():
	#f.write("posts\n")
	lines = open("FCBQuestionsOnly.csv").readlines()[1:]
	count = 0
	postID = {}
	idsmessages = []
	for line in lines[3200:]:
		
		cols = line.split('|')
		#message,uni,postid,likes, comments = cols[7],cols[3],cols[2],cols[4],cols[5]
		message,uni = cols[7],cols[3]

		message = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', message)
		if "Rhodes" in uni or "Southwestern" in uni or "?" not in message:
			continue
		count += 1
		idsmessages += [cols]
		if count == 673:
			return idsmessages

	#return (len(lines[700:3200]) - len(messages)), len(lines[700:3200])


#getQuestions()
#print len1
#print len2