"""-It begins by asking the user to enter a URL (e.g. http://www.northwestern.edu),
    complete with the http:// prefix. Don't forget that prefix when entering a URL.
-It then goes to that website and gets the contents of the website as a string.
-Next, it goes through that string and separates out the individual words into a list.
-The list of words is then "cleaned" by removing frequently occurring uninteresting words
    (e.g. "a", "the", "I", etc.) and removing punctuation.
    The best way to do this is to maintain a list of words called a "stop list"
    and remove all words from your text that occur in that list.
-The remaining set of words is "stemmed" so that words such as
    "jog", "jogs", "jogging", "jogger", "jogged", etc. are all just transformed to "jog". Y
    you will need to think about how to do this effectively. It's impossible to do it perfectly, but for this milestone just try to do a reasonable job.
-The words are then counted to determine their frequency.
-A string is returned that contains the words sorted from most
    frequently to least frequently occurring, with the number of occurrences
    following each word (in parentheses). In order to avoid displaying too many words,
    there should be a global variable in your program called MAXWORDS. This global variable
    dictates the number of words that are returned. For example if MAXWORDS is set to 50,
    only the 50 most frequently occurring words will be returned.
-That string of the MAXWORDS most frequently occurring strings is
    printed on the screen. The words appear in order from most frequent
    to least frequent, with each word followed by the number of times it
    occurs (in parentheses). This is a simple version of a text cloud!"""

    
def extractText(text):

    a = text.split('\n')
    b = dePuncList(a)
    c = ' '.join(b)
    d = c.split(' ')
    e = []
    for ele in d:
    	if ele != '':
		e += [ele]
    return e


def dePunc( rawword ):
    """ de-punctuationifies the input string """
    L = [ c for c in rawword if 'A' <= c <= 'Z' or 'a' <= c <= 'z'  or c == ' ']
    # L is now a list of alphabetic characters
    L = [x for x in L if x != '']
    word = ''.join(L)   # this _strings_ the elements of L together
    return word

def dePuncList(L):
    c = []
    for i in L:
         c = c + [dePunc(i)]
    return c

def clean(URL):
    """takes out common words and empty spaces from text"""
    c = []
    stopList = ['',' ','i','the','a']
    for i in getText(URL):
        if i not in stopList:
            c = c + [i]
    return c

def stem(URL):
    """takes out suffixes from words"""
    suffixes = ['s','er','ing','ed','es','ers']
    h = []
    for i in clean(URL):
        for j in suffixes:
            if i.endswith(j):
                if i[len(i)-len(j)-2] == i[len(i)-len(j)-1]:
                    i = i[:-len(j)-1]
                
                else:    
                    i = i[:-len(j)]
        h = h + [i]
    return h

def countWords(URL):
    allWords= list(stem(URL)) #Defines new variable setWords, which is a list of the set of the list.
    setWords = list(set(allWords))
    #allWords is list of all words in the text except the stopwords. setWords is the list of unique words
    dictionary = {}
    for word in setWords: # We use counters to count the number of times each word appears. So, here we are initializing the counters to 0
        dictionary [word] =0#Now i guess it would make sense
    for word in allWords:
        if word in dictionary.keys():
            dictionary[word]+=1 #Creates a dictionary displaying the number of times each word appears in the list.
        else:
            dictionary[word]=1 
    return sorted(dictionary.items(), key=lambda x: x[1], reverse = True)
    

	

MAXWORDS = 50


    
