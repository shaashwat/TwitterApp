#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv

# Twitter API credentials
consumer_key = "iFM83lSHaysa7GTHbGRYOUHbH"
consumer_secret = "FgcO8CrxEYedFWUjn43aChntaspJV5FPbQamCI4Dp6R5ovQoT0"
access_key = "722173364396298240-UnOQ1uZiwAETRNy5Jh4V8vWGh2JazPC"
access_secret = "xgPt5BwXLziBBzMZb4fsYl8d7lZRP4iL5ainlvMhX3mug"


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print
        "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        "...%s tweets downloaded so far" % (len(alltweets))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    

    # write the csv
    #with open('%s_tweets.csv' % screen_name, 'w') as f:
    #    writer = csv.writer(f)
    #   writer.writerow(["id", "created_at", "text"])
    #    writer.writerows(outtweets)

    return outtweets