import scipy
import os
import myFunctions as m
from scipy import stats
from scipy.stats import mode

	
def stats():
	#f = open("statsData.csv","w")
	List = os.listdir("USA")
	path = "USA/"
	newPath = "USAStats/"
	zl = open("zeroLikePosts.dat",'w')
	zc = open("zeroCommentPosts.dat",'w')
	import sys
	grandTotalComments = []
	grandTotalLikes = []

	totalLikes = {}
	totalComments = {}

	zeroLikes = {}
	zeroComments = {}

	avoidList = []
	count = 0
	for Filename in List:
		actualFileName = Filename
		newFilename = newPath + Filename
		Filename = path + Filename
		if "posts" not in Filename:
			avoidList += [Filename]
			continue
	
		f = open(newFilename.replace(".csv","ByLikes.dat"),'w')
		g = open(newFilename.replace(".csv","ByComments.dat"),'w')
		lines = open(Filename).readlines()
		if len(lines)<3:
			avoidList += [Filename]
			continue
		count +=1
		prefix = actualFileName.split("posts.csv")[0]
		
		totalLikes[prefix] = [[]]
		totalComments[prefix] = [[]]

		totalLikes[prefix].append([])
		totalComments[prefix].append([])
		
		for line in lines[1:]:
			columns = line.split("|")
			try:
				numLikes = int(columns[3])
				numComments = int(columns[4])
				totalLikes[prefix][0] += [columns[2]]
				totalComments[prefix][0] += [columns[2]]
				totalLikes[prefix][1] += [numLikes]
				totalComments[prefix][1] += [numComments]
			except:
				pass	
	
		zeroLikes[prefix] = totalLikes[prefix][1].count(0)
		zeroComments[prefix] = totalComments[prefix][1].count(0)
		
		
		totalLikes[prefix] = sorted(zip(*totalLikes[prefix]), key = lambda l:l[1], reverse = True)
		totalComments[prefix] = sorted(zip(*totalComments[prefix]), key = lambda l:l[1], reverse = True)

		grandTotalComments += totalComments[prefix]
		grandTotalLikes += totalLikes[prefix]
		
		for like in totalLikes[prefix]:
			f.write(str('"'+ like[0].replace('"','')+'"')+"|"+str(like[1])+"\n")
		
		for comment in totalComments[prefix]:
			g.write(str('"'+comment[0].replace('"','')+ '"')+"|"+str(comment[1])+"\n")


		f.close()
		g.close()
		zl.write(prefix+"|"+str(zeroLikes[prefix])+"\n")
		zc.write(prefix+"|"+str(zeroComments[prefix])+"\n")
	zeroTotalLikes = grandTotalLikes.count(0)
	zeroTotalComments = grandTotalComments.count(0)
		
stats()
