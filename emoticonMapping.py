lines = open("Excel_Data/emoticons.csv").readlines()
emotSentiment = {'(:': 'Happy face (mirror)', ':o': '"Shock', ':-)': 'Happy face (with nose)', ':(': 'Sad face', ':)': 'Happy face', ':]': 'Happy face', ':D': 'Laugh', '=)': 'Happy face', ';D': 'Wink and grin', ':-(': 'Unhappy', 'XD': 'Big grin', '=(': 'Unhappy', '=D': 'Laugh', ':/': '"Uneasy', 'D:': 'Grin (mirror)', '=]': 'Happy face', ';)': 'Wink', ':P': 'Tongue out', '=/': '"Uneasy', ';-)': 'Wink (with nose)'}
'''
lines = lines[1:]
for line in lines:
	word = line.split(",")
	emotion = str(word[4]).strip("\r\n")
	emotSentiment[str(word[1])] = emotion

'''
print emotSentiment

