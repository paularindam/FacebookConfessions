lines = open("JmpStats.csv").readlines()[1:]
header = 'PostID | uni | Size | Religious | State | Politics | Tuition | Post | numLikes | numComments | wordCount | isCoded | Taboo | Stigma | isQuestion | questionType | Loneliness | Stress | Victim|isLiked|isCommented|isTaboo|isStigma\n'
f = open("TabooStigmaJmpStats.csv","w")
f.write(header)
for line in lines:
	col = line.split("|")
	isStigma, isTaboo = "N","N"
	if "None" not in col[12]:
		isTaboo = "Y"
	if "None" not in col[13]:
		isStigma = "Y"
	f.write(line.strip()+"|"+isTaboo+"|"+isStigma+"\n")


	


