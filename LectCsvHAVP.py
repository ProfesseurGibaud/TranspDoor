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
        DataAction = pd.read_csv("2_actions.csv",sep = ";")
        DataInfoGenerale = pd.read_csv("1_informations_generales.csv",sep = ";")
        os.chdir("..")
        dossier()
    if i == 1:
        DataInfoGenerale = pd.read_csv(r"C:\Users\François T\Desktop\Python\TranspDoor data\Vues fusionnées\1_informations_generales.csv",sep = ";")
        DataAction = pd.read_csv(r"C:\Users\François T\Desktop\Python\TranspDoor data\Vues fusionnées\2_actions.csv",sep = ";")
        
    return [DataInfoGenerale,DataAction]
    
    