import csv
g = open("insertPosts.sql","w")
g.write("insert into posts(schoolid, postid, message, numlikes,numcomments,type)\n") 
with open("allPosts.csv", 'rb') as f:
	#csvreader = csv.DictReader(f,delimiter='|')
	rows = list(csv.reader(f,delimiter = '|'))
	rows = rows[1:]
	print rows[1000][3]
	for row in rows:
		schoolid = str(row[0])
		postid = str(row[1])
		time = str(row[2])
		message = str(row[3])
		numlikes = str(row[4])
		numcomments = str(row[5])
		Type = str(row[6])

		g.write("Values("+schoolid+","+postid+","+time+","+message+","+numlikes+","+numcomments+","+Type+")")
		g.write("\n")

g.write(";")
	
