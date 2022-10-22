import tweepy as tweepy
from django.db.models.signals import post_save
from django.dispatch import receiver

from .tweets import Tweets


@receiver(post_save, sender=Tweets)
def tweet_post(sender, instance, **kwargs):
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