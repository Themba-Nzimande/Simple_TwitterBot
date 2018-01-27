import tweepy as tp
import time
import os

# Twitter API creds
consumer_key = 'XyBFRRLJZd3OjPz2iP7ThrxTh'
consumer_secret = 'Px8eS9p3tZtXYfckr3TPKciVNGfkoBjQHK1XiXkJp8qpsKiu8o'
access_token = '957203182475759616-W0prNVQjitTr7WOTEtP7STrYJXwBKae'
access_secret = 'euGBXajTSEiVTuxnNxvFZRwoDLEg1bawjSa3bD8pyxqMI'

#Login in dat ish
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

tweet = 'Hello, world and a SPECIAL Hello to BLACK TWIITER, the best thing to happen to twitter'
api.update_status(status=tweet)


os.chdir('models')

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(3)
