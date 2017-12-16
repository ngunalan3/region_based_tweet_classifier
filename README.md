# region_based_tweet_classifier
Classify tweets from 5 different regions classify them into one of the 7 main topic categories and find out the topic that is trending the most in each region 

Python Library to fetch tweets CNN tweets from 5 different regions Asia, Africa, America, Europe and Australia along with the CNN homepage and classify those fetched tweets into 7 different topics and find out which topic is most popular and trending now in each region.

## Dependencies:

- nltk
- tweepy
- scikit-learn

## Usage:

First add your twitter api keys in the twc/tweet_classify.py file. (consumer_key, consumer_secret, access_token, access_token_secret) which can be generated from "https://apps.twitter.com"

```python
from twc import tweet_classify

#initialize the object
#Twitter id and no. of tweets to be classified
T = tweet_classify("nand_gun", 50)


#To find out the trending topics for each of the trend_names ["CNN","CNNASIA24","CNN_NewsGroupEU", "CNNALDUB_AUS","CNNAMERICA","CNNAFRICA"]
T.get_trends(sname=trend_name)

#classify the tweets topic wise 
#(Naive Bayes Classifier accuracy: 75%)
#(Multinomial Naive Bayes : 78%)
T.classify()
tweets_topic = T.topic_bucket

```

## Training Dataset and Model:

Dataset was created by fetching titles of different **subreddits** relating to 7 main following categories.

- technology 
- business
- politics
- entertainment
- sports
- health
- travel & lifestyle

---
To refresh the dataset with new headlines, run the script in dir ``twc/data/``:

``` bash
$ python3 test.py

```
To train the model again in ``twc/``
```bash
$ python3 train.py


```
To run the script
``` bash
$ python3 example.py

```

The classifier being used to train is ** Naive Bayes Classifier** with accuracy of 75% and ***MNB Classifier*** with 78%.
