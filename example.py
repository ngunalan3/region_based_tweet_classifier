from twc import tweet_classify

import sys


T = tweet_classify( "nand_gun", 50)
screen_name = ["CNN","CNNASIA24","CNN_NewsGroupEU", "CNNALDUB_AUS","CNNAMERICA","CNNAFRICA"]

for trend_name in screen_name:
	classified_trend = {}
	T.get_trends(sname=trend_name)
	T.classify()
	
	for key,value in T.topic_bucket.items() :
		classified_trend[key] = len(value)
		#print(key+"----"+str(len(value)))
	
	sortedByValueDict = sorted(classified_trend.items(), key= lambda t:t[1], reverse=True)
	print(sortedByValueDict[0][0]+" is trending in "+trend_name)

