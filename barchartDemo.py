import numpy as np
import matplotlib.pyplot as plt
import pylab

def saveFigure(count):
	N = 5
	menMeans = (20, 35, 30, 35, 27)
	menStd =   (2, 3, 4, 1, 2)

	ind = np.arange(N)  # the x locations for the groups
	width = 0.35       # the width of the bars

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, menMeans, width, color='r')

	womenMeans = (25, 32, 34, 20, 25)
	womenStd =   (3, 5, 2, 3, 3)
	rects2 = ax.bar(ind+width, womenMeans, width, color='y')

	# add some
	ax.set_ylabel('Scores')
	ax.set_title('Scores by group and gender')
	ax.set_xticks(ind+width)
	ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )

	ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )

	def autolabel(rects):
	    # attach some text labels
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)

	#plt.show()
	#plt.ylim((0,max(max(yvals), max(zvals)) + 1))
	pylab.savefig('foo'+str(count)+'.png', bbox_inches='tight')

def myBarSide(count):
	N = 3
	ind = np.arange(N)  # the x locations for the groups
	width = 0.27       # the width of the bars

	fig = plt.figure()
	ax = fig.add_subplot(111)

	yvals = [4, 9, 2]
	rects1 = ax.bar(ind, yvals, width, color='r')
	zvals = [1,2,3]
	rects2 = ax.bar(ind+width, zvals, width, color='g')
	#kvals = [11,12,13]
	#rects3 = ax.bar(ind+width*2, kvals, width, color='b')

	ax.set_ylabel('Scores')
	ax.set_xticks(ind+width)
	ax.set_xticklabels( ('2011-Jan-4', '2011-Jan-5', '2011-Jan-6') )
	#ax.legend( (rects1[0], rects2[0], rects3[0]), ('y', 'z', 'k') )
	#ax.set_xticklabels( ('2011-Jan-4', '2011-Jan-5') )
	ax.legend( (rects1[0], rects2[0]), ('y', 'z') )
	ax.set_ylim([0,10])

	def autolabel(rects):
	    for rect in rects:
	        h = rect.get_height()
	        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
	                ha='center', va='bottom')

	autolabel(rects1)
	autolabel(rects2)
	#autolabel(rects3)

	#plt.show()
	#x1,x2,y1,y2 = plt.axis()
	plt.ylim((0,max(max(yvals), max(zvals)) + 1))
	#plt.autoscale()
	#plt.show()
	pylab.savefig('foo'+str(count)+'.png', bbox_inches='tight')

	#plt.show()
	#pylab.savefig('foo'+str(count)+'.png', bbox_inches='tight')
	#pylab.savefig('foo'+str(count)+'.png')
def myBarStack(count):
	N = 5
	menMeans   = (20, 35, 30, 35, 27)
	womenMeans = (25, 32, 34, 20, 25)
	menStd     = (2, 3, 4, 1, 2)
	womenStd   = (3, 5, 2, 3, 3)
	ind = np.arange(N)    # the x locations for the groups
	width = 0.35       # the width of the bars: can also be len(x) sequence

	p1 = plt.bar(ind, menMeans,   width, color='r', yerr=None)
	p2 = plt.bar(ind, womenMeans, width, color='y',
	             bottom=menMeans, yerr=None)

	plt.ylabel('Scores')
	plt.title('Scores by group and gender')
	plt.xticks(ind+width/2., ('G1', 'G2', 'G3', 'G4', 'G5') )
	plt.yticks(np.arange(0,81,10))
	plt.legend( (p1[0], p2[0]), ('Men', 'Women') )

	#plt.show()
		#pylab.savefig('foo'+str(count)+'.png', bbox_inches='tight')
	pylab.savefig('foo'+str(count)+'.png', bbox_inches='tight')

#myBarSide(8)
saveFigure(10)