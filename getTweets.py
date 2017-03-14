import twitter

api = twitter.Api()
statuses = api.GetUserTimeline(26257166)
print([s.text for s in statuses])
