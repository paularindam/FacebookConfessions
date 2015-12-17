import os
import sys
import random
from getFeatures import *
from urllib import unquote
from dePunct import *
ALCHEMY_API_KEY = "83a666ff5cabd33f153673e8e05d1162794ba9fc"
#ALCHEMY_API_KEYS = ['392cc0aa431acb0b53a89fe3647d5ba40ce28319','b13e3de000330123dff1f043f848af52e5134446', 'f3d930a5a9e53475f5fcbe4fae6a66e81d750819','4e940e22cc8996086b886b5f9eb5de037f7d0d6e']

def notAlchemized(path):
	files = os.listdir(path)
	lst = []
	for aFile in files:
		content = open(path+aFile).read()
		if "}" not in content:
			lst += [aFile]

	return lst

def alchemize(text, fileName,path):

	
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
	para = ""
	newFileTaxonomy = path+ fileName.replace(".dat",para+"taxonomy.dat")
	newFileEntities = path + fileName.replace(".dat",para+"entities.dat")
	newFileConcepts = path + fileName.replace(".dat",para+"concepts.dat")
	newFileKeywords = path + fileName.replace(".dat",para+"keywords.dat")
	newFileCategories = path + fileName.replace(".dat",para+"categories.dat")

	g = open(newFileTaxonomy,'w')
	g.write(results['taxonomy'])
	g.close()

	g = open(newFileEntities,'w')
	g.write(results['entities'])
	g.close()

	g = open(newFileConcepts,'w')
	g.write(results['concepts'])
	g.close()

	g = open(newFileKeywords,'w')
	g.write(results['keywords'])
	g.close()

	g = open(newFileCategories,'w')
	g.write(results['categories'])
	g.close()
	
#def alchemize(post):
#	print "here"
#	return []
def main():
	path = "/Users/arindam/"+sys.argv[1]
	fileList = os.listdir(path)
	#alchemyPath = path+"Together/"
	#notDone = notAlchemized(alchemyPath)
	#print notDone
	count = 0
	for fileName in fileList:
		originalFileName = path+"/"+fileName
		data = open(originalFileName).readlines()
		text = ""
		for line in data:
			text += str(line)
		post = " ".join(extractText(text))
		#print results
		results = alchemize(quote(post),fileName, path+"Alchemy"+"/" )
		break
	
if __name__ == '__main__':
    main()
