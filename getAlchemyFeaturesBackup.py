# Takes a URL, sends the request to three of Alchemy's API methods, and receives the entities,
# printing them to the screen and saving them to a file of the user's choice. To process a text
# file instead, you will have to change the base URLs to match the correct API methods.

import urllib2
import json
from pprint import pprint
from urllib import quote
import sys
import random
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

#ALCHEMY_API_KEYS = ['83a666ff5cabd33f153673e8e05d1162794ba9fc','392cc0aa431acb0b53a89fe3647d5ba40ce28319','b13e3de000330123dff1f043f848af52e5134446', 'f3d930a5a9e53475f5fcbe4fae6a66e81d750819','4e940e22cc8996086b886b5f9eb5de037f7d0d6e']

ALCHEMY_URL_KEYWORDS = 'http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?url=%(url)s&apikey=%(apikey)s&keywordExtractMode=%(mode)s&showSourceText=%(showSource)s&outputMode=json'
ALCHEMY_URL_CONCEPTS = 'http://access.alchemyapi.com/calls/url/URLGetRankedConcepts?url=%(url)s&apikey=%(apikey)s&showSourceText=%(showSource)s&outputMode=json'
ALCHEMY_URL_CATEGORY = 'http://access.alchemyapi.com/calls/url/URLGetCategory?url=%(url)s&apikey=%(apikey)s&showSourceText=%(showSource)s&outputMode=json'
ALCHEMY_URL_ENTITIES = 'http://access.alchemyapi.com/calls/url/URLGetRankedNamedEntities?url=%(url)s&apikey=%(apikey)s&showSourceText=%(showSource)s"ations=%(quotations)s&outputMode=json'
ALCHEMY_URL_TAXONOMY = 'http://access.alchemyapi.com/calls/url/URLGetRankedTaxonomy?url=%(url)s&apikey=%(apikey)s&&outputMode=json'
ALCHEMY_TEXT_TAXONOMY = 'http://access.alchemyapi.com/calls/text/TextGetRankedTaxonomy?apikey=%(apikey)s&text=%(text)s&outputMode=json'
ALCHEMY_TEXT_KEYWORDS = 'http://access.alchemyapi.com/calls/text/TextGetRankedKeywords?apikey=%(apikey)s&text=%(text)s&keywordExtractMode=%(mode)s&showSourceText=%(showSource)s&outputMode=json'
ALCHEMY_TEXT_CONCEPTS = 'http://access.alchemyapi.com/calls/text/TextGetRankedConcepts?apikey=%(apikey)s&text=%(text)s&showSourceText=%(showSource)s&outputMode=json'
ALCHEMY_TEXT_CATEGORY = 'http://access.alchemyapi.com/calls/text/TextGetCategory?apikey=%(apikey)s&text=%(text)s&showSourceText=%(showSource)s&outputMode=json'
ALCHEMY_TEXT_ENTITIES = 'http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities?apikey=%(apikey)s&text=%(text)s&showSourceText=%(showSource)s"ations=%(quotations)s&outputMode=json'
#http://access.alchemyapi.com/calls/text/TextGetRankedTaxonomy
def fetch_alchemy_taxonomy(ALCHEMY_API_KEY, text):
        print ALCHEMY_API_KEY

	r_taxonomy = urllib2.urlopen(ALCHEMY_TEXT_TAXONOMY % {'apikey': ALCHEMY_API_KEY, 'text': text})
        r_taxonomy = r_taxonomy.read()
        taxonomy = json.loads(r_taxonomy)
        print(taxonomy)
    	print "here"
        return taxonomy


def fetch_url_alchemy_entities(url, mode='normal', show_source=1,quotations=0):
    r_entities = urllib2.urlopen(ALCHEMY_URL_ENTITIES % {
        'url': url,
        'apikey': ALCHEMY_API_KEY,
        'mode': mode,
        'showSource': show_source,
        'quotations': quotations
    })
    r_entities = r_entities.read()
    entities = json.loads(r_entities)
    pprint(entities)
    return entities

def fetch_alchemy_entities(ALCHEMY_API_KEY, text, mode='normal', show_source=1,quotations=0):
    r_entities = urllib2.urlopen(ALCHEMY_TEXT_ENTITIES % {
    
        'apikey': ALCHEMY_API_KEY,
        'text': text,
        'mode': mode,
        'showSource': show_source,
        'quotations': quotations
    })
    r_entities = r_entities.read()
    entities = json.loads(r_entities)
    pprint(entities)
    return entities

def fetch_url_alchemy_concepts(url, mode='normal', show_source=1,quotations=0):
    r_concepts = urllib2.urlopen(ALCHEMY_URL_CONCEPTS % {
        'url': url,
        'apikey': ALCHEMY_API_KEY,
        'mode': mode,
        'showSource': 0,
        'quotations': quotations
    })
    r_concepts = r_concepts.read()
    concepts = json.loads(r_concepts)
    pprint(concepts)
    return concepts
def fetch_alchemy_concepts(ALCHEMY_API_KEY, text, mode='normal', show_source=1,quotations=0):
    r_concepts = urllib2.urlopen(ALCHEMY_TEXT_CONCEPTS % {
        'apikey': ALCHEMY_API_KEY,
        'text': text,
        'mode': mode,
        'showSource': 0,
        'quotations': quotations
    })
    r_concepts = r_concepts.read()
    concepts = json.loads(r_concepts)
    pprint(concepts)
    return concepts

def fetch_url_alchemy_keywords(url, mode='normal', show_source=1,quotations=0):
    r_keywords = urllib2.urlopen(ALCHEMY_URL_KEYWORDS % {
        'url': url,
        'apikey': ALCHEMY_API_KEY,
        'mode': mode,
        'showSource': 0,
        'quotations': quotations
    })
    r_keywords = r_keywords.read()
    keywords = json.loads(r_keywords)
    pprint(keywords)
    return keywords

def fetch_alchemy_keywords(ALCHEMY_API_KEY, text, mode='normal', show_source=1,quotations=0):
    r_keywords = urllib2.urlopen(ALCHEMY_TEXT_KEYWORDS % {
        'apikey': ALCHEMY_API_KEY,
        'text': text,
        'mode': mode,
        'showSource': 0,
        'quotations': quotations
    })
    r_keywords = r_keywords.read()
    keywords = json.loads(r_keywords)
    pprint(keywords)
    return keywords

def fetch_url_alchemy_categories(url, mode='normal', show_source=1,quotations=0):
    r_categories = urllib2.urlopen(ALCHEMY_URL_CATEGORY % {
        'url': url,
        'apikey': ALCHEMY_API_KEY,
        'mode': mode,
        'showSource': 0,
        'quotations': quotations
    })
    r_categories = r_categories.read()
    categories = json.loads(r_categories)
    pprint(categories)
    return categories

def fetch_alchemy_categories(ALCHEMY_API_KEY, text, mode='normal', show_source=1,quotations=0):
    r_categories = urllib2.urlopen(ALCHEMY_TEXT_CATEGORY % {
        'apikey': ALCHEMY_API_KEY,
        'text': text,
        'mode': mode,
        'showSource': 0,
        'quotations': quotations
    })
    r_categories = r_categories.read()
    categories = json.loads(r_categories)
    pprint(categories)
    return categories

def saveResults(results):
    newFileName=raw_input("Please enter a file name to save these results: ")
    with open(newFileName, 'w') as newFile:
        json.dump(results,newFile)

def main():
    lines = open(sys.argv[1]).readlines()
    for line in lines:
        #url=raw_input("What is the URL you wish to process? ")
        ALCHEMY_API_KEY = "83a666ff5cabd33f153673e8e05d1162794ba9fc"
        url = line.strip()
        demo_text = 'Yesterday dumb Bob destroyed my fancy iPhone in beautiful Denver, Colorado. I guess I will have to head over to the Apple Store and buy a new one.'
        text = 'Yesterday%20dumb%20Bob%20destroyed%20my%20fancy%20iPhone%20in%20beautiful%20Denver%2C%20Colorado.%20I%20guess%20I%20will%20have%20to%20head%20over%20to%20the%20Apple%20Store%20and%20buy%20a%20new%20one.'
        text = quote(line)
        #alchemy_taxonomy = fetch_alchemy_taxonomy(ALCHEMY_API_KEY, text)
        alchemy_entities = fetch_alchemy_entities(ALCHEMY_API_KEY, text)
        #alchemy_concepts = fetch_alchemy_concepts(ALCHEMY_API_KEY, text)
        #alchemy_keywords = fetch_alchemy_keywords(ALCHEMY_API_KEY, text)
        #alchemy_categories = fetch_alchemy_categories(ALCHEMY_API_KEY, text)
            
        #alchemy_entities = alchemyapi.entities('text',demo_text, { 'sentiment':1 })
        

        results = {}

        #results['taxonomy'] = alchemy_taxonomy['taxonomy']
        #print results['taxonomy']
        #results['entities'] = alchemy_taxonomy['entities']
        results['entities'] = alchemy_entities['entities']
        print results['entities']
        #results['concepts'] = alchemy_concepts['concepts']
        #print results['concepts']
        #results['keywords'] = alchemy_keywords['keywords']
        #print results['keywords']
        #results['categories'] = alchemy_categories['categories']
        #results['categories'] = alchemy_categories
        #print results['categories']
        


if __name__ == '__main__':
    main()

