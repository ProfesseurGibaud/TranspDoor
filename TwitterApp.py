from twython import Twython
import json
import pandas as pd
import os

"""

Préambule

"""


def dossier():
    os.chdir("Google Drive//Python//TranspDoor")

dossier()

with open("twitter_credentials.json",'r') as file:
    creds = json.load(file)
    
twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])





user = 'CecilePrevieu'

query = {'q': 'Storengy',
        'user' : 'user',
        'count': 100
        }
        


# Search tweets


dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in twitter.search(**query)['statuses']:
    print(status['user']['screen_name'])
    if status['user']['screen_name'] == user:
        dict_2['user'].append(status['user']['screen_name'])
        dict_2['date'].append(status['created_at'])
        dict_2['text'].append(status['text'])
        dict_2['favorite_count'].append(status['favorite_count'])    

# Structure data in a pandas DataFrame for easier manipulation


df = pd.DataFrame(dict_2)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)

