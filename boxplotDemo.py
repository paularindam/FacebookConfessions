from pylab import *
import matplotlib.pyplot as plt
from scipy.io import loadmat

def boxPlot(name):
	NYCdiseases = loadmat('NYCDiseases.mat') # it's a matlab file

	# multiple box plots on one figure
	# Chickenpox cases by month
	figure(1)
	# NYCdiseases['chickenPox'] is a matrix 
	# with 30 rows (1 per year) and 12 columns (1 per month)
	print NYCdiseases['chickenPox']
	boxplot(NYCdiseases['chickenPox'][:2])
	labels = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
	          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
	xticks(range(1,13),labels, rotation=15)
	xlabel('Month')
	ylabel('Chickenpox cases')
	title('Chickenpox cases in NYC 1931-1971')
	plt.savefig(name+".pdf")

boxPlot("boxplotDemoNew")

