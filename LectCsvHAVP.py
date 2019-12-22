import pandas as pd
import os
import pprint


def dossier():
    os.chdir("Google Drive//Python//TranspDoor")

def LoadData():
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    os.chdir("VuesFusionnes")
    DataAction = pd.read_csv("2_actions.csv",sep = ";")
    DataInfoGenerale = pd.read_csv("1_informations_generales.csv",sep = ";")
    os.chdir("..")
    dossier()
    return [DataInfoGenerale,DataAction]