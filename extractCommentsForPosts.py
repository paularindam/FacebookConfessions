from myTime import myTime
from collections import Counter
from processUnis import *
from myTime import *

import scipy
from scipy import stats
from scipy.stats import mode

from mapUnis import *
from extractPercent import *
from barchart import *

import sys

'''

b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow

k: black
'''

LIWCategories = ["sex","religious","death","sad","anger", "swear", "social", "family", "friends", "humans", "anxiety", "body", "health", "ingest", "time", "work", "achievment", "leisure", "home", "money"]
impLIWCategories = ["sex","religious","death","sad","anger", "anxiety", "health", "money"]

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
timeSlots = {"earlyMorning" : "6am-9am", "lateMorning": "9am-noon", "earlyAfternoon":"noon-3pm", "lateAfternoon" :"3pm-6pm", "evening" :"6pm-9pm", "night" :"9pm-midnight", "lateNight" :"midnight- 3 am", "beforeSunRise" :"3 am - 6am" }
interval = {"earlyMorning" : 1, "lateMorning": 1, "earlyAfternoon":1, "lateAfternoon" :1, "evening" :1, "night" :1, "lateNight" :1, "beforeSunRise" :1 }
#TODW = {"earlyMorningMonday", "lateMorningMonday": 1, "earlyAfternoonMonday":1, "lateAfternoon" :1, "evening" :1, "night" :1, "lateNight" :1, "beforeSunRise" :1 }

religious = {0: "nonReligious", 1: "Religious", 2: "religion" }
politics = {0: "Democrats", 1: "Republican", 2: "political color"}
schoolType = {0: "private", 1: "public", 2: "tuition"}
schoolSize = {0: "Liberal Arts", 1 : "Big School", 2: "size of School"}

category = {"isReligious":religious, "politics":politics, "tuition" :schoolType, "size":schoolSize}


timesOfDay = ["earlyMorning" , "lateMorning", "earlyAfternoon", "lateAfternoon", "evening", "night", "lateNight", "beforeSunRise" ]

def extractCommentsForPosts(postIDs, comments, category, feature):


	uniList = cleanUniList()

	count1 = count0 = 0
	countComments0 = {}
	countComments1 = {}
	for uni in postIDs.keys():
	
		for comment in comments[uni]:
			if comment["postID"] in postIDs[uni]:
				if mapUni(uni, uniList, feature) == 1:
					count1 += 1 #The comments which have posts with sex
					for LIWCategory in impLIWCategories:
						if processLIWC(comment["message"], LIWCategory) == True:
							if LIWCategory in countComments1.keys():
								countComments1[LIWCategory] += 1
							else:
								countComments1[LIWCategory] = 1
				elif mapUni(uni, uniList, feature) == 0:
					count0 += 1 #The comments which have posts with sex
					for LIWCategory in impLIWCategories:
						if processLIWC(comment["message"], LIWCategory) == True:
							if LIWCategory in countComments0.keys():
								countComments0[LIWCategory] += 1
							else:
								countComments0[LIWCategory] = 1

	print "************************Total******************"
	print count0
	print count1
	
	for LIWCategory in impLIWCategories:
		if LIWCategory in countComments0.keys():
			
			countComments0[LIWCategory] = simplePercent(countComments0[LIWCategory], count0)
		else:
			countComments0[LIWCategory] = 0
	for LIWCategory in impLIWCategories:
		if LIWCategory in countComments1.keys():	
			countComments1[LIWCategory] = simplePercent(countComments1[LIWCategory], count1)
		else:
			countComments1[LIWCategory] = 0
	'''
		if LIWCategory in catComments1.keys():
			#print LIWCategory
			#print "========================================"
			#print len(catComments[LIWCategory])
			countComments[LIWCategory] = simplePercent(countComments0, count0)
			#print
		else:
			#print LIWCategory
			#print "========================================"
			#print 0
			countComments[LIWCategory] =  simplePercent(0, count)
			#print
	'''

	return countComments0,countComments1
		
def extractAllCategories(LIWCategory, feature):

	#LIWCategory = impLIWCategories[0]
	posts, allPosts,postIDs = processPosts(LIWCategory)
	comments, allComments = processCommentsAll()
	#feature = category.keys()[0]
	#for feature in category.keys():

		#barchart("comment", "anger", cat0, cat1, keys, "religious", "Not religious", )
	cat0, cat1 = extractCommentsForPosts(postIDs, comments, LIWCategory, feature)
	barchart("byComments", LIWCategory, cat0, cat1, impLIWCategories, category[feature][0], category[feature][1], feature)
	print "********************"+feature+"for "+LIWCategory+"********"
	print
	print

extractAllCategories(sys.argv[1], sys.argv[2])
