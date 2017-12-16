import tweepy
import pickle
import nltk
import re
import requests

#classifier = pickle.load(open('twc/data/trained/NAIVE.pickle', 'rb'))
#classifier = pickle.load(open('/Users/nandhinigunalan/Documents/Coursera/Twitter-tweet-classifier-main/twc/data/trained/NAIVE.pickle', 'rb'))
classifier = pickle.load(open('/Users/nandhinigunalan/Documents/Coursera/Twitter-tweet-classifier-main/twc/data/trained/MNB.pickle', 'rb'))
word_features = pickle.load(open('/Users/nandhinigunalan/Documents/Coursera/Twitter-tweet-classifier-main/twc/data/trained/word_features.pickle', 'rb'))



def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

def tweet_clean(t):
		t = t.replace("#", "")
		t = t.replace("@", "")
		t = re.sub(r"[^\w\s]","",t)
		t = re.sub(" \d+", " ", t)
		return t


def is_actionable(t):
	t = tweet_clean(t)
	tags = [i[1] for i in nltk.pos_tag(t.split())]
	if len(t.split())>4:
		if 'NN' and 'VBD' or 'VB' in tags:
			return True
		else:
			False
	else:
		False


def predict_topic(s):
	s = tweet_clean(s)
	token = nltk.word_tokenize(s.lower())
	return classifier.classify(document_features(token))


class tweet_classify:
	def __init__(self, user,count=10):
		self.consumer_key = "***************************"
		self.consumer_secret = "************************"

		self.access_token = "**************************"
		self.access_token_secret = "********************"

		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret)

		self.count = count
		self.user = user

		self.tweets = []
		self.topic_bucket = {}


	def crawl(self):
		api = tweepy.API(self.auth)
		try:
			api = tweepy.API(self.auth)
			for status in tweepy.Cursor(api.user_timeline, retweets=True).items(self.count):
			#for status in tweepy.Cursor(api.followers, screen_name="nand_gun").items(self.count):
				self.tweets.append(status.text)
				#print("status text:")
		except Exception as e:
			print(e)

	def classify(self):
		for t in self.tweets:
			if is_actionable(t):
				topic = predict_topic(t)
				if self.topic_bucket.get(topic):
					self.topic_bucket[topic].append(t)
					
				else:
					self.topic_bucket[topic] = [t]	

	def get_trends(self,sname):

		api = tweepy.API(self.auth)
		#screen_name_collection = [ "CNN","CNNASIA24","CNN_NewsGroupEU","CNNALDUB_AUS","CNNAMERICA","CNNAFRICA"]

		tweet_results = []
		trends1 = api.user_timeline(screen_name=sname,count=self.count,trim_user=1,exclude_replies=1,tweet_mode="extended")
		#print(trends1)
		tweet_results.extend([tweet.full_text for tweet in trends1])
		
		self.tweets = tweet_results
		# print(tweet_results)
		# print("Completed")
    

if __name__=="__main__":
	t = tweet_classify("nand_gun", count=2)
	t.crawl()
	t.classify()
	t.get_trends()

	print(t.topic_bucket)
	print("*****************topic bucket*******************")

     

		
		

	
	
