from WhereStuffHappens import downloadTweets
from WhereStuffHappens import MarkovModel
import numpy as np
import twitter
import time

api = twitter.Api(consumer_key="iFM83lSHaysa7GTHbGRYOUHbH",
                  consumer_secret = "FgcO8CrxEYedFWUjn43aChntaspJV5FPbQamCI4Dp6R5ovQoT0",
                  access_token_key="722173364396298240-UnOQ1uZiwAETRNy5Jh4V8vWGh2JazPC",
                  access_token_secret="xgPt5BwXLziBBzMZb4fsYl8d7lZRP4iL5ainlvMhX3mug"
                  )

screenname = input('Enter Twitter Screen name here: ')


tweetsinfolist = downloadTweets.get_all_tweets(screenname)
arraytweets = np.array(tweetsinfolist)
tweetsList = arraytweets[:, 2]
tweets = ''.join(str(e) for e in tweetsList)
prediction = MarkovModel.create_markov_model(tweets)
print("You Tweeted: ")
predictionToTweet = prediction.replace("""'b'""", "")
print(predictionToTweet)
status = api.PostUpdate(predictionToTweet)
