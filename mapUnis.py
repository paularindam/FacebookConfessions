import sys
from csv import reader
from collections import Counter
from manageExceptions import *

dictionary = {}

#isReligious --> "Present","None"
#politics --> "R","D"
#schoolSize" --> "small","top schools"
#tuition" --> "private","public"
#dictionary["ranking"] = ["high","low"]
#dictionary["population"] = ["high","low"] #To find out population based on S.D.

def mapUni(uni, uniList, category):
	flag = -1
	lst = {"id":0,"size":1,"ranking":2,"school":3,"confessionPage":4,"population":5,"tuition":6,"isReligious":7,"state":8,"region":9,"politics":10}
	for line in uniList:

		columns = line.split("|")
		school = columns[3]
		if "\xc2\xa0" in school:
			school = school.split("\xc2\xa0")[0]

		#school = correct(school)
		if uni not in school:
			continue
		
		if "politics" in category:
			if "R" in columns[lst[category]].strip():
				flag = 1

			elif "D" in columns[lst[category]].strip():
				flag = 0

		elif "tuition" in category:
			if "State" in columns[lst[category]].strip():
				flag = 1
			else:
				flag = 0

		elif "isReligious" in category:
			if "None" not in columns[lst[category]].strip():
				flag = 1
				
			else:
				flag = 0

		elif "size" in category:
			#print lst[category]
			#print columns[lst[category]]
			if "top" in columns[lst[category]].strip():
				flag = 1
			elif "small" in columns[lst[category]].strip():
				flag = 0


	#dctCounter = Counter(dct.values())
	'''
	print len(uniList)
	print len(list(uniList))
	print counter
	print len(dct)
	'''
	return flag



def  mapUnis(uniList):
	dct = {}
	counter = 0
	lst = {"id":0,"size":1,"ranking":2,"school":3,"confessionPage":4,"population":5,"tuition":6,"isReligious":7,"state":8,"region":9,"politics":10}
	for line in uniList:

		columns = line.split("|")
		school = columns[3]
		if "\xc2\xa0" in school:
			school = school.split("\xc2\xa0")[0]

		#school = correct(school)
		
		if "politics" in category:
			if "R" in columns[lst[category]].strip():
				dct[school] = 1

			elif "D" in columns[lst[category]].strip():
				dct[school] = 0

		elif "tuition" in category:
			if "State" in columns[lst[category]].strip():
				dct[school] = 1
			else:
				dct[school] = 0

		elif "isReligious" in category:
			if "None" not in columns[lst[category]].strip():
				dct[school] = 1
				
			else:
				dct[school] = 0

		elif "size" in category:
			#print lst[category]
			#print columns[lst[category]]
			if "top" in columns[lst[category]].strip():
				dct[school] = 1
			elif "small" in columns[lst[category]].strip():
				dct[school] = 0


	#dctCounter = Counter(dct.values())
	'''
	print len(uniList)
	print len(list(uniList))
	print counter
	print len(dct)
	'''
	return dct
def  mapUnis(uniList):
	dct = {}
	counter = 0
	lst = {"id":0,"size":1,"ranking":2,"school":3,"confessionPage":4,"population":5,"tuition":6,"isReligious":7,"state":8,"region":9,"politics":10}
	for line in uniList:

		columns = line.split("|")
		school = columns[3]
		if "\xc2\xa0" in school:
			school = school.split("\xc2\xa0")[0]

		#school = correct(school)
		
		if "politics" in category:
			if "R" in columns[lst[category]].strip():
				dct[school] = 1

			elif "D" in columns[lst[category]].strip():
				dct[school] = 0

		elif "tuition" in category:
			if "State" in columns[lst[category]].strip():
				dct[school] = 1
			else:
				dct[school] = 0

		elif "isReligious" in category:
			if "None" not in columns[lst[category]].strip():
				dct[school] = 1
				
			else:
				dct[school] = 0

		elif "size" in category:
			#print lst[category]
			#print columns[lst[category]]
			if "top" in columns[lst[category]].strip():
				dct[school] = 1
			elif "small" in columns[lst[category]].strip():
				dct[school] = 0


	#dctCounter = Counter(dct.values())
	'''
	print len(uniList)
	print len(list(uniList))
	print counter
	print len(dct)
	'''
	return dct

def cleanUniList():
	
	counter = 0
	schools = []
	scrapedUnis = open("lenPosts.dat").readlines()
	extractList = []
	lines = []
	uniList = []
	for uni in scrapedUnis:
		uniList += [uni.split(":")[0]]

	allUnis = open("Excel_Data/FCBCollegeList.csv").readlines()
	for line in allUnis[1:]:
		columns = line.split("|")
		school = columns[3]
		schools += [school.split("\xc2\xa0")[0]]
		flag = 0

		if "\xa0" in school:
			school = school.strip("\xa0")
		if "\xc2" in school:
			school = school.strip("\xc2")
		if "\xc2\xa01" in school:
		    school = school.strip("\xc2\xa01")
		if "\xef" in school:
			school = school.split("\xef")[0]
		#if "Northwestern" in line or "Wisconsin" in line or "Rensselaer" in line:
		#	counter += 1
		#	flag = 1
		#	lines += [line]
		#	extractList += [school]
		#	break
		for aSchool in uniList:
			if school in aSchool :
				#or "Northwestern" in aSchool or "Wisconsin" in aSchool or "Rensselaer" in aSchool:
				counter += 1
				flag = 1
				lines += [line]
				extractList += [school]
				break

		if flag == 0:
			continue
    	
	#return uniList, lines, extractList
	return lines

def cleanUniDict():
	
	counter = 0
	schools = []
	scrapedUnis = open("lenPosts.dat").readlines()
	extractList = []
	lines = []
	uniList = []
	unis = {}
	for uni in scrapedUnis:
		uni = uni.split(":")[0]
		uniList += [uni]



	allUnis = open("Excel_Data/FCBCollegeList.csv").readlines()
	for line in allUnis[1:]:
		columns = line.split("|")
		school = columns[3]
		schools += [school.split("\xc2\xa0")[0]]
		flag = 0

		if "\xa0" in school:
			school = school.strip("\xa0")
		if "\xc2" in school:
			school = school.strip("\xc2")
		if "\xc2\xa01" in school:
		    school = school.strip("\xc2\xa01")
		if "\xef" in school:
			school = school.split("\xef")[0]
		#if "Northwestern" in line or "Wisconsin" in line or "Rensselaer" in line:
		#	counter += 1
		#	flag = 1
		#	lines += [line]
		#	extractList += [school]
		#	break
	
		for aSchool in uniList:
			if school in aSchool :
				#or "Northwestern" in aSchool or "Wisconsin" in aSchool or "Rensselaer" in aSchool:
				counter += 1
				flag = 1
				uniDict = {}
				cols = line.split("|")
				uniDict["category"] = cols[1]
				uniDict["rank"] = cols[2]
				uniDict["size"] = cols[5]
				uniDict["tuition"] = cols[6]
				if "None" in cols[7]:
					uniDict["isReligious"] = "No"
				else:
					uniDict["isReligious"] = "Yes"
				uniDict["state"] = cols[8]
				#uniDict["politics"] = cols[9]
				if "D" in cols[10]:
					uniDict["politics"] = "Blue"
				elif "R" in cols[10]:
					uniDict["politics"] = "Red"
				unis[aSchool] = uniDict
				lines += [line]
				extractList += [school]
				break

		if flag == 0:
			continue
    	
	#return uniList, lines, extractList
	return unis
def mapUniDict(uni):
	dct = cleanUniDict()
	return dct[uni]
#full = cleanUniList()
#print mapUnis(full, "size")
