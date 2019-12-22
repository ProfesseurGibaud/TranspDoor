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
        }
        


# Search tweets


dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in twitter.search(**query)['statuses']:
    print(status['user']['screen_name'])
    if status['user']['screen_name'] == user:
        dict_['user'].append(status['user']['screen_name'])
        dict_['date'].append(status['created_at'])
        dict_['text'].append(status['text'])
        dict_['favorite_count'].append(status['favorite_count'])    

# Structure data in a pandas DataFrame for easier manipulation


df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)



def Recherche(user,keyword,Date):
    query = {'q': keyword,'until' : Date}
    
    #Dictionnaire à modifier avec nom des users liés
    dict_ = {'user': [], 'date': [], 'text': []}
    for status in twitter.search(**query)['statuses']:
        print(status['user']['screen_name'])
        if status['user']['screen_name'] == user:
            dict_['user'].append(status['user']['screen_name'])
            dict_['date'].append(status['created_at'])
            dict_['text'].append(status['text'])
            
    
    # Structure data in a pandas DataFrame for easier manipulation
    
    
    df = pd.DataFrame(dict_)
    return df

user = "CecilePrevieu"
keyword = "Storengy"
Date = "2019-12-19"


"""

Nouvelle tentative (http://2017.compciv.org/guide/topics/python-nonstandard-libraries/twython-guide/twitter-twython-api-basics.html)

"""


result = twitter.show_user(screen_name='CecilePrevieu')