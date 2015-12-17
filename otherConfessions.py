import re
import urllib2
from BeautifulSoup import BeautifulSoup

# Only scraping first confession boards
lines = open("FCB.dat").readlines()
page_ids = []
notFound = []
#dictionary1 = {}
#dictionary2 = {}
for line in lines:
	values = line.split("\n")[0].split("\t")
	
	if "facebook" in values[4]:
		ids = values[4].rsplit('/',1)[1]
		if re.search(r'\d+$', values[4]) is not None and ids.isdigit():
			if "?" in ids:
				ids = ids.split("?")[0]
			page_ids.append( int(ids))
			#dictionary1.setdefault(values[2].strip("\xc2\xa0"),[]).append(values[3].strip())
		else:
		
			if "http:" in values[4]:
				path = values[4].split("http://www").pop()
			elif "https:" in values[3]:
				path = values[4].split("https://www").pop()
			path = "http://graph"+path
			try:
				text = urllib2.urlopen(path).read().split(",")[0].split(":").pop()
				ids = re.findall('"([^"]*)"',text)[0]
		
				page_ids.append( int(ids))
			except Exception,e:
				notFound.append(path)
	
			#dictionary2.setdefault(values[2].strip("\xc2\xa0"),[]).append(values[3].strip())
#print dictionary1.values()
#print dictionary2
broken = ['http://graph.facebook.com/UPennEdufess', 'http://graph.facebook.com/VirginiaConfessions', 'http://graph.facebook.com/YaleEdufess','http://graph.facebook.com/UmichMemes', 'http://graph.facebook.com/UniversityOfDelawareConfessions', 'http://graph.facebook.com/UFEdufess','http://graph.facebook.com/PrincetonEdufess','https://www.facebook.com/ColumbiaEdufess','https://www.facebook.com/bostonik']

static = ['http://graph.facebook.com/UGAConfessions','http://graph.facebook.com/MuhlenbergCollegeConfessions']
#notFound = list(set(notFound) - set(broken) - set(static))
print page_ids
print notFound

