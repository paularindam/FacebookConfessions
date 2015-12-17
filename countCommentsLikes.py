import scipy
import os
import myFunctions as m
from scipy import stats
from scipy.stats import mode

	
def stats():
	f = open("statsData.csv","w")
	List = os.listdir("USA")
	path = "USA/"

	import sys
	grandTotalComments = []
	grandTotalLikes = []

	totalLikes = {}
	totalComments = {}

	averageLikes = {}
	averageComments = {}

	stdDevLikes = {}
	stdDevComments = {}
	
	modeLikes = {}
	modeComments = {}

	medianLikes = {}
	medianComments = {}

	avoidList = []
	count = 0
	f.write("School"+","+"averageLikes"+","+"stdDevLikes"+","+"medianLikes"+","+"modeLikes"+","+"averageComments"+","+"stdDevComments"+","+"medianComments"+","+"modeComments"+"\n")
	for Filename in List:
		Filename = path + Filename
		if "posts" not in Filename:
			avoidList += [Filename]
			continue

		lines = open(Filename).readlines()
		
		if len(lines)<3:
			avoidList += [Filename]
			continue
		count +=1
		prefix = Filename.split("posts.csv")[0]
		
		totalLikes[prefix] = []
		totalComments[prefix] = []
		
		for line in lines[1:]:
			columns = line.split("|")
			
			try:
				numLikes = int(columns[3])
				numComments = int(columns[4])
			
				totalLikes[prefix] += [numLikes]
				totalComments[prefix] += [numComments]
			except:
				pass	

		averageLikes[prefix] = str(scipy.mean(totalLikes[prefix]))
		averageComments[prefix] = str(scipy.mean(totalComments[prefix]))
		stdDevLikes[prefix] = str(scipy.std(totalLikes[prefix]))
		stdDevComments[prefix] = str(scipy.std(totalComments[prefix]))
		
		medianLikes[prefix] = str(scipy.median(totalLikes[prefix]))
		medianComments[prefix] = str(scipy.median(totalComments[prefix]))
		modeLikes[prefix] = str(mode(totalLikes[prefix])[0][0])
		modeComments[prefix] = str(mode(totalComments[prefix])[0][0])

		grandTotalComments += totalComments[prefix]
		grandTotalLikes += totalLikes[prefix]
		f.write(prefix.split("USA/").pop()+","+averageLikes[prefix]+","+stdDevLikes[prefix]+","+medianLikes[prefix]+","+modeLikes[prefix]+ ","+ averageComments[prefix]+","+stdDevComments[prefix]+","+medianComments[prefix]+","+modeComments[prefix]+"\n")


	averageTotalLikes = scipy.mean(grandTotalLikes)
	averageTotalComments = scipy.mean(grandTotalComments)
	stdDevTotalLikes = scipy.std(grandTotalLikes)
	stdDevTotalComments = scipy.std(grandTotalComments)
	medianTotalLikes = scipy.median(grandTotalLikes) 
	medianTotalComments = scipy.median(grandTotalComments)
	modeTotalLikes = mode(grandTotalLikes)[0][0]
	modeTotalComments = mode(grandTotalComments)[0][0]

	print "Stats calculated. See statsComplete.dat for overall stats and statsData.csv for individual FCB stats" 
	f.close()
	f = open("statsComplete.dat","w")

	m.fileWrite(f, "Entire dataset stats")
	m.fileWrite(f, "averagelikes: "+str(averageTotalLikes))
	m.fileWrite(f, "averagecomments: " +str(averageTotalComments))
	m.fileWrite(f, "stdDevlikes: "+str(stdDevTotalLikes))
	m.fileWrite(f, "stdDevcomments: "+str(stdDevTotalComments))
	m.fileWrite(f, "medianlikes: "+str(medianTotalLikes))
	m.fileWrite(f, "mediancomments: " +str(medianTotalComments))
	m.fileWrite(f, "modelikes: "+str(modeTotalLikes))
	m.fileWrite(f, "modecomments: "+str(modeTotalComments))

stats()
