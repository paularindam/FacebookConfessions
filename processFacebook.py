from processUnis import *
import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
import facebook
import pickle
from collections import Counter

def getUserIDs():

	allComments = processComment()

	commentIDs = []
	lines = open("StatsForCommentsWithoutUserID.csv").readlines()[1:]
	for line in lines:
		commentIDs += [line.split("|")[0]]

	codedCommentIDict, restCommentIDict = {},{}
	for uni in allComments.keys():
		for commentID in allComments[uni].keys():
				if commentID in commentIDs:
					codedCommentIDict[commentID] = allComments[uni][commentID]['userID']
				else:
					restCommentIDict[commentID] = allComments[uni][commentID]['userID']

	return codedCommentIDict, restCommentIDict



def assignUserIDs(commentIDict)	:
	
	f = open("StatsForComments.csv","w")
	f.write('commentID|postID|uni|post|userID| username| date|time|comment|wordCount|numLikes|isViable|isMean|isProsocial|Taboo|Stigma|isCoded\n')
	lines = open("StatsForCommentsWithoutUserID.csv").readlines()[1:]
	for line in lines:
		first = line.rsplit("|",12)[0]
		second = line.split("|",4)[-1]
		userID = commentIDict[line.split("|")[0]]
		newLine = first +"|"+userID+"|"+second
		f.write(newLine)

#commentIDict = getUserIDs()
#assignUserIDs()
def assignGenderCodedComments():
	graph = facebook.GraphAPI("CAAGljQ0ymaQBAFRbTseLLCtDwwC1HZCvcCDcHZA120WFB58F02QqCDSpFRPsfMrChUPiZCTaHOQrWvJhWGhpZApY4JITwVPZAb7rrrNfba9ZBY0PJfDfpkfApLlZBdPSyWnGQO4HfMmrDBfdGB4sUHXxxm7qKzrZAksUduARzLE41PSvKFNIaYxqTB4DDtF6tFzNHqAJmSMyYHZAZBeaLAgbxvXYXWtBKwdTAZD")
	lines = open("StatsForComments.csv").readlines()[1:]
	userIDs = []
	genderDict = {}
	simpleKeys = [u'username', u'first_name', u'last_name', u'link', u'name', u'locale', u'gender', u'id', u'updated_time']
	detailedEntries = []
	for line in lines:
		userIDs += [line.split("|")[4]]

	userIDs = list(set(userIDs))
	others = []
	countUS = countUM = countNP = 0
	for userID in userIDs:
		try:
			fbDetails = graph.get_object(userID)
			if 'first_name' in fbDetails.keys() or 'last_name' in fbDetails.keys():
				#I.e. if its a person
				if "gender" in fbDetails.keys():
					genderDict[userID] = fbDetails["gender"]
					keys = list(set(fbDetails.keys()) - set(simpleKeys))
					if len(keys)>0:
						detailedEntries += [fbDetails]

				else:
					countUM += 1
					genderDict[userID] = "unmentioned"
			else:
				countNP += 1
				others += [fbDetails]
				genderDict[userID] = "notPerson"


		except:
			countUS += 1
			genderDict[userID] = "unScraped"

	return genderDict, countUS, countUM, countNP, others, detailedEntries


'''
[{u'category': u'Community', u'username': u'OLCCgull', u'about': u'Defender of justice at Lewis & Clark College, protecting students everywhere from the dangers of underage alcohol consumption.', u'talking_about_count': 1, u'name': u'OLCC-gull', u'has_added_app': False, u'can_post': True, u'link': u'https://www.facebook.com/OLCCgull', u'likes': 137, u'parking': {u'street': 0, u'lot': 0, u'valet': 0}, u'is_community_page': False, u'were_here_count': 0, u'checkins': 0, u'id': u'214115452099605', u'is_published': True}, {u'category': u'Community', u'username': u'TexasAMConfessions20', u'about': u'Post yours 100% ANONYMOUSLY. Forever Free: \nhttps://docs.google.com/forms/d/13EViaeAbmGoHprAt1vSH46SDBfxPz4rISpttBin62NE/viewform', u'talking_about_count': 1805, u'description': u'This page, run for and by students, is not officially affiliated with Texas A&M University or the Texas A&M System. \n\nFans of the page may post confessions anonymously and for free without charge. Likewise students may view, add or make comments, and engage in dialogue freely and without charge. \n\nThe page reserves the right to remove or block any content which violates the terms and conditions of Facebook or at request of poster.', u'has_added_app': False, u'can_post': True, u'cover': {u'source': u'https://scontent-a.xx.fbcdn.net/hphotos-xfp1/t31.0-8/s720x720/1501434_674492252589934_518311603_o.jpg', u'cover_id': 674492252589934, u'offset_x': 0, u'offset_y': 50}, u'name': u'Ag Confessions', u'website': u'https://docs.google.com/forms/d/13EViaeAbmGoHprAt1vSH46SDBfxPz4rISpttBin62NE/viewform', u'link': u'https://www.facebook.com/TexasAMConfessions20', u'likes': 10276, u'parking': {u'street': 0, u'lot': 0, u'valet': 0}, u'is_community_page': False, u'were_here_count': 0, u'checkins': 0, u'id': u'527813577257803', u'is_published': True}, {u'category': u'Community', u'username': u'peppconfessions', u'about': u'Even a small private Christian school has its secrets... Share your confessions here at http://tiny.cc/7lc3cx', u'talking_about_count': 312, u'description': u'A page for the Pepperdine University community to post their confessions anonymously.\n\nThis page is in no way affiliated with Pepperdine University or its staff.', u'has_added_app': False, u'can_post': False, u'cover': {u'source': u'https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-xfp1/v/t1.0-9/p180x540/994045_1426044207612466_1153793135_n.jpg?oh=1167e935f72c7003deb72570e6d3e183&oe=549BE671&__gda__=1419406570_71a4109da6e755203f3c519cee6b0b6c', u'cover_id': 1426044207612466, u'offset_x': 0, u'offset_y': 55}, u'name': u'Pepperdine University Confessions', u'link': u'https://www.facebook.com/peppconfessions', u'likes': 1083, u'parking': {u'street': 0, u'lot': 0, u'valet': 0}, u'is_community_page': False, u'were_here_count': 0, u'checkins': 0, u'id': u'1426040870946133', u'is_published': True}, {u'category': u'Community', u'username': u'LCConfessions', u'about': u"C'mon, Lewis & Clark, we all have secrets. Let 'em out here, anonymously. It's cathartic! Click this link to fill out the form: http://tinyurl.com/LCconfessions", u'talking_about_count': 25, u'description': u"A disclaimer:\nThis page is in no way associated with Lewis & Clark College's faculty, administrators, and staff; it is student-run and posts student submissions. Its posts are not intended to make objective statements about the college, and do not necessarily reflect the views of the page's administrator or of the entire student body. This is just our sounding board. \n\nLONG STORY SHORT: Don't take this page too seriously.\n\nAnother disclaimer:\nLewis & Clark is no ordinary school, so this is no ordinary confessions page. We do not post content that personally identifies anyone (even in a joking or inoffensive manner), and we don't post anything mean-spirited or that insults a particular social group on campus. This is a safe space.\nIf you really want your secret posted, try to make it personal--a secret that is yours to give out. Bonus points if it's hilarious. Secrets about something you saw are also fine, but remember to keep identifying details vague.\nWe still don't post all the good confessions we get, just for the sake of not spamming everyone's newsfeed. But rest assured, we read them, and we love them.\n\nHappy confessing!\n\n\nEmail the admin: lewisandclarkconfessions@gmail.com", u'has_added_app': False, u'can_post': True, u'cover': {u'source': u'https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xfp1/t31.0-8/s720x720/903074_155770951255982_235011593_o.jpg', u'cover_id': 155770951255982, u'offset_x': 0, u'offset_y': 59}, u'name': u'Lewis & Clark Confessions', u'link': u'https://www.facebook.com/LCConfessions', u'likes': 1306, u'parking': {u'street': 0, u'lot': 0, u'valet': 0}, u'is_community_page': False, u'were_here_count': 0, u'checkins': 0, u'id': u'134331240066620', u'is_published': True}, {u'category': u'Community', u'username': u'petroliumengineeringbuildingstatueisreallyhot', u'about': u'Once there was a fake confessions page, but all that changed when the fire nation attacked. \nPage for funny posts, trolls, and pranks. Cstat based.', u'talking_about_count': 3, u'name': u'Texas A&M: Department of Trolls', u'has_added_app': False, u'can_post': True, u'cover': {u'source': u'https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-xfp1/v/t1.0-9/10389249_326711990837859_4680051574179118442_n.jpg?oh=e49b6c100c5a9ed92fa4ccb1ddc309df&oe=5494F680&__gda__=1419176969_17bdee9ce41050adbcb8b0e2d1acf543', u'cover_id': 326711990837859, u'offset_x': 0, u'offset_y': 0}, u'link': u'https://www.facebook.com/petroliumengineeringbuildingstatueisreallyhot', u'likes': 321, u'parking': {u'street': 0, u'lot': 0, u'valet': 0}, u'is_community_page': False, u'were_here_count': 0, u'checkins': 0, u'id': u'230522747123451', u'is_published': True}, {u'category': u'Cause', u'username': u'NYUSecrets', u'about': u"Share your secrets. Let's build a community--once and for all.\nFAQ: http://nyusecrets.tumblr.com/post/86017930330/frequently-asked-questions", u'talking_about_count': 7330, u'description': u"NYU is a strange place sometimes. It's hard to find a community. It's hard to find a place to fit in. If you're struggling with your time here, this is the place to vent. Share your secrets. Let's build a community--once and for all. Completely unaffiliated with New York University.\n", u'has_added_app': False, u'can_post': True, u'cover': {u'source': u'https://scontent-a.xx.fbcdn.net/hphotos-xap1/t31.0-8/s720x720/1912396_763842263651300_8650989269152821172_o.jpg', u'cover_id': 763842263651300, u'offset_x': 0, u'offset_y': 0}, u'mission': u'To give NYU a community. ', u'name': u'NYU Secrets', u'link': u'https://www.facebook.com/NYUSecrets', u'likes': 30920, u'parking': {u'street': 0, u'lot': 0, u'valet': 0}, u'is_community_page': False, u'were_here_count': 0, u'checkins': 0, u'id': u'455528264482703', u'is_published': True}]

'''
def assignGenderStats():
	genderDict = assignGender()

def selectCodedPosts():
	lines = open("StatsForPosts.csv").readlines()[1:]
	postIDs = []
	for line in lines:
		postIDs += [line.split("|")[0]]
	comments =  processCommentList()
	selectedComments = {}
	restComments = {}
	for uni in comments.keys():
		for postID in comments[uni].keys():
			if postID in postIDs:
				selectedComments[postID] = comments[uni][postID]
			else:
				restComments[postID]= comments[uni][postID]

	return selectedComments

def selectRemainingPosts(postIDs):

	comments =  processCommentList()
	selectedComments = {}
	restComments = {}
	for uni in comments.keys():
		for postID in comments[uni].keys():
			if postID in postIDs:
				selectedComments[postID] = comments[uni][postID]
			

	return selectedComments

def assignGender(selectedComments, postID,graph):
	male = female = 0
	if postID in selectedComments.keys():
		for comment in selectedComments[postID]:
			userID = comment["userID"]
			try:
				fbDetails = graph.get_object(userID)
				if "gender" in fbDetails.keys() and 'first_name' in fbDetails.keys():
					if "female" in fbDetails["gender"]:
						female += 1
					elif "male" in fbDetails["gender"]:
						male += 1
						

			except:
				continue
	return male,female

def assignGenderID(userID,graph):
	
	try:
		fbDetails = graph.get_object(userID)
		if "gender" in fbDetails.keys():
			if "female" in fbDetails["gender"]:
				return "Female"
			elif "male" in fbDetails["gender"]:
				return "Male"
			else:
				return "None"
		else:
			return "None"
						
	except:
		return "None"


def detectGenderCodedPosts():

	selectedComments = selectCodedPosts()
	lines = open("StatsForPosts.csv").readlines()[1:]
	#graph = facebook.GraphAPI(apiKey)
	userIDs, userIDict = [],{}
	userGender = {}
	for line in lines[1:]:
		postID = line.split("|")[0]
		ids = []
		if postID in selectedComments.keys():
			for comment in selectedComments[postID]:
				userIDs += [comment["userID"]]
				ids += [comment["userID"]]

			ids = list(set(ids))
			userIDict[postID] = ids

	userIDs = list(set(userIDs))
	return userIDs
	'''
	for userID in userIDs:
		userGender[userID] = assignGenderID(userID,graph)
		print userID, userGender[userID]

	output = open('userGender2.pkl', 'wb')
	pickle.dump(userGender, output)
	output.close()

	output = open('userIDict2.pkl', 'wb')
	pickle.dump(userIDict, output)
	output.close()

	return selectedComments, userGender, userIDict
	'''
def detectGenderRestPosts():

	selectedComments = pickle.load(open('selected.pkl', 'rb'))
	lines = open("StatsForPosts.csv").readlines()[1:]
	graph = facebook.GraphAPI("CAAGljQ0ymaQBACwaEbDhp9mwMVCZAYJl7wgAuKhCOUqvbJ0ufh1kahYzU6zEhJF6osT6ta4fiILAY39Hy0dqeAAXnAosJtKBbZAblHhOQKOeSS4MkZBOic8cPs40ZAEOjHnNs8UwoBBJgJ4bZCPpmzfJGwDJ1NgNK6VZBDJBXMYxnivp6vBqW6yUqB92BC4Mb34cMaMylOZAfM0TPC83yUWEKaklskTe8cZD")
	userIDs, userIDict = [],{}
	userGender = {}
	for line in lines[1:]:
		postID = line.split("|")[0]
		ids = []
		if postID in selectedComments.keys():
			for comment in selectedComments[postID]:
				userIDs += [comment["userID"]]
				ids += [comment["userID"]]

			ids = list(set(ids))
			userIDict[postID] = ids

	userIDs = list(set(userIDs))
	for userID in userIDs:
		userGender[userID] = assignGenderID(userID,graph)
		print userID, userGender[userID]

	return userGender, userIDict

def assignGenderPosts():
	#selectedComments = selectCodedPosts()
	userGender = pickle.load(open('userGender.pkl', 'rb'))
	userIDict = pickle.load(open('userIDict.pkl', 'rb'))
	restGender, restDict = detectGenderRestPosts()
	f = open("StatsForPostsGender.csv","w")
	header = 'PostID | uni | Size | Religious | State | Politics | Tuition | Post | numLikes | numComments | wordCount |No. of Male Commentors|No. of Female Commentors|No. of None Commentors| isCoded|Taboo | Stigma | isQuestion | questionType | Loneliness | Stress | Victim\n'
	f.write(header)
	postIDs = []
	lines = open("StatsForPosts.csv").readlines()[1:]
	count = 0
	for line in lines[1:]:
		col = line.split("|")
		postID = col[0]
		gender = []
		if postID in userIDict.keys():
			for userID in userIDict[postID]:
				gender += [userGender[userID]]
		else:
			if postID in restDict.keys():
				for userID in restDict[postID]:
					gender += [restGender[userID]]

		gender = Counter(gender)
		
		if "Male" not in gender:
			gender['Male'] = 0
		if "Female" not in gender:
			gender['Female'] = 0
		if "None" not in gender:
			gender['None'] = 0
		
		isCoded = col[11]
		if "Y" in isCoded:
			first = line.rsplit("|",8)[0]
		else:
			first = line.rsplit("|",1)[0]

		last = line.split("|",11)[-1]

		newLine = first + "|"+str(gender["Male"])+"|"+str(gender["Female"])+"|"+str(gender["None"])+"|"+last
		f.write(newLine)


def createStatsForComments():
	comments = processCommentList()
	posts = processPostsDict()
	genderDict = {}
	lines= open("StatsForPosts.csv").readlines()[1:]
	f = open("StatsForComments.csv","w")
	f.write('commentID|postID|uni|post|userID| username|time|comment|wordCount|numLikes\n')
	for line in lines:
		postID = line.split("|")[0]
		uni = line.split("|")[1]
		if postID in comments[uni]:
			for comment in comments[uni][postID]:
				post = posts[uni][postID]['message']
				message = comment['message'].replace("\n","").replace("^M","")
				line = comment['commentID'] + "|"+postID+"|"+uni +"|"+post+"|"+comment['userID']+"|"+comment['userName']+"|"+comment['time']+ "|"
				line += message+ "|"+str(len(message.split()))+ "|"+comment['likeCount']+'\n'
				f.write(line)

	#output = open('genderDict.pkl', 'wb')
	#pickle.dump(genderDict, output)
	#output.close()

#createStatsForComments()
def genderCodeComments(apiKey):
	graph = facebook.GraphAPI(apiKey)
	comments = open("StatsForComments.csv").readlines()[1:]
	f = open("StatsForCommentsGender.csv","w")
	genderDict = {}
	header = 'commentID|postID|uni|post|userID| username|gender|time|comment|wordCount|numLikes\n'
	f.write(header)
	for comment in comments:
		col = comment.split("|")
		userID = col[4]
		genderDict[userID] = assignGenderID(userID, graph)

		first =  comment.rsplit("|",4)[0]
		second = comment.split("|",6)[-1]
		newLine = first + "|"+genderDict[userID]+"|"+second
		f.write(newLine)

	output = open('genderDict.pkl', 'wb')
	pickle.dump(genderDict, output)
	output.close()




		









