#!/usr/bin/env python

import sys
from identifyGender import *

readFile = "firstNameList.dat"
writeFile = "identifiedFirstName.dat"

#genderNames = open("Text_Data/my"+gender+".txt").readlines()
#f = open("api"+gender+".txt",'w')
genderNames = open(readFile).readlines()
f = open(writeFile,'w')
count = 0
for i in range(len(genderNames)):
	genderNames[i] = genderNames[i].strip()
	gender = identifyGender(genderNames[i])
	print(genderNames[i]+":"+gender+"\n")
	f.write(genderNames[i]+":"+gender+"\n")

f.close()
