from twython import Twython
import json
import pandas as pd


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








"""
Sauvegarder Crédential


# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = "raTdGCpJFNyPTslBTSpkLw3bT"
credentials['CONSUMER_SECRET'] = "H96uO3hncAsbay8Z58rmdj7uD10g7vOHu6DS8sb2DEeD7VLfAO"
credentials['ACCESS_TOKEN'] = "785472099452321792-vR33rtbSpgUbQ2iGfA6mouKvCmd2JzR"
credentials['ACCESS_SECRET'] = "eeS0CDfriqvvVDmy2VFEWJd00tcO4ATbedESJQnfjxOcK"

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)
"""