from twython import Twython
import json

import os


def dossier():
    os.chdir("Google Drive//Python//TranspDoor")


with open("twitter_credentials.json",'r') as file:
    creds = json.load(file)
    
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])



query = {'q': 'learn python',
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        }
        


# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)









import time
from twython import TwythonStreamer

TERMS='social'

APP_KEY='MY APP KEY'
APP_SECRET='MY APP SECRET'
OAUTH_TOKEN='MY OATH TOKEN'
OAUTH_TOKEN_SECRET='MY OATH TOKEN SECRET'
FOLLOW  = "PREVIEU Cécile" #Personne d'intéret


class BlinkyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'].encode('utf-8'))
            
            
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS,follow = FOLLOW)
except:
    KeyboardInterrupt

