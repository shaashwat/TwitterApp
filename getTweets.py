import twitter

api = twitter.Api(consumer_key="iFM83lSHaysa7GTHbGRYOUHbH",
                  consumer_secret = "FgcO8CrxEYedFWUjn43aChntaspJV5FPbQamCI4Dp6R5ovQoT0",
                  access_token_key="722173364396298240-UnOQ1uZiwAETRNy5Jh4V8vWGh2JazPC",
                  access_token_secret="xgPt5BwXLziBBzMZb4fsYl8d7lZRP4iL5ainlvMhX3mug"
                  )

#status = api.PostUpdate('I love python-twitter!')
#print(status.text)

statuses = api.GetUserTimeline(user_id=26257166, count=100)
print([s.text for s in statuses])

#user = api.GetUser(user_id=26257166)