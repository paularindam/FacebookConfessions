from nltk.corpus import stopwords
nltkStop = stopwords.words('english')
data = open("FCBPosts/Georgetown University:409149419153181posts.csv").readlines()
posts = []

myStop = ["me","it's","&","and","i'm","i'd", "i've","didn't"]
for i in range(10000):
	myStop += [str(i+1)]
	myStop += ['#'+str(i+1)+':']
stop = nltkStop + myStop

for row in data:
	posts += [row.split("|")[2]]

uniqueWords = []
for sentence in posts:
	uniqueWords +=  [i for i in sentence.lower().split() if i not in stop]
	uniqueWords = list(set(uniqueWords))

print uniqueWords
