import json

import tweepy as tweepy
from django.db.models.signals import post_save
from django.dispatch import receiver

from .follower_data import FollowerModel
from .followers import Followers
from .tweets import Tweets


def credentials():
    twitter_auth_keys = {
        "consumer_key": "pjPwFYuSiqvfStZLCC6hB4Qwu",
        "consumer_secret": "dsxlqR7Xx2U0NzAjbttdHDlFnShgpJge7LbftA0x6OQEl4h1ED",
        "access_token": "1496475057119547407-pUeMwObKPoC23Qh8JjK13nqa9k3VVm",
        "access_token_secret": "wXYK9VqeAkvW9zgaObNZqms3DV4TIfoqj4CHbCoUXJUyN"
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)
    return api

def save_followers(followersList, iteracion, screen_name):
    if (iteracion == 6):
        return
    for follower in followersList:
        follower = follower._json
        print(follower["screen_name"])
        follow_model = FollowerModel.objects.create(screem_name=follower["screen_name"],follower_count=follower["followers_count"], screen_name_base=screen_name)
        follow_model.save()
        api = credentials()
        followersListSend = api.get_followers(screen_name='@'+follower["screen_name"], count='10')
        save_followers(followersListSend, (iteracion + 1), follower["screen_name"])


@receiver(post_save, sender=Tweets)
def tweet_post(sender, instance, **kwargs):
    
    api = credentials()

    try:
        api.verify_credentials()
        print('Successful Authentication')
    except:
        print('Failed authentication')
    tweet = instance.title + '\n' + Tweets.get_absolute_url(instance) 
    
    try:
        ##api.update_status(status=tweet) not posible, permisos read only
        ##Profile.objects.create(user=instance)
        print('Gracias')
    except tweepy.TweepyException as error:
        if error:
            print(error)

@receiver(post_save, sender=Followers)
def follower_list(sender, instance, **kwargs):
    api = credentials()
    try:
        api.verify_credentials()
        print('Successful Authentication')
    except:
        print('Failed authentication')
    try:
        followers = api.get_followers(screen_name=instance.screen_name_base, count='10')
        save_followers(followers, 0, instance.screen_name_base)  
        
    except tweepy.TweepyException as error:
        if error:
            print(error)
    