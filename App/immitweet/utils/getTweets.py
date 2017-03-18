import os

import twitter

from WhereStuffHappens import MarkovModel

api = twitter.Api(consumer_key="iFM83lSHaysa7GTHbGRYOUHbH",
                  consumer_secret = "FgcO8CrxEYedFWUjn43aChntaspJV5FPbQamCI4Dp6R5ovQoT0",
                  access_token_key="722173364396298240-UnOQ1uZiwAETRNy5Jh4V8vWGh2JazPC",
                  access_token_secret="xgPt5BwXLziBBzMZb4fsYl8d7lZRP4iL5ainlvMhX3mug"
                  )


def get_tweets(screenname):
    statuses = api.GetUserTimeline(screen_name=screenname, count=300, exclude_replies=True)
    tweetsList = [s.text for s in statuses]
    tweets = ''.join(str(e) for e in tweetsList)
    file = open("DownloadedTweets.txt", "w")
    file.write(tweets)

    outputToTweet = MarkovModel.create_markov_model()
    os.remove("DownloadedTweets.txt")
    file.close()

    status = api.PostUpdate(outputToTweet)
    print(status.text)
