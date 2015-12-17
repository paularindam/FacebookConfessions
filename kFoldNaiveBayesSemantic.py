import csv
import random
import sys
from text.classifiers import NaiveBayesClassifier
from text.blob import TextBlob

num_folds= int(sys.argv[2])
with open('myNUData2.csv', 'rU') as f:
    reader = csv.reader(f, delimiter='|', lineterminator='\r\n', quotechar='"', quoting=csv.QUOTE_NONE)
    aList = [[x.strip() for x in row] for row in reader]

#post 0,SlfRef 1 ,NU 2,MntlHlth 3,Wish/Want 4,Request 5,flame 6,joke 7,Gravity 8,Topic 9,TabooTopic 10,Identity 11,format 12
categories = {}
aList = aList[1:]
posts = []
for item in aList:
	posts += [[item[0]]+item[1:35:3]]

for i in range(len(posts)):
	post = posts[i]
	if "Y" in post[1]:
		categories.setdefault("SelfRef",[]).append(i)
	
	if "Y" in post[2]:
		categories.setdefault("NUMention",[]).append(i)

	
	if "Y" in post[3]:
		categories.setdefault("MentalHealth",[]).append(i)
	
	if "Y" in post[4]:
		categories.setdefault("WishWant",[]).append(i)

	if "Y" in post[5]:
		categories.setdefault("Request",[]).append(i)

	if "Y" in post[6]:
		categories.setdefault("Flaming",[]).append(i)

	if "Y" in post[7]:
		categories.setdefault("Joke",[]).append(i)

	if "N" in post[1]:
		categories.setdefault("NoSelfRef",[]).append(i)
	
	if "N" in post[2]:
		categories.setdefault("NoNUMention",[]).append(i)

	
	if "N" in post[3]:
		categories.setdefault("NoMentalHealth",[]).append(i)
	
	if "N" in post[4]:
		categories.setdefault("NoWishWant",[]).append(i)

	if "N" in post[5]:
		categories.setdefault("NoRequest",[]).append(i)

	if "N" in post[6]:
		categories.setdefault("NoFlaming",[]).append(i)

	if "N" in post[7]:
		categories.setdefault("NoJoke",[]).append(i)

	lstGravity = ["Superficial","Central","Core"]

	if "1" in post[8]:
		categories.setdefault("Superficial",[]).append(i)
	
	if "2" in post[8]:
	    categories.setdefault("Central",[]).append(i) 
	
	if "3" in post[8]:
	    categories.setdefault("Core",[]).append(i)  

	lstTopic = ["Romance", "Social","Academics","CollegeLife","Other"]

	if "R" in post[9]:
		categories.setdefault("Romance",[]).append(i)
	if "C" in post[9]:
		categories.setdefault("Social",[]).append(i)
	
	if "A" in post[9]:
		categories.setdefault("Academics",[]).append(i)
	
	if "L" in post[9]:
		categories.setdefault("CollegeLife",[]).append(i)
	
	if "O" in post[9]:
		categories.setdefault("Other",[]).append(i)

	lstTabooTopic = ["Sexual","Death","Body","Drug","Race"]

	if "S" in post[10]:
		categories.setdefault("Sexual",[]).append(i)

	if "D" in post[10]:
		categories.setdefault("Death",[]).append(i)
	
	if "E" in post[10]:
		categories.setdefault("Body",[]).append(i)
	
	if "U" in post[10]:
		categories.setdefault("Drug",[]).append(i)

	if "A" in post[10]:
		categories.setdefault("Race",[]).append(i)

	lstTabooIdentity = ["External","Character","Group"]
	if "E" in post[11]:
		categories.setdefault("External",[]).append(i)

	if "C" in post[11]:
		categories.setdefault("Character",[]).append(i)

	if "G" in post[11]:
		categories.setdefault("Group",[]).append(i)
	
	lstFormat = ["Criticism","Expression","Narrative"]

	if "T" in post[12]:
		categories.setdefault("Criticism",[]).append(i)

	if "E" in post[12]:
		categories.setdefault("Expression",[]).append(i)

	if "N" in post[12]:
		categories.setdefault("Narrative",[]).append(i)

#print categories['NUMention']
category = sys.argv[1]
f = open(sys.argv[2]+"fold"+category+".dat","w")
sys.stdout = f
binary = ["SelfRef","NUMention","MentalHealth","Request","WishWant","Flaming","Joke"]
data = []

if category not in binary :#or category not != "All":
	for i in range(len(posts)):
		string = unicode(posts[i][0], errors='ignore')
		
		if i in categories[category]:
			data += [(string,"pos")]
		else:
			data += [(string,"neg")]

else:

	oppcategory = "No"+category
	pos = neg = 0
	for i in range(len(posts)):
		string = unicode(posts[i][0], errors='ignore')
		if i in categories[category]:
			data += [(string,'pos')]
			#pos += 1
		elif i in categories[oppcategory]:
			#data += [(posts[i][0].decode('utf-8'),'neg')]
			data += [(string,'neg')]
				#neg += 1

random.shuffle(data)

#kFold Naive Bayes
subset_size = len(data)/num_folds
sumAccuracy = 0
cl = [0]*num_folds
for i in range(num_folds):
	test = data[i*subset_size:][:subset_size]
	train = data[:i*subset_size] + data[(i+1)*subset_size:]

	cl[i] = NaiveBayesClassifier(train)

	random.shuffle(test)
	random.shuffle(train)

	sumAccuracy += float("Accuracy: {0}".format(cl[i].accuracy(test)).split("Accuracy: ").pop())


print("Accuracy: "+str(sumAccuracy/10))
	#f.write("Accuracy: {0}".format(cl2.accuracy(test)))

for i in range(num_folds):

	cl[i].show_informative_features(2)








#idx till 36 multiples of 3
