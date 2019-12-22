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

#Mot Clé, DateDebut, Date Din inutiles pour l'instant
def Recherche(user,MotCle,DateDebut,DateFin):
    NombreTweets = twitter.show_user(screen_name = "CecilePrevieu")["statuses_count"]
    if NombreTweets < 200:
        List = twitter.get_user_timeline(screen_name = user,count = NombreTweets + 1)
    if NombreTweets >= 200:
        compteur = NombreTweets
        while compteur >= 200:
            compteur = 0 #Fallait finir
        