#!/usr/bin/python
import tweepy
import cred_twitt as secrets


def tweet(message):
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)
    api = tweepy.API(auth)
    auth.secure = True
    print("Posting message {}".format(message))
    api.update_status(status=message)
