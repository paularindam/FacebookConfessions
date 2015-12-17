import os
g = open("FCB/scraped.dat","w")
lst = []
files = os.listdir("FCB")
for f in files:
	if ".csv" in f:
		lst.append(f.split(":")[0])

lst = list(set(lst))

for ele in lst:
	g.write(str(ele)+"\n")

print "Checked for files already scraped................."	

