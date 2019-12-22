import csv
import os


def dossier():
    os.chdir("Google Drive\Python\Twitter HAVP\Twitter-HAVP")

dossier()
Dico = {}    
Liste =[]
i=0
with open("liste.csv","r") as file:
    reader = csv.DictReader(file,delimiter = ";")
    for row in reader :
        i = i+1
        print(i)
        Liste.append(dict(row))