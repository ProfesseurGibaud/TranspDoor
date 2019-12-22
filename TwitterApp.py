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





user = "CecilePrevieu"
keyword = "Storengy"
Date = "2019-12-19"

user = "MET_Token"

def ModifListe(L,item):
    L.append(item)
    return L

#Mot Clé, DateDebut, Date Din inutiles pour l'instant
def Recherche(user,MotCle,DateDebut,DateFin):
    NombreTweets = twitter.show_user(screen_name = user)["statuses_count"]
    compteur = NombreTweets
    Liste = []
    for tweet in twitter.get_user_timeline(screen_name = user,count = 200):
        Liste = ModifListe(Liste,tweet)
    
    last_id = Liste[len(Liste)-1]['id']
    
    while len(Liste) < NombreTweets:
        print(len(Liste))
        for item in twitter.get_user_timeline(screen_name = user,max_id = last_id,count = 199):
            print(item["lang"])
            Liste = ModifListe(Liste,item)
        last_id = Liste[len(Liste)-1]['id']
    
    return Liste 
        
        
   