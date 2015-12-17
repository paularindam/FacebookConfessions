import os

lst = os.listdir("FCB")
for fileName in lst:
	f = open("FCB/"+fileName)
	g = open("FCB_excel/"+fileName,"w")
	lines = f.readlines()

	g.write(lines[0])
	lines = lines[1:]
	for line in lines:
		line = line.split("|")
		for l in line:
			l = l.replace(",","")
			g.write(l+",")

	g.close()
#	if line.index(l) == 2:
#		x,y = l.split(" ",1)
#		print x
#		print y
#	else:
#		pass
