import tweepy
from textblob import TextBlob


consumer_key= 'WLRqE8EZbJ064jlAZgoAcuJ9V'
consumer_secret= '1GZ6HHPBULXInFdsfRJWi6lyycOowujglOy3TZj2wx5RZy3noh'

access_token='1172982543219478528-hO0mmdBXpKUlFaVoH16feWxhC1TxzP'
access_token_secret='2A8swDTb0S5fwW8xGogybVh4YrMxZdEovRjMTxQGBkaPI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Chandrayaan')


for tweet in public_tweets:
    print(tweet.text)
    

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
