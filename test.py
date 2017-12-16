import pickle
import nltk


classifier = pickle.load(open('data/trained/NAIVE.pickle', 'rb'))
word_features = pickle.load(open('data/trained/word_features.pickle', 'rb'))

def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

def predict_topic(s):
	token = nltk.word_tokenize(s.lower())
	return classifier.classify(document_features(token))




topic = predict_topic("""Japan has an income-inequality problem, and it’s getting worse""")
print("""in test.py printing topic""")
print("Japan has an income-inequality problem, and it’s getting worse RESULT:"+topic)
#print(topic)
