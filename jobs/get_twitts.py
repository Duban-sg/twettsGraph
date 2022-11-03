from datetime import datetime

from .tweepy import auth_tweepy


def Get_twetts():
    try:
        api_tweepy = None
        tweets_json = []

        if(api_tweepy==None):
            api_tweepy = auth_tweepy.Auth_tweepy()
        
        if(api_tweepy):
            api_tweepy.verify_credentials()
            
            place = api_tweepy.search_geo(query="Colombia", granularity="country")
            place_id = place[0].id
            searchs = api_tweepy.search_tweets(q='place:%s' % place_id,geocode='10.46314,-73.253222,10km', count='2')
            for tweet in searchs:
                tweetJson = tweet._json
                tweets_json.append(tweetJson)
            print(tweets_json)

    except:
        print("Error problemas con la api")