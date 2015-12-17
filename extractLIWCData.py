from myTime import myTime
from collections import Counter
from processUnis import *
from myTime import *

import scipy
from scipy import stats
from scipy.stats import mode

from extractPercent import *
from barchart import *

import sys

LIWCategories = ["sex","religious","death","sad","anger", "swear", "social", "family", "friends", "humans", "anxiety", "body", "health", "ingest", "time", "work", "achievment", "leisure", "home", "money"]

for LIWCategory in LIWCategories:
	percentPosts, percentComments = processUnisAll("USA/", LIWCategory, True)
	barchartSimple(percentPosts.keys(), percentPosts, percentComments, LIWCategory)
