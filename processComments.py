#f = open("processedComments.csv","a")
f = open("processedCommentsID.csv","w")
f.write("university | postID | Post | Username | Time | CommentID| Comment|Viable Ans?|Mean Post|Taboo?|Stigma?|Stigma type?|inter w/ OP|inter w/ com||||||||\n")
'''
for num in range(1,4):
	lines = open("comments"+str(num)+".csv").readlines()[1:]
	for line in lines:
		uni = line.split("|")[0]
		if "Davis" in uni:
			continue
		f.write(line)
for num in range(4,7):
	lines = open("comments"+str(num)+".csv").readlines()[1:]
	for line in lines:
		org = line.rsplit("|",7)
		line = org[0]+"|"+org[2]+"|"+org[3]+"|"+org[4]+"|"+org[5]+"|"+org[6]+"|"+org[7]
		uni = line.split("|")[0]
		if "Davis" in uni:
			continue
		f.write(line)
'''

for num in range(7,9):
	lines = open("comments"+str(num)+".csv").readlines()[1:]
	for line in lines:
		#org = line.rsplit("|",8)
		#line = org[0]+"|"+org[3]+"|"+org[4]+"|"+org[5]+"|"+org[6]+"|"+org[7]+"|"+org[8]
		uni = line.split("|")[0]
		if "Davis" in uni:
			continue
		f.write(line)