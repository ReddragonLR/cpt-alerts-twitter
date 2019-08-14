import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamListener

import twitter_credentials

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':

    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)
    stream.filter(follow=[twitter_credentials.CITY_OF_CAPE_TOWN_TWITTER_ID])