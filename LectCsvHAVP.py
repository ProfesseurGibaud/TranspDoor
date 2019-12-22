import pandas as pd
import os
import pprint


def dossier():
    os.chdir("Google Drive//Python//TranspDoor")

def LoadData(i):
    if i == 0:
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        os.chdir("VuesFusionnes")
        dfAction = pd.read_csv("2_actions.csv",sep = ";")
        dfInfoGenerale = pd.read_csv("1_informations_generales.csv",sep = ";")
        os.chdir("..")
        dossier()
    if i == 1:
        dfInfoGenerale = pd.read_csv(r"C:\Users\François T\Desktop\Python\TranspDoor data\Vues fusionnées\1_informations_generales.csv",sep = ";")
        dfAction = pd.read_csv(r"C:\Users\François T\Desktop\Python\TranspDoor data\Vues fusionnées\2_actions.csv",sep = ";")
        
    return [DataInfoGenerale,DataAction]
dev = 1
LoadData(dev) 

cyloby = dfInfoGenerale[["denomination","nom_prenom_collaborateur"]].drop_duplicates() #Permet d'avoir une liste des lobbyists attachés à une entreprise