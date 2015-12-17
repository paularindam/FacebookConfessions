import requests
import json
def alchemyCallsLeft(ALCHEMY_KEY):
#ALCHEMY_KEY = "83a666ff5cabd33f153673e8e05d1162794ba9fc"
	URL = "http://access.alchemyapi.com/calls/info/GetAPIKeyInfo?apikey={}&outputMode=json".format(ALCHEMY_KEY)
	response = requests.get(URL)
	calls_left = json.loads(response.content)
	return int(int(calls_left['dailyTransactionLimit']) - int(calls_left['consumedDailyTransactions']))
	#return calls_left
def main():
	ALCHEMY_API_KEYS = ['83a666ff5cabd33f153673e8e05d1162794ba9fc','392cc0aa431acb0b53a89fe3647d5ba40ce28319','b13e3de000330123dff1f043f848af52e5134446', 'f3d930a5a9e53475f5fcbe4fae6a66e81d750819','4e940e22cc8996086b886b5f9eb5de037f7d0d6e']
	for key in ALCHEMY_API_KEYS:
		print "key "+str(key)+" :"+str(alchemyCallsLeft(key))

if __name__ == '__main__':
    main()
