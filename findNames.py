#This will look for names in posts and comments

import os

namePosts = open("namePosts.dat","w")
nameComments = open("nameComments.dat","w")
names = open("firstNameList.dat").readlines()

lst = os.listdir("USA")
path = "USA/"
for Filename in lst:
	print Filename
	Filename = path + Filename

	text = open(Filename).readlines()
	for line in text[1:]:
		count = 0
		if "comments" in Filename:	
			message = line.split("|")[6]
			for name in names:
				if name in message:
					count += 1
			if count > 0: 
				nameComments.write(str(count)+"|"+message+"\n")
		elif "posts" in Filename:
			message = line.split("|")[2]
			for name in names:
				if name in message:
					count += 1
			if count > 0:
				namePosts.write(str(count)+"|"+message+"\n")
		
	

