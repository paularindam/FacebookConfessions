from processUnis import *
from barchart import *

import scipy
from scipy import stats
from scipy.stats import mode

posts, comments, allPosts, allComments = processUnisAll("USA/")
numPosts = {}
for key in posts.keys():
	numPosts[key] = len(posts[key])

barchartNew(numPosts, "QPosts")	

