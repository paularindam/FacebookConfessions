from processUnis import *
unis = open("FCBQuestions.csv").readlines()
uniPosts = unis[1:]
unis = []
fullList = revUnivCorrect(getScrapedUnis())
for uni in uniPosts:
	univ = uni.split("|")[3]
	unis += [univ]

unis = filter(None, list(set(unis)))
print "Here but not in scraped List", list(set(unis) - set(fullList))
print "In scraped list but not here",list(set(fullList)- set(unis))
