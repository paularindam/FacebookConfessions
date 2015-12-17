import numpy as np
import matplotlib.pyplot as plt
import pylab


def barchartLIWC(cat):
	keys = ["sex","religious","death","sad","anger", "anxiety"]

	N = 6
	values = [[None]*6]*6
	for i in range(N):
		for j in range(N):
			x = int(cat[keys[j]][keys[i]])
			values[i][j] = int(cat[keys[j]][keys[i]])
			print values[i][j]
			
	

		
	keys = tuple(keys)
	ind = np.arange(N)  # the x locations for the groups
	#ind = np.arange(0, 2*N, 2)
	width = 0.35       # the width of the bars
	fig, ax = plt.subplots()#figsize = (144,12))
	rects = []
	rects1 = ax.bar(ind, values[0], width, color='b')
	rects2 = ax.bar(ind + width, values[1], width, color='g')
	rects3 = ax.bar(ind + (2*width), values[2], width, color='r')
	rects4 = ax.bar(ind + (3*width), values[3], width, color='c')
	rects5 = ax.bar(ind + (4*width), values[4], width, color='m')
	rects6 = ax.bar(ind + (5*width), values[5], width, color='y')

	ax.set_ylabel('Percentages %')
	ax.set_title('Percentages by LIWCategory matching')
	ax.set_xticks(ind+width)
	ax.set_xticklabels(keys)
	#ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
	ax.legend( (rects1[0], rects2[0],rects3[0], rects4[0],rects5[0], rects6[0] ), (keys[0], keys[1],keys[2], keys[3],keys[4], keys[5]) )
	def autolabel(rects):
	    # attach some text labels
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)
	autolabel(rects4)
	autolabel(rects5)
	autolabel(rects6)

	#maximum = max()
	#if maximum *1.3 <110:
	#	plt.ylim((0, 1.3 * maximum ))
	#else:
	plt.ylim(0, 100)
	fileName = 'LIWCCommentsByPosts.chart.png'
	pylab.savefig(fileName, bbox_inches='tight')

# initial barchart function which needs 9 arguments 
#barchart("comment", "anger", cat1, cat2, keys, "religious", "Not religious", )
def barchart(postcomment, LIWCategory, cat1, cat2, keys, namCat1, namCat2, feature1, feature2= ""):
	
	N = len(cat1.keys())
	values1 = []
	values2 = []
	for key in keys:
		values1 += [cat1[key]]
		values2 += [cat2[key]]
	
	if feature1 == "timeOfDay":
		keys = tuple(["earlyMorning", "lateMorning", "earlyAfternoon", "lateAfternoon", "evening", "night", "lateNight", "beforeSunRise"])
		
	elif feature1 == "month":
		newKeys = []
		year = {"January" :"Jan", "February":"Feb", "March":"Mar", "April":"Apr", "May":"May", "June":"Jun", "July":"Jul", "August":"Aug", "September":"Sep", "October":"Oct", "November":"Nov", "December":"Dec"}
		for key in keys:
			newKeys += [year[key]]
		keys = tuple(newKeys)
	else:
		keys = tuple(keys)
	ind = np.arange(N)  # the x locations for the groups
	width = 0.35       # the width of the bars
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, values1, width, color='r')
	rects2 = ax.bar(ind + width, values2, width, color='b')
	ax.set_ylabel('Percentages %')
	if feature2 == "":
		ax.set_title('LIWC Category '+ LIWCategory+ ': Percentages by '+ feature1)
	else:
		ax.set_title('LIWC Category '+ LIWCategory+ ': Percentages by '+ feature1 +' and ' + feature2)
	ax.set_xticks(ind+width)
	ax.set_xticklabels(keys)
	#ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
	ax.legend( (rects1[0], rects2[0]), (namCat1, namCat2) )
	def autolabel(rects):
	    # attach some text labels
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
	                ha='center', va='bottom')
	autolabel(rects1)
	autolabel(rects2)
	maximum = max(max(cat1.values()), max(cat2.values()))
	plt.ylim((0, 1.3 * maximum ))

	fileName = postcomment+'/'+LIWCategory+"-"+feature2+feature1+'.chart.png'
	pylab.savefig(fileName, bbox_inches='tight')

#its only for barchart for comparing different unis together without categories
def barchartNew(O, name):
	OX = O.keys()
	OY = O.values()
	fig = plt.figure(figsize = (30,36))
	width = .35
	ind = np.arange(len(OY))
	plt.bar(ind, OY)
	plt.xticks(ind + width / 2, OX)
	fig.autofmt_xdate()
	plt.savefig(name+".pdf")

#its for barchart 
def barchartClose(O,name,width = 1):
	OX = O.keys()
	OY = O.values()
	fig = plt.figure()
	#fig, ax = plt.subplots(figsize = (48,12))
	data = OY
	bin = np.arange(len(data))  
	ax = plt.subplot(111)
	ax.bar(bin, data, width, color='r')
	plt.xticks(bin + 1.25/ 2, OX)
	fig.autofmt_xdate()
	plt.savefig(name+".pdf")

def histogram(O, name, width = 1):
	barchartClose(O, name, width)
#keys: items
#cat1,2 : list of data
#namCat1,2 : name of the legend
#feature1,2: {time, features (only in title)
#postcomment : post or comment (only in title)
#LIWCategory : name of LIWCategory (only in title)
#barchart4(categoryDict[0], categoryDict[1],categoryDict[2])

#keys would be list of schools (dict.keys())
#post and comment can be inside one chart
def barchartSimple( keys,cat1, cat2,feature, namCat1 = "posts", namCat2 = "comments", postcomment = "PostsComments"):
	newKeys = []
	N = len(cat1.keys())
	values1 = []
	values2 = []
	for key in keys:
		values1 += [cat1[key]]
		values2 += [cat2[key]]
	'''
		if "University of" in key:
			key = key.split("University of")[1]
		elif "College" in key:
			key = key.split("College")[0]
		elif " University" in key:
			key = key.split("University")[0]
		newKeys += [key]
	keys = tuple(newKeys)
	'''
	keys = tuple(keys)
	#ind = np.arange(N)  # the x locations for the groups
	ind = np.arange(0, 2*N, 2)
	width = 0.35       # the width of the bars
	fig, ax = plt.subplots(figsize = (144,12))
	rects1 = ax.bar(ind, values1, width, color='r')
	rects2 = ax.bar(ind + width, values2, width, color='b')
	ax.set_ylabel('Percentages %')
	ax.set_title('Percentages by '+ postcomment +' and ' + feature)
	ax.set_xticks(ind+width)
	ax.set_xticklabels(keys)
	#ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
	ax.legend( (rects1[0], rects2[0]), (namCat1, namCat2) )
	def autolabel(rects):
	    # attach some text labels
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
	                ha='center', va='bottom')
	autolabel(rects1)
	autolabel(rects2)
	maximum = max(max(cat1.values()), max(cat2.values()))
	if maximum *1.3 <110:
		plt.ylim((0, 1.3 * maximum ))
	else:
		plt.ylim((0, 110))
	fileName = "newCharts/"+postcomment+" "+feature+'.chart.png'
	pylab.savefig(fileName, bbox_inches='tight')

#it is for wide barcharts for TODW
def barchartWide(postcomment, LIWCategory, cat1, cat2, keys, namCat1, namCat2, feature1, feature2):
	
	
	N = len(cat1.keys())
	values1 = []
	values2 = []
	for key in keys:
		values1 += [cat1[key]]
		values2 += [cat2[key]]
	
	
	
	keys = tuple(keys)
	ind = np.arange(N)  # the x locations for the groups
	width = 0.35       # the width of the bars

	fig, ax = plt.subplots(figsize = (24,12))
	rects1 = ax.bar(ind, values1, width, color='r')
	rects2 = ax.bar(ind + width, values2, width, color='b')
	ax.set_ylabel('Percentages %')
	ax.set_title('LIWC Category '+ LIWCategory+ ': Percentages by '+ feature1 +' and ' + feature2)
	ax.set_xticks(ind+width)
	ax.set_xticklabels(keys)

	ax.legend( (rects1[0], rects2[0]), (namCat1, namCat2) )
	def autolabel(rects):
	    # attach some text labels
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
	                ha='center', va='bottom')
	autolabel(rects1)
	autolabel(rects2)
	maximum = max(max(cat1.values()), max(cat2.values()))
	#ax.set_autoscale_on(False)
	xmin, xmax = plt.xlim()
	
	fileName = postcomment+'LIWCategory'+LIWCategory+"-"+feature2+feature1+'.chart.png'
	pylab.savefig(fileName)

def main():
	menMeans = {'G1': 20, 'G2': 35, 'G3': 30, 'G4': 35, 'G5': 27}
	womenMeans = {'G1' : 25, 'G2' : 32, 'G3' : 34, 'G4' : 20, 'G5' : 25}
	feature1 = "religion"
	feature2 = "day"
	barchart(menMeans, womenMeans, "Men", "Women",feature1, feature2)
