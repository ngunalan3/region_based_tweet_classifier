# categories: 
	# technology, 
	# business, 
	# politics, 
	# entertainment, 
	# sports, 
	# health
	# travel & lifestyle

import requests

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'en-US,en;q=0.8',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'}

def build_dataset(subtweet, topic):
	url = "https://www.reddit.com/r/{}/.json?limit=100".format(subtweet)
	#url = "https://www.twitter.com/r/{}/.json?limit=100".format(subtweet)

	r = requests.get(url, headers=headers)
	pre = open('raw/'+topic+".txt", 'r').read().split('\n')
	with open("raw/"+topic+'.txt', 'a') as f:
		for i in r.json()['data']['children']:
			i = i['data']['title']
			if i not in pre:
				print(i in pre)
				f.write(i+"\n")


subtweet = {
	#topic: [subtweet...]
	'technology': ['technology','gadgets','Technology_', 'tech'],
	'politics': ['politics','Indian_Politics','News_Politics'], 
	'business':['business','economy', 'InvestmentBanking123'],
	'entertainment':['entertainment', 'movies', 'hollywoodtime'],
	'sports':['sports', 'Cricket', 'football'],
	'health':['Health', 'publichealth'],
	'travel': ['travel','lifestyle','holiday','hotel']
}

for t in subtweet:
	for s in subtweet[t]:
		print("{}:{}".format(s, t))
		build_dataset(s, t)

