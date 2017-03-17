from WhereStuffHappens import downloadTweets
from WhereStuffHappens import MarkovModel
import numpy as np
import os
#getTweets.get_tweets()
screenname = input('Enter Twitter Screen name here: ')
tweetsinfolist = downloadTweets.get_all_tweets(screenname)
arraytweets = np.array(tweetsinfolist)

tweets = arraytweets[:, 2]
tweetprediction = MarkovModel.create_markov_model(tweets)
