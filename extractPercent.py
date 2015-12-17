from __future__ import division

def simplePercent(num, denom, asString = False):
	if num ==0 and asString == True:
		return " 0 %"
	elif num ==0 and asString == False:
		return 0
		
	percent = num/denom * 100

	if asString == False:
		return percent
	else:
		return str(percent) + " %"	

def percent(Dict, elem, denom, feature):
	
	num = Dict[elem]
	print feature, num, denom
	frac = str(num/denom * 100) + " %"	

	return frac

def relPercent(Dict1, Dict2, elem, denom, feature, flag = None):
	
	if flag == "actual":
		return percent(Dict1, elem, denom, feature)
	num = Dict1[elem]
	denom = Dict2[elem]
	print feature, num, denom
	if num ==0 and denom ==0:
		return 0
	frac = num/denom * 100	

	return frac

def strRelPercent(frac):
	frac = str(frac) + str (" %")
	return frac
def sumTOW(Dict):
	Sum = 0
	for key, value in sorted(Dict.items()):
		Sum += value

	return Sum


def percentTOW(Dict, elem, denom, feature):
	num = Dict[elem]
	if elem == "weekend":
		frac = str(num/denom * 100) + " %"
	#print feature, num, denom
	frac = str(num/denom * 100) + " %"	

	return frac
