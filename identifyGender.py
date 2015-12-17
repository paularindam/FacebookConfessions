#Credits to Iulia Cioroianu-PhD Student NYU 
#for major part of this code

import random
import nltk
import sys
from nltk.classify import apply_features


def identifyGender(Name):
	names = ([(name, 'male') for name in nltk.corpus.names.words('male.txt')] + [(name, 'female') for name in nltk.corpus.names.words('female.txt')])
	random.shuffle(names)
	featuresets = [(gender_features(n), g) for (n,g) in names]
	train_set = apply_features(gender_features, names)
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	gender = classifier.classify(gender_features(Name))
	return gender

def gender_features(word):
	return {'last_letter':word[-1]}

def main():
	print identifyGender(sys.argv[1])

if __name__ == '__main__':
	main()
