lines = open("StatsForCodedPostsJmp.csv").readlines()
f = open("JmpStats.csv","w")
for line in lines[1:]:
	col = line.split("|")
	numLikes, numComments = int(col[8]), int(col[9])
	line = line.strip()
	if numLikes == 0 and numComments ==0:
		f.write(line+"|N|N\n")
	elif numLikes != 0 and numComments !=0:
		f.write(line+"|Y|Y\n")
	elif numLikes != 0 and numComments ==0:
	        f.write(line+"|Y|N\n")
	elif numLikes == 0 and numComments !=0:
	        f.write(line+"|N|Y\n")
	


