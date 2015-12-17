import urllib
import urllib2
import json
from pprint import pprint
import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
import unirest
'''
url = "https://sentinelprojects-skyttle20.p.mashape.com/"
text = "We have visited this restaurant a few times in the past, and the meals have been ok, but this time we were deeply disappointed."
opener = urllib2.build_opener(urllib2.HTTPHandler)
params = {'text': text, 'lang': 'en', 'keywords': 1, 'sentiment': 1, 'annotate': 0}
headers = {'X-Mashape-Authorization': 'JmyxsqBRMVLozvuNSosTNs5OlYWY0FQV'} 
request = urllib2.Request(url, urllib.urlencode(params), headers=headers)
response = opener.open(request)
opener.close()
data = json.loads(response.read())
pprint(data)
'''

response = unirest.post("https://sentinelprojects-skyttle20.p.mashape.com/",
  
  headers={
    "X-Mashape-Authorization": "Zw2BqqzTBY5lamDWN77VhRXimfDa3VLl"
  },
  params={ 
    "text": "[\"We have visited this restaurant a few times in the past\",\"and the meals have been ok\",\"but this time we were deeply disappointed.\"]",
    "lang": "en",
    "keywords": 1,
    "sentiment": 1,
    "annotate": 0
  }
);
#data = json.loads(response.read())
print response.body


