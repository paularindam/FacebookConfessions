import os
import sys
import random
from getFeatures import *

ALCHEMY_API_KEY = "83a666ff5cabd33f153673e8e05d1162794ba9fc"
ALCHEMY_API_KEYS = ['392cc0aa431acb0b53a89fe3647d5ba40ce28319','b13e3de000330123dff1f043f848af52e5134446', 'f3d930a5a9e53475f5fcbe4fae6a66e81d750819','4e940e22cc8996086b886b5f9eb5de037f7d0d6e']

def notAlchemized(path):
	files = os.listdir(path)
	lst = []
	for aFile in files:
		content = open(path+aFile).read()
		if "}" not in content:
			lst += [aFile]

	return lst

def alchemize(post):
	text = quote(post)
	ALCHEMY_API_KEY = random.choice(ALCHEMY_API_KEYS)
	alchemy_taxonomy = fetch_alchemy_taxonomy(ALCHEMY_API_KEY, text)
	alchemy_entities = fetch_alchemy_entities(ALCHEMY_API_KEY, text)
	alchemy_concepts = fetch_alchemy_concepts(ALCHEMY_API_KEY, text)
	alchemy_keywords = fetch_alchemy_keywords(ALCHEMY_API_KEY, text)
	alchemy_categories = fetch_alchemy_categories(ALCHEMY_API_KEY, text)
	results = {}
	results['taxonomy'] = str(alchemy_taxonomy['taxonomy'])		        
	results['entities'] = str(alchemy_entities['entities'])
	results['concepts'] = str(alchemy_concepts['concepts'])
	results['keywords'] = str(alchemy_keywords['keywords'])
	results['categories'] = str(alchemy_categories)

	return results
#def alchemize(post):
#	print "here"
#	return []
def main():
	path = "/Users/arindam/"+sys.argv[1]
	fileList = os.listdir(path)
	alchemyPath = path+"Alchemy/"
	notDone = notAlchemized(alchemyPath)
	print notDone
	count = 0
	for fileName in notDone:
		if ".csv" not in fileName:
			continue
		count +=1
		originalFileName = path+"/"+fileName.replace("Alchemy","")
		#if alchemyPath+fileName.replace(".csv","Alchemy.csv") not in notDone:
		#	continue
		#else:
		#	print fileName
		#data = open(path+"/"+fileName).readlines()
		data = open(originalFileName).readlines()
		#newCSV = open(path+"Alchemy/"+fileName.replace(".csv","Alchemy.csv"),'w')
		newCSV = open(alchemyPath+fileName,'w')
		if len(data) < 1 :
			continue
		newCSV.write(data[0].strip()+"|taxonomy|entities|concepts|keywords|categories"+"\n")
		for row in data[1:]:
			if "|" in row:
				if "post" in fileName:
					post = row.split("|")[2]
				elif "comment" in fileName:
					post = row.split("|")[6]
				else:
					break
					
				if len(post)>140:
					try:
						results = alchemize(post)
						newCSV.write(row.strip()+"|"+results['taxonomy']+"|"+ results['entities']+"|"+results['concepts']+"|"+results['keywords']+"|"+results['categories']+"\n")
					except:
						newCSV.write(row.strip()+"|"+"|"+"|"+"|"+"|"+"\n")
				else:
					newCSV.write(row.strip()+"|"+"|"+"|"+"|"+"|"+"\n")
		newCSV.close()

	
if __name__ == '__main__':
    main()
