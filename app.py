import tweepy
import time
import random
   
auth = tweepy.OAuth1UserHandler(
      'CONSUMER_KEY',
      'CONSUMER_SECRET',
      'ACCESS_TOKEN',
      'ACCESS_TOKEN_SECRET'
    )

api = tweepy.API(auth)


client = tweepy.Client(
    "BEARER_TOKEN",
    "CONSUMER_KEY",
    "CONSUMER_SECRET",
    "ACCESS_TOKEN",
    "ACCESS_TOKEN_SECRET"
)


def __main__():
    f1 = api.media_upload(filename='fotos/1.jpg'); f2 = api.media_upload(filename="fotos/2.jpg")
    f3 = api.media_upload(filename="fotos/3.jpg"); f4 = api.media_upload(filename="fotos/4.jpg")
    f5 = api.media_upload(filename="fotos/5.jpg"); f6 = api.media_upload(filename="fotos/6.jpg")
    f7 = api.media_upload(filename="fotos/7.jpg"); f8 = api.media_upload(filename="fotos/8.jpg")
    f9 = api.media_upload(filename="fotos/9.jpg"); f10 = api.media_upload(filename="fotos/10.jpg")
    f11 = api.media_upload(filename="fotos/11.jpg"); f12 = api.media_upload(filename="fotos/12.jpg")
    f13 = api.media_upload(filename="fotos/13.jpg"); f14 = api.media_upload(filename="fotos/14.jpg")
    f15 = api.media_upload(filename="fotos/15.jpg"); f16 = api.media_upload(filename="fotos/16.jpg")
    f17 = api.media_upload(filename="fotos/17.jpg"); f18 = api.media_upload(filename="fotos/18.jpg")

    fotos = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18]

    a = random.randrange(18)

    
    try:
        tweet = client.create_tweet(media_ids=[fotos[a].media_id_string])
        print("Tweet enviado, foto ", a+1)
      
    except:
        print("Erro ao tweetar.")
    
   
while True:
   __main__()
   time.sleep(43200) #Um dia = 86400   12h = 43200