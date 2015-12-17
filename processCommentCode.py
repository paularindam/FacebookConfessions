from collections import Counter
from processUnis import *

def processCommentCode():
	#lines = open("comments1.csv").readlines()
	lines = open("comments7.csv").readlines()
	commentInfo = processComment()
	Dict = {}
	lines = lines[1:]
	for line in lines:
		cols = line.split("|")
		dct = {}
		dct["uni"] = cols[0]
		dct["postID"] = cols[1]
		dct["post"] = cols[2]
		dct["username"] = cols[3]

		dct["time"] = cols[4]
		#dct["commentID"] = cols[5]
		dct["likeCount"] =commentInfo[dct["uni"]][cols[5]]["likeCount"]

		'''
		dct["comment"] = cols[4]
		dct["isAnswer"] = cols[5]
		dct["isMeanPost"] = cols[6]
		dct["isTaboo"] = cols[7]
		dct["isStigma"] = cols[8]
		dct["stigmaType"] = cols[9]
		'''
		Dict[cols[5]] = dct
	return Dict
	