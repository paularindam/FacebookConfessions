import os

def notAlchemized():
	path = "/Users/arindam/AllAlchemy/"
	files = os.listdir(path)
	lst = []
	for aFile in files:
		content = open(path+aFile).read()
		if "}" not in content:
			lst += [aFile]

	return lst
