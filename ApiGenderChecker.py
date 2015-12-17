#!/usr/bin/env python

import sys
sys.path.append("/Users/arindam/Confessions/genderize")
from genderize import Genderize
if len(sys.argv)>1:
	gender = sys.argv[1]

readFile = "firstNameList.dat"
writeFile = "apiFirstName.dat"

#genderNames = open("Text_Data/my"+gender+".txt").readlines()
#f = open("api"+gender+".txt",'w')
genderNames = open(readFile).readlines()
f = open(writeFile,'w')
count = 0
for i in range(len(genderNames)):
	genderNames[i] = genderNames[i].strip()

genderList = []
for i in range(0,len(genderNames),10):
	genderNams = genderNames[i:(i+10)]
	genderList += Genderize().get(genderNams)

probability = count = 0
for i in range(len(genderList)):
	if genderList[i]['gender'] is not None:
		probability = genderList[i]['probability']
		count = genderList[i]['count']
	else:
		genderList[i]['gender'] = "None"
	print(genderNames[i]+":"+genderList[i]['gender']+","+str(count)+","+str(probability)+"\n")
	f.write(genderNames[i]+":"+genderList[i]['gender']+","+str(count)+","+str(probability)+"\n")

f.close()
