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

if len(sys.argv) <7:
	orig_stdout = sys.stdout
	fileName = ""
	for name in sys.argv[1:]:
		fileName += name
	fileName += ".dat"
	f = file(fileName,'w')
	sys.stdout = f
#sys.argv[1] -> posts/comments
#sys.argv[[0]*[0]*[[]]*2] -> religion/size/population etc
#sys.argv[3] -> timeLines / LIWC
#sys.argv[4] -> only for LIWC ()

g = open("Exceptions.error","w")

if sys.argv[1] == "posts":
	print "Need to be cautious while making timeline analysis of posts (The time is that if when they are posted by moderators)"
LIWCategories = ["sex","religious","death","sad","anger", "swear", "social", "family", "friends", "humans", "anxiety", "body", "health", "ingest", "time", "work", "achievment", "leisure", "home", "money"]

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
timeSlots = {"earlyMorning" : "6am-9am", "lateMorning": "9am-noon", "earlyAfternoon":"noon-3pm", "lateAfternoon" :"3pm-6pm", "evening" :"6pm-9pm", "night" :"9pm-midnight", "lateNight" :"midnight- 3 am", "beforeSunRise" :"3 am - 6am" }
interval = {"earlyMorning" : 1, "lateMorning": 1, "earlyAfternoon":1, "lateAfternoon" :1, "evening" :1, "night" :1, "lateNight" :1, "beforeSunRise" :1 }
#TODW = {"earlyMorningMonday", "lateMorningMonday": 1, "earlyAfternoonMonday":1, "lateAfternoon" :1, "evening" :1, "night" :1, "lateNight" :1, "beforeSunRise" :1 }
religious = {0: "nonReligious", 1: "Religious", 2: "religion" }
politics = {0: "Democrats", 1: "Republican", 2: "political color"}
schoolType = {0: "private", 1: "public", 2: "tuition"}
schoolSize = {0: "Liberal Arts", 1 : "Big School", 2: "size of School"}
timesOfDay = ["earlyMorning" , "lateMorning", "earlyAfternoon", "lateAfternoon", "evening", "night", "lateNight", "beforeSunRise" ]
print "Note: We are only extracting posts which have questions"
#print "This is for all boards together..This is for "+sys.argv[1]+" only"

print

if len(sys.argv) >4 and sys.argv[3] == "LIWC":
	LIWCategory = sys.argv[4]
	timeCategory = sys.argv[5]
else:
	LIWCategory = None
	timeCategory = sys.argv[3]

posts, comments, allPosts, allComments = processUnisAll("USA/", LIWCategory)


if len(sys.argv) <= 2:
	feature = "isReligious"
	
else:
	feature = sys.argv[2]
	#category = mapUnis(cleanUniList(), sys.argv[[0]*[0]*[[]]*2])
	#print "**************", category, "**************"

category = mapUnis(cleanUniList(),feature)

if feature == "politics":
	print "Remember that schools and states being R/D may be different. Also, there are very few Republican schools in samples in comparison (Ofcourse, we have averaged them but typically a comparable number of schools give more trusted results)"
	print
elif feature == "tuition":
	print "Warning: We have considered public schools as ones which have different instate and out of state tuitions. Although, more or less consistent, may not be entirely correct"
	print 
print 

#if len(sys.argv) >[0]*[0]*[[]]*2 :
#	category =  mapUnis(cleanUniList(), sys.argv[[0]*[0]*[[]]*2])


DOW0 = [] #day of week
DOW1 = []
allDOW0 = [] #day of week
allDOW1 = []

HOD0 = [] #hr of day
HOD1 = []
allHOD0 = [] #hr of day
allHOD1 = []

MOY0 = [] #month (of year)
MOY1 = []
allMOY0 = [] #month (of year)
allMOY1 = []

TOD0 = [] # different time during the day
TOD1 = []
allTOD0 = [] # different time during the day
allTOD1 = []

TOW0 = []
TOW1 = []
allTOW0 = []
allTOW1 = []

TODW0 =[]
TODW1 = []
allTODW0 =[]
allTODW1 = []

numTexts0 = numTexts1 =  0
#print numPosts.keys()
#print "******************************************"
if sys.argv[1] == "posts":
	for uni in posts.keys():

		if category[uni] == 0:
			#numTexts0 += numPosts[uni]
			DOW0, HOD0, MOY0, TOD0, TOW0, TODW0 = getTime(posts,uni,DOW0,HOD0,MOY0,TOD0,TOW0,TODW0)
			allDOW0, allHOD0, allMOY0, allTOD0, allTOW0, allTODW0 = getTime(allPosts,uni,allDOW0,allHOD0,allMOY0,allTOD0,allTOW0,allTODW0)
		elif category[uni] == 1:
			#numTexts1 += numPosts[uni]
			DOW1, HOD1, MOY1, TOD1, TOW1, TODW1 = getTime(posts,uni,DOW1,HOD1,MOY1,TOD1,TOW1,TODW1)
			allDOW1, allHOD1, allMOY1, allTOD1, allTOW1, allTODW1 = getTime(allPosts,uni,allDOW1,allHOD1,allMOY1,allTOD1,allTOW1,allTODW1)
	
elif sys.argv[1] == "comments":
	for uni in comments.keys():
		
		if category[uni] == 0:
			#numTexts0 += numComments[uni]
			DOW0, HOD0, MOY0, TOD0, TOW0, TODW0 = getTime(posts,uni,DOW0,HOD0,MOY0,TOD0,TOW0,TODW0)
			allDOW0, allHOD0, allMOY0, allTOD0, allTOW0, allTODW0 = getTime(allPosts,uni,allDOW0,allHOD0,allMOY0,allTOD0,allTOW0,allTODW0)
		
		elif category[uni] == 1:
			#numTexts1 += numComments[uni]
			DOW1, HOD1, MOY1, TOD1, TOW1, TODW1 = getTime(posts,uni,DOW1,HOD1,MOY1,TOD1,TOW1,TODW1) 
			allDOW1, allHOD1, allMOY1, allTOD1, allTOW1, allTODW1 = getTime(allPosts,uni,allDOW1,allHOD1,allMOY1,allTOD1,allTOW1,allTODW1)
		
#if sys.argv[5] == "ignore" and sys.argv[3] == "LIWC":
#	barchart4(sys.argv[1],sys.argv[4],cat0, cat1, week, categoryDict[0], categoryDict[1], "day", categoryDict[2])
#	sys.exit()
# This is comparison of 

DOW0 = Counter(DOW0)
DOW1 = Counter(DOW1)
allDOW0 = Counter(allDOW0)
allDOW1 = Counter(allDOW1)

HOD0 = Counter(HOD0)
HOD1 = Counter(HOD1)
allHOD0 = Counter(allHOD0)
allHOD1 = Counter(allHOD1)

MOY0 = Counter(MOY0)
MOY1 = Counter(MOY1)
allMOY0 = Counter(allMOY0)
allMOY1 = Counter(allMOY1)

TOD0 = Counter(TOD0)
TOD1 = Counter(TOD1)
allTOD0 = Counter(allTOD0)
allTOD1 = Counter(allTOD1)

TOW0 = Counter(TOW0)
TOW1 = Counter(TOW1)
allTOW0 = Counter(allTOW0)
allTOW1 = Counter(allTOW1)

TODW0 = Counter(TODW0)
TODW1 = Counter(TODW1)
allTODW0 = Counter(allTODW0)
allTODW1 = Counter(allTODW1)
	
#mapping
categoryDict = {}
if feature == "isReligious":
	categoryDict = religious
elif feature == "size":
	categoryDict = schoolSize
elif feature == "tuition":
	categoryDict = schoolType
elif feature == "politics":
	categoryDict = politics

print "The % refers to number of posts in each category which appeared during the time Slot"

print 
if len(sys.argv) > 3:

	print timeCategory
	print "++++++++++++++++++++++++++++"
	cat1 = {}
	cat0 = {}
	#if timeCategory == "ignore":

	if timeCategory == "day":
		for day in week:

			cat0[day] = relPercent(DOW0,allDOW0, day, numTexts0, categoryDict[0])
			cat1[day] = relPercent(DOW1,allDOW1, day, numTexts1, categoryDict[1])
			#print str(day)+":-"+ categoryDict[0] + ": " + relPercent(DOW0,allDOW0, day, numTexts0, categoryDict[0]) + "," + categoryDict[1] + ": " + relPercent(DOW1,allDOW1, day, numTexts1, categoryDict[1])
			print str(day)+":-"+ categoryDict[0] + ": " + strRelPercent(cat0[day])+ "," + categoryDict[1] + ": " + strRelPercent(cat1[day])
			print
		barchart(sys.argv[1],sys.argv[4],cat0, cat1, week, categoryDict[0], categoryDict[1], "day", categoryDict[2])

	elif timeCategory == "month":
		for month in year: #MOY and month
			cat0[month] = relPercent(MOY0,allMOY0, month, numTexts0, categoryDict[0])
			cat1[month] = relPercent(MOY1,allMOY1, month, numTexts1, categoryDict[1])
			print str(month)+":-"+ categoryDict[0] + ": " + strRelPercent(cat0[month]) + "," + categoryDict[1] + ": " + strRelPercent(cat1[month])
			print
		barchart(sys.argv[1],sys.argv[4],cat0, cat1,year, categoryDict[0], categoryDict[1], "month", categoryDict[2])
	elif timeCategory == "time":
		for time, slotName in sorted(timeSlots.items()):
			cat0[time] = relPercent(TOD0,allTOD0, time, numTexts0, categoryDict[0])
			cat1[time] = relPercent(TOD1,allTOD1, time, numTexts1, categoryDict[1])
			print str(time)+":-"+ categoryDict[0] + ": " + strRelPercent(cat0[time])+ "," + categoryDict[1] + ": " + strRelPercent(cat1[time])
			print
		barchart(sys.argv[1],sys.argv[4],cat0, cat1, timesOfDay, categoryDict[0], categoryDict[1], "timeOfDay", categoryDict[2])

	elif timeCategory == "timeweek":
		timeOfWeek = []
		for day in week:
			for time, slotName in sorted(timeSlots.items()):
				timeweek =  str(time) + str(day)
				timeOfWeek += [timeweek]
				cat0[timeweek] = relPercent(TODW0,allTODW0, timeweek, numTexts0, categoryDict[0])
				cat1[timeweek] = relPercent(TODW1,allTODW1, timeweek, numTexts1, categoryDict[1])
				print str(timeweek)+"("+slotName+")"+":-"+ categoryDict[0] +  ": " + strRelPercent(cat0[timeweek]) + "," + categoryDict[1] + ": " + strRelPercent(cat1[timeweek])
				print
		barchartWide(sys.argv[1],sys.argv[4],cat0, cat1, timeOfWeek, categoryDict[0], categoryDict[1], "timeweek", categoryDict[2])
	elif timeCategory == "hour":
		for hour in range(24):
			cat0[hour] = relPercent(HOD0,allHOD0, hour, numTexts0, categoryDict[0])
			cat1[hour] = relPercent(HOD1,allHOD1, hour, numTexts1, categoryDict[1])
			print str(hour)+":-"+ categoryDict[0] + ": " + strRelPercent(cat0[hour]) + "," + categoryDict[1] + ": " + strRelPercent(cat1[hour])
			print
		barchart(sys.argv[1],sys.argv[4],cat0, cat1,range(24), categoryDict[0], categoryDict[1], "hour", categoryDict[2])	
	elif timeCategory == "week":
		weekdayend = ["weekday", "weekend"]
		for cat in weekdayend:
			cat0[cat] = relPercent(TOW0,allTOW0, cat, numTexts0, categoryDict[0])
			cat1[cat] = relPercent(TOW1,allTOW1, cat, numTexts1, categoryDict[1])
			print str(cat)+":-"+ categoryDict[0] + ": " + strRelPercent(cat0[cat]) + "," + categoryDict[1] + ": " + strRelPercent(cat1[cat])
			print
		barchart(sys.argv[1],sys.argv[4],cat0, cat1,weekdayend, categoryDict[0], categoryDict[1], "week", categoryDict[2])
	else:


		for day in week:

			cat0[day] = relPercent(DOW0,allDOW0, day, numTexts0, categoryDict[0])
			cat1[day] = relPercent(DOW1,allDOW1, day, numTexts1, categoryDict[1])
			#print str(day)+":-"+ categoryDict[0] + ": " + relPercent(DOW0,allDOW0, day, numTexts0, categoryDict[0]) + "," + categoryDict[1] + ": " + relPercent(DOW1,allDOW1, day, numTexts1, categoryDict[1])
			print str(day)+":-"+ categoryDict[0] + ": " + strRelPercent(cat0[day])+ "," + categoryDict[1] + ": " + strRelPercent(cat1[day])
			print
		barchart(sys.argv[1],sys.argv[4],cat0, cat1, week, categoryDict[0], categoryDict[1], "day", categoryDict[2])

		cat1 = {}
		cat0 = {}

		for month in year: #MOY and month
			cat0[month] = relPercent(MOY0,allMOY0, month, numTexts0, categoryDict[0])
			cat1[month] = relPercent(MOY1,allMOY1, month, numTexts1, categoryDict[1])
			print str(month)+":-"+ categoryDict[0] + ": " + strRelPercent(cat0[month]) + "," + categoryDict[1] + ": " + strRelPercent(cat1[month])
			print
		barchart(sys.argv[1],sys.argv[4],cat0, cat1,year, categoryDict[0], categoryDict[1], "month", categoryDict[2])

		cat1 = {}
		cat0 = {}

		for time, slotName in sorted(timeSlots.items()):
			cat0[time] = relPercent(TOD0,allTOD0, time, numTexts0, categoryDict[0])
			cat1[time] = relPercent(TOD1,allTOD1, time, numTexts1, categoryDict[1])
			print str(time)+":-"+ categoryDict[0] + ": " + strRelPercent(cat0[time])+ "," + categoryDict[1] + ": " + strRelPercent(cat1[time])
			print
		barchart(sys.argv[1],sys.argv[4],cat0, cat1, timesOfDay, categoryDict[0], categoryDict[1], "timeOfDay", categoryDict[2])

		cat1 = {}
		cat0 = {}

		timeOfWeek = []
		for day in week:
			for time, slotName in sorted(timeSlots.items()):
				timeweek =  str(time) + str(day)
				timeOfWeek += [timeweek]
				cat0[timeweek] = relPercent(TODW0,allTODW0, timeweek, numTexts0, categoryDict[0])
				cat1[timeweek] = relPercent(TODW1,allTODW1, timeweek, numTexts1, categoryDict[1])
				print str(timeweek)+"("+slotName+")"+":-"+ categoryDict[0] +  ": " + strRelPercent(cat0[timeweek]) + "," + categoryDict[1] + ": " + strRelPercent(cat1[timeweek])
				print
		barchartWide(sys.argv[1],sys.argv[4],cat0, cat1, timeOfWeek, categoryDict[0], categoryDict[1], "timeweek", categoryDict[2])
	
		cat1 = {}
		cat0 = {}

		for hour in range(24):
			cat0[hour] = relPercent(HOD0,allHOD0, hour, numTexts0, categoryDict[0])
			cat1[hour] = relPercent(HOD1,allHOD1, hour, numTexts1, categoryDict[1])
			print str(hour)+":-"+ categoryDict[0] + ": " + strRelPercent(cat0[hour]) + "," + categoryDict[1] + ": " + strRelPercent(cat1[hour])
			print
		barchart(sys.argv[1],sys.argv[4],cat0, cat1,range(24), categoryDict[0], categoryDict[1], "hour", categoryDict[2])	

		cat1 = {}
		cat0 = {}

		weekdayend = ["weekday", "weekend"]
		for cat in weekdayend:
			cat0[cat] = relPercent(TOW0,allTOW0, cat, numTexts0, categoryDict[0])
			cat1[cat] = relPercent(TOW1,allTOW1, cat, numTexts1, categoryDict[1])
			print str(cat)+":-"+ categoryDict[0] + ": " + strRelPercent(cat0[cat]) + "," + categoryDict[1] + ": " + strRelPercent(cat1[cat])
			print
		barchart(sys.argv[1],sys.argv[4],cat0, cat1,weekdayend, categoryDict[0], categoryDict[1], "week", categoryDict[2])


else:
	print "                    Category is Day oF Week"
	print "                    +++++++++++++++++++++++"
	print "S.D. is "+str(scipy.std(DOW.values()))
	print
	print "Mean is "+str(scipy.mean(DOW.values()))
	print "Median is "+str(scipy.median(DOW.values()))
	print "Mode is "+str(mode(DOW.values())[0][0])
	print "======================================="
	for day in week:
		print str(day)+":"+ str(DOW[day])

	print 
	print
	print

	print "                    Category is Hour of Day"
	print "                    +++++++++++++++++++++++"
	print "S.D. is "+str(scipy.std(HOD.values()))
	print
	print "Mean is "+str(scipy.mean(HOD.values()))
	print "Median is "+str(scipy.median(HOD.values()))
	print "Mode is "+str(mode(HOD.values())[0][0])
	print "======================================="
	for hour in range(24):
		print "hour " + str(hour)+" : "+str(HOD[hour])

	print 
	print
	print

	print "                    Category is Time of Day"
	print "                    +++++++++++++++++++++++"
	print "S.D. is "+str(scipy.std(TOD.values()))
	print
	print "Mean is "+str(scipy.mean(TOD.values()))
	print "Median is "+str(scipy.median(TOD.values()))
	print "Mode is "+str(mode(TOD.values())[0][0])
	print "======================================="
	for hour in sorted(timeSlots):
		print str(hour)+" "+str(timeSlots[hour])+": total posts "+str(TOD[hour])+": per hour is "+str(TOD[hour]/interval[hour])

	print 
	print
	print

	print "                    Category is Month of Year"
	print "                    +++++++++++++++++++++++"
	print "S.D. is "+str(scipy.std(MOY.values()))
	print
	print "Mean is "+str(scipy.mean(MOY.values()))
	print "Median is "+str(scipy.median(MOY.values()))
	print "Mode is "+str(mode(MOY.values())[0][0])
	print "======================================="
	for month in year:
		print str(month)+":"+str(MOY[month])

	print 
	print
	print
if len(sys.argv) <7:
	sys.stdout = orig_stdout
	f.close()
