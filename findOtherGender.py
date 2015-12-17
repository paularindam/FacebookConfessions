from __future__ import division
import sys

if len(sys.argv) <3:
	lines = open("check"+sys.argv[1]+".txt").readlines()
else:
	lines = open(sys.argv[2]+sys.argv[1]+".txt").readlines()
other = 0
unisex = 0
notFound = 0
if  "Male" in sys.argv[1]:
	otherGender = "female"
elif "Female" in sys.argv[1]:
	otherGender = "male"

for line in lines:
	if ":"+otherGender in line:
		other+=1
	elif "unisex" in line:
		unisex += 1
	elif "None" in line:
		notFound += 1

print len(lines)
length = len(lines)
print other

print 100*(other/length)
print unisex
print 100*(unisex/length)
print notFound
print 100*(notFound/length)
