#!/usr/bin/env python

#	Copyright 2013 AlchemyAPI
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import sys

demo_text = open(sys.argv[1]).read()

#Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()
#Entity Extraction
response = alchemyapi.entities('text',demo_text, { 'sentiment':1 })
fileName = sys.argv[1].replace(".txt",".dat")
f = open(fileName,'w')
if response['status'] == 'OK':

	for entity in response['entities']:
		f.write('text: '+ entity['text'].encode('utf-8'))
		f.write("\n")
		f.write('type: '+ entity['type'])
		f.write("\n")
		f.write('relevance: '+ entity['relevance'])
		f.write("\n")
		f.write('sentiment: '+ entity['sentiment']['type'])
		f.write("\n")
		if 'score' in entity['sentiment']:
			f.write('sentiment score: ' + entity['sentiment']['score'])
			f.write("\n")
		f.write('')
		f.write("\n")
else:
	f.write('Error in entity extraction call: '+ response['statusInfo'])
	f.write("\n")

'''
print('')
print('')
print('')
print('############################################')
print('#   Keyword Extraction Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.keywords('text',demo_text, { 'sentiment':1 })

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Keywords ##')
	for keyword in response['keywords']:
		print('text: ', keyword['text'].encode('utf-8'))
		print('relevance: ', keyword['relevance'])
		print('sentiment: ', keyword['sentiment']['type']) 
		if 'score' in keyword['sentiment']:
			print('sentiment score: ' + keyword['sentiment']['score'])
		print('')
else:
	print('Error in keyword extaction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Concept Tagging Example                #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.concepts('text',demo_text)

if response['status'] == 'OK':
	print('## Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Concepts ##')
	for concept in response['concepts']:
		print('text: ', concept['text'])
		print('relevance: ', concept['relevance'])
		print('')
else:
	print('Error in concept tagging call: ', response['statusInfo'])





print('')
print('')
print('')
print('############################################')
print('#   Targeted Sentiment Analysis Example    #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.sentiment_targeted('text',demo_text, 'Denver')

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))

	print('')
	print('## Targeted Sentiment ##')
	print('type: ', response['docSentiment']['type'])
	
	if 'score' in response['docSentiment']:
		print('score: ', response['docSentiment']['score'])
else:
	print('Error in targeted sentiment analysis call: ', response['statusInfo'])






print('')
print('')
print('')
print('############################################')
print('#   Language Detection Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.language('text',demo_text)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Language ##')
	print('language: ', response['language'])
	print('iso-639-1: ', response['iso-639-1'])
	print('native speakers: ', response['native-speakers'])
	print('')
else:
	print('Error in language detection call: ', response['statusInfo'])






print('')
print('')
print('')
print('############################################')
print('#   Relation Extraction Example            #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.relations('text',demo_text)

if response['status'] == 'OK':
	print('## Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Relations ##')
	for relation in response['relations']:
		if 'subject' in relation:
			print('Subject: ', relation['subject']['text'].encode('utf-8'))
		
		if 'action' in relation:
			print('Action: ', relation['action']['text'].encode('utf-8'))
		
		if 'object' in relation:
			print('Object: ', relation['object']['text'].encode('utf-8'))
		
		print('')
else:
	print('Error in relation extaction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Text Categorization Example            #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.category('text',demo_text)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Category ##')
	print('text: ', response['category'])
	print('score: ', response['score'])
	print('')
else:
	print('Error in text categorization call: ', response['statusInfo'])






'''
