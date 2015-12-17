def correct(uni): #From excel to data csv
	
	if uni == 'Northwestern Univeristy':
		return "Northwestern"
	elif uni == 'University of Wisconsin--Madison':
		return "Wisconsin--Madison"
	elif uni == "Rensselaer Polytechnic Institute":
		return "RensselaerPolytechnicInstitute"
	elif ":" in uni:
		return uni.split(":")[0]
	else:
		return uni

def revCorrect(uni): #From data csv to excel

	if uni == "Northwestern":
		return 'Northwestern Univeristy'
	elif uni == "Wisconsin--Madison":
		return 'University of Wisconsin--Madison'
	elif uni == "RensselaerPolytechnicInstitute":
		return "Rensselaer Polytechnic Institute"
	elif ":" in uni:
		return uni.split(":")[0]
	else:
		return uni

def revUnivCorrect(lst): #Bulk version of revCorrect

	newLst = []
	for uni in lst:
		newLst += [revCorrect(uni)]
	return newLst

def univCorrect(lst): #Bulk version of correct
	
	newLst = []
	for uni in lst:
		newLst += [correct(uni)]
	return newLst
