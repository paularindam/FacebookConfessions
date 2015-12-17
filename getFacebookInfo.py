import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
import json
import facebook
from collections import Counter
from processUnis import *


allComments = processComments()
uniqueUsers = {}
unScapedUsers = {}
genderCount = {}
others = {}
f = open("Others2.csv","w")
f.write("university | fbDetails \n")
for uni in allComments.keys():
	uniqueUsers[uni] = []
	genderCount[uni] = []
	unScapedUsers[uni] = []

graph = facebook.GraphAPI(sys.argv[1])

try:
	me = graph.get_object('me')
except:
	me = None

if not me:
	print "Get new Access Token"
	sys.exit()

x = []
for uni in allComments.keys():
	comments = allComments[uni]
	for postID in comments:
		try:
			commentsPost = comments[postID]

			if commentsPost == None:
				continue
			for comment in commentsPost:
				uniqueUsers[uni] += [comment['userID']]
				print "here"
		except:
			x += [uni]
		
for uni in uniqueUsers.keys():
	uniqueUsers[uni] = list(set(uniqueUsers[uni]))

with open('uniqueUsers.json', 'wb') as fp:
	json.dump(uniqueUsers, fp)
print x
for uni in uniqueUsers.keys():
	for userID in uniqueUsers[uni]:
		try:
			fbDetails = graph.get_object(userID)
			if 'first_name' in fbDetails.keys() or 'last_name' in fbDetails.keys():
				totalPeople += 1
				if "gender" in fbDetails.keys():
					genderCount[uni] += [fbDetails["gender"]] #people with gender mentioned
				else:
					genderCount[uni] += ["unmentioned"]		
			else:
				others[uni] += [fbDetails]
				with open("Others2/"+str(userid)+'.json', 'wb') as fp:
					json.dump(fbDetails, fp)
		except:
			unScapedUsers[uni] += [userID]
	print "processed......."

with open('genderCount2.json', 'wb') as fp:
	json.dump(genderCount, fp)
with open('others2.json', 'wb') as fp:
	json.dump(others, fp)
with open('unscraped2.json','wb') as fp:
	json.dump(unScapedUsers, fp)


#with open(str(userid)+'.json', 'rb') as fp:

male = female = total = notScraped = 0
TotalKeys = []
for uni in genderCount.keys():
	genderDict = Counter(genderCount[uni])
	TotalKeys += genderDict.keys()
	print genderDict['male']
	male += genderDict['male']
	female += genderDict['female']
	notScraped += len(unScapedUsers[uni])

TotalKeys = list(set(TotalKeys))
print "Breakup of gender :- Male:" + str(male)+" Female: "+str(female)
print "Gender keys : ",len(TotalKeys)
print "Number of unscraped : "+str(notScraped)

		
