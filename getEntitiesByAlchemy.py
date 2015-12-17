from alchemyapi import AlchemyAPI
import json
import sys


def main ():
	demo_text = 'Yesterday dumb Bob destroyed my fancy iPhone in beautiful Denver, Colorado. I guess I will have to head over to the Apple Store and buy a new one.'
	#demo_text = open(sys.argv[1]).read()
	alchemyapi = AlchemyAPI()
	response = alchemyapi.entities('text',demo_text, { 'sentiment':1 })

	if response['status'] == 'OK':
		print('## Response Object ##')
		print(json.dumps(response, indent=4))


		print('')
		print('## Entities ##')
		for entity in response['entities']:
			print('text: ', entity['text'].encode('utf-8'))
			print('type: ', entity['type'])
			print('relevance: ', entity['relevance'])
			print('sentiment: ', entity['sentiment']['type'])
			if 'score' in entity['sentiment']:
				print('sentiment score: ' + entity['sentiment']['score'])
			print('')
	else:
		print('Error in entity extraction call: ', response['statusInfo'])


if __name__ == '__main__':
    main()

