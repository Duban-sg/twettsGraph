from datetime import datetime

from dateutil import parser

from authApp.models.tweets import Tweets

from .tweepy import auth_tweepy


def get_geo(geo_aray):
    try:
        geo_response = ""
        for item in geo_aray[0][0]:
            geo_response*= item
        return geo_response
    except Exception as inst:
        return '10.4645041,-73.2932692' #valledupar city

def save_twetts(tweetJson):
    try:
        geo= get_geo(tweetJson['place']['bounding_box']['coordinates'])
        create_date = parser.parse(tweetJson['created_at']).date()
        content= tweetJson['text']
        name= tweetJson['user']['screen_name']
        fav_count = tweetJson['favorite_count']
        ret_count= tweetJson['retweet_count']
        new_object = Tweets.objects.create(geo=geo,content=content,screen_name=name,favorite_count=fav_count,retweet_count=ret_count,create_at_twett=create_date)
        new_object.save()
    except Exception as inst:
        print("Error error bd: "+ str(inst))

def Get_twetts():
    try:
        api_tweepy = None

        if(api_tweepy==None):
            api_tweepy = auth_tweepy.Auth_tweepy()
        
        if(api_tweepy):
            api_tweepy.verify_credentials()
            
            place = api_tweepy.search_geo(query="Colombia", granularity="country")
            place_id = place[0].id
            searchs = api_tweepy.search_tweets(q='place:%s' % place_id,geocode='10.46314,-73.253222,10km', count='2')
            index = 0
            for tweet in searchs:
                tweetJson = tweet._json
                save_twetts(tweetJson)
    except Exception as inst:
        print("Error problemas con la api: "+ str(inst))
