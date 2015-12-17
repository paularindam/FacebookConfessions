from processUnis import *
from mapUnis import *
from myTime import *
from extractTimePercentages import *

posts, comments, numPosts, numComments, allPosts, allComments = processUnisAll("USA/", "anxiety")
category = mapUnis(cleanUniList(), "size")
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
numTexts0 = numTexts1 =  0
DOW0 = [] #day of week
DOW1 = []
allDOW0 = [] #hr of day
allDOW1 = []

for uni in comments.keys():
		
		
		for comment in comments[uni]:
			time = myTime(comment["time"],uni)
			if category[uni] == 0:
				DOW0 += [time["DOW"]]
				

			elif category[uni] == 1:
				DOW1 += [time["DOW"]]
		
		for comment in allComments[uni]:
			time = myTime(comment["time"],uni)
			if category[uni] == 0:
				allDOW0 += [time["DOW"]]
				

			elif category[uni] == 1:
				allDOW1 += [time["DOW"]]

DOW0 = Counter(DOW0)
DOW1 = Counter(DOW1)
allDOW0 = Counter(allDOW0)
allDOW1 = Counter(allDOW1)
categoryDict = {0: "Liberal Arts", 1 : "Big School"}
for day in week: #DOW and day
	print str(day)+":-"+ categoryDict[0] + ": " + relPercent(DOW0,allDOW0, day, numTexts0,categoryDict[0]) + "," + categoryDict[1] + ": " + relPercent(DOW1,allDOW1, day, numTexts1, categoryDict[1])
	print
#Stuff from processUnis
##if "post" in:
			
		#	postDict[uni], numQposts[uni] = processText("posts",path+ele, LIWCategory)
		#elif "comment" in uni:
		#	commentDict[uni], numQcomments[uni]  = processText("comments",path+ele, LIWCategory)
			#uni = ele.split("comment")[0]
			#postDict[uni], numQposts[uni] = processPosts(path+ele, LIWCategory)
			#postDict[uni], numQposts[uni] = processText("posts",path+ele, LIWCategory)
		
			#postDict[uni], numQposts[uni] = processPosts(path+ele, LIWCategory)
			#commentDict[uni], numQcomments[uni]  = processText("comments",path+ele, LIWCategory)
'''
def processPosts(path, LIWCategory, numWords = 1):
	posts = open(path).readlines()[1:]
	allPosts = []
	count = 0
	for post in posts:
		
		elements = post.split("|")
		
		if "?" not in elements[2]: #"message" -> elements[2]
			continue
		count += 1

		if LIWCategory != None:	
			inCategory = processLIWC(elements[2], LIWCategory, numWords)
		
		if LIWCategory == None or inCategory == True:
			dct = {}
			dct["postID"] = elements[0]
			dct["time"] = elements[1] 
			dct["message"] = elements[2]
			dct["numLikes"] = elements[3]
			dct["numComments"] = elements[4]
			dct["type"] = elements[5]
			
			allPosts.append(dct)

	#print count
	#print "*************************"
	return allPosts, count

def processComments(path, LIWCategory, numWords = 1):
	comments = open(path).readlines()[1:]
	allComments = []
	count = 0
	#inCategory = False
	for comment in comments:

		elements = comment.split("|")
		if "?" not in elements[6]: #"message" -> elements[6]
			continue
		count += 1
		if LIWCategory != None:	
			inCategory = processLIWC(elements[6], LIWCategory, numWords)

		if LIWCategory ==None or inCategory == True:
			dct = {}
			dct["postID"] = elements[0]
			dct["commentID"] = elements[1] 
			dct["userName"] = elements[2]
			dct["userID"] = elements[3]
			dct["time"] = elements[4]
			dct["likeCount"] = elements[5]
			dct["message"] = elements[6]
			
			allComments.append(dct)

	#print count
	#print "*************************"
	return allComments, count
'''
