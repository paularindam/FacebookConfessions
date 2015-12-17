import os
path = "/Users/arindam/All/"
files = os.listdir(path)
listNames = []
f = open("nameList.dat","w")
g = open("firstNameList.dat","w")
for fileName in files:
	if "comment" not in fileName:
		continue
	comments = open(path+fileName).readlines()
	usernameMap = {}
	for comment in comments[1:]:
		post_id, user_name = comment.split("|")[0],comment.split("|")[2]
		listNames += [user_name]
		usernameMap.setdefault(post_id,[]).append(user_name)
listNames = list(set(listNames))
firstNames = []
for name in listNames:
	f.write(name+"\n")
	if " " in name:
		name = name.split(" ")[0]
	firstNames += [name]

firstNames = list(set(firstNames))
for name in firstNames:
	g.write(name+"\n")
	
