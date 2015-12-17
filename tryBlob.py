
from text.classifiers import NaiveBayesClassifier
from text.blob import TextBlob


train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
]
test = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]

print train[0]
print train[-1]
cl = NaiveBayesClassifier(train)
 
# Classify some text
print("Their burgers are amazing. :"+cl.classify("Their burgers are amazing."))  # "pos"
print("I don't like their pizza. :"+cl.classify("I don't like their pizza."))   # "neg"
 
# Classify a TextBlob
blob = TextBlob("The beer was amazing. But the hangover was horrible. "
                "My boss was not pleased.", classifier=cl)
print(blob)
print(blob.classify())
 
for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())
 
# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))
 
# Show 5 most informative features
cl.show_informative_features(5)
