from __future__ import division
from collections import Counter
import scipy
import os
import myFunctions as m
from scipy import stats
from scipy.stats import mode

	
def stats():
	posts = open("lenPosts.dat").readlines()
	#f = open("statsData.csv","w")
	List = os.listdir("USA")
	path = "USA/"
	newPath = "USACommentStats/"
	
	g = open("zeroLikeComments.dat",'w')
	h = open("commentStats.csv",'w')
	h.write("university,numPosts,numComments,numCommentators,commentsPerCommentator\n")
	j = open("topCommentators.dat",'w')
	
	import sys
	grandTotalLikes = []
	totalLikes = {}
	
	grandTotalPosts = 0
	grandTotalComments = 0
	grandTotalCommentators = 0

	zeroLikes = {}
	zeroComments = {}

	avoidList = []
	count = 0
	for Filename in List:
		actualFileName = Filename
		newFilename = newPath + Filename
		Filename = path + Filename
		if "comments" not in Filename:
			avoidList += [Filename]
			continue
		

		f = open(newFilename.replace(".csv","ByLikes.dat"),'w')
		lines = open(Filename).readlines()
		if len(lines)<3:
			avoidList += [Filename]
			continue
		count +=1
		prefix = actualFileName.split("comments.csv")[0]
		idx = -1
		totalPosts = 0
		for post in posts:
			if prefix in post:
				idx = posts.index(post)
				totalPosts = post.rsplit(":",1)[1]
				break

		#if ":" in prefix:
		#	prefix = prefix.replace(":","")
		#if " " in prefix:
		#	prefix = prefix.replace(" ","")
		
		totalLikes[prefix] = [[]]
		totalLikes[prefix].append([])
		commentatorID = []
		totalComments = 0

		for line in lines[1:]:
			columns = line.split("|")
			try:
				totalComments += 1
				commentatorID += [columns[3].strip()]
				numLikes = int(columns[5])
				totalLikes[prefix][0] += [columns[6]]
				totalLikes[prefix][1] += [numLikes]
			except:
				pass	
		
		grandTotalPosts += int(totalPosts)
		grandTotalComments += totalComments
		commentatorCount = Counter(commentatorID)
		totalCommentators = len(list(set(commentatorID)))
		grandTotalCommentators += totalCommentators
		commentsPerCommentator = totalComments/totalCommentators
		
		zeroLikes[prefix] = totalLikes[prefix][1].count(0)
		
		totalLikes[prefix] = sorted(zip(*totalLikes[prefix]), key = lambda l:l[1], reverse = True)

		grandTotalLikes += totalLikes[prefix]
		
		for like in totalLikes[prefix]:
			f.write(str('"'+ like[0].replace('"','').strip()+'"')+"|"+str(like[1])+"\n")
		
	
		f.close()

		zeroTotalLikes = grandTotalLikes.count(0)
		g.write(prefix+"|"+str(zeroLikes[prefix])+"\n")
		
		j.write(prefix)

		for ID in commentatorCount.keys():
			j.write("|"+ str(ID))
		j.write("\n")

		if idx == -1:
			print prefix
		else:
			h.write(prefix+","+str(totalPosts.strip())+","+str(totalComments)+","+str(totalCommentators)+","+str(commentsPerCommentator)+"\n")

	h.write("total,"+str(grandTotalPosts)+","+str(grandTotalComments)+","+str(grandTotalCommentators)+","+str(grandTotalComments/grandTotalCommentators)+"\n")
stats()
