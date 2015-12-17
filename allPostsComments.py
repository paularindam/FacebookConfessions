import os

path = "/Users/arindam/All/"
fileList = os.listdir(path)
newpath = "/Users/arindam/AllTogether/"
collegeName = []
for aFile in fileList:
	if "posts" in aFile:
		collegeName += [aFile.replace("posts","")]
	elif "comments" in aFile:
		collegeName += [aFile.replace("comments","")]
print len(collegeName)
collegeName = list(set(collegeName))
print
print collegeName
print
print len(collegeName)

for college in collegeName:
	f = open(newpath+college,'w')
	for i in range(2):
		if i ==0:
			aFile = college.replace(".csv","posts.csv")
			column = 2
		else:
			aFile = college.replace(".csv","comments.csv")
			column = 6

		filePath = path+aFile
		lines = open(filePath).readlines()

		for line in lines:
			f.write(str(line.split("|")[column])+"\n")
	
	f.close()

