import json

import tweepy
from decouple import config


def Auth_tweepy():
    auth = tweepy.OAuthHandler(config("API_KEY"),config("API_SECRETS"))
    auth.set_access_token(config("ACCES_TOKEN"),config("ACCES_SECRET"))

    return tweepy.API(auth)




