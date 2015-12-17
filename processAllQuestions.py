from processUnis import *
from mapUnis import *
import re

def processAllQuestions():
	allPosts = open("StatsForLIWCPosts.csv").readlines()
	f = open("StatsForLIWCPosts.csv","a")
	#f.write("PostID | uni | Size | Religious | State | Politics | Tuition | Post | numLikes | numComments | isCoded |  Taboo | Stigma | isQuestion | questionType | Loneliness | Stress | Victim\n")
	done = []
	
	for post in allPosts[1:]:
		done += [post.split("|")[0]]
	#print done
	posts = processPosts()
	postIDs = []
	for uni in posts.keys():
		for post in posts[uni]:
			uniInfo = mapUniDict(uni)
			if post["postID"] not in done:
				postIDs += [post["postID"]]
				if "527813577257803_630067583699068" in post["postID"] or "599429153419231_113350488871762" in post["postID"]:
					continue
				f.write(post["postID"]+"|"+uni+"|"+uniInfo["size"]+"|"+uniInfo["isReligious"]+"|"+ uniInfo["state"]+"|"+ uniInfo["politics"]+"|"+ uniInfo["tuition"]+ "|"+post["message"] + "|"+post["numLikes"]+"|"+post["numComments"]+"|"+str(len(post["message"].split()))+"|")
				for LIWCategory in LIWC.order():
					f.write(processLIWCNum(post["message"],LIWCategory)+ "|")

				f.write("N\n")
		
	
	#print set(done).intersection(set(postIDs))
				
processAllQuestions()