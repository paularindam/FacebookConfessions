f = open("isAllPosts.csv","w")
f.write('PostID | uni | Size | Religious | State | Politics | Tuition | Post | numLikes | numComments | wordCount | isCoded |isLiked|isCommented\n')
lines = open("StatsForPosts.csv").readlines()[1:]
count = 0
for line in lines:
	line = line.rsplit("|",9)[0]
	col = line.split("|")
	if len(col) <10:
		count += 1
		continue
	if not col[8] or " " in col[8] or int(col[8])==0:
		isLiked = "N"
	else:
		isLiked = "Y"
	if not col[9] or  " " in col[9] or int(col[9])==0:
		isCommented = "N"
	else:
		isCommented = "Y"
	f.write(line+"|"+isLiked+"|"+isCommented+"\n")
print count

