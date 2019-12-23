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
        
    return [dfInfoGenerale,dfAction]

def prepare_data(dfInfoGenerale,dfAction):
    cyloby = dfInfoGenerale[["denomination","nom_prenom_collaborateur"]].drop_duplicates() #Permet d'avoir une liste des lobbyists attachés à une entreprise

    #Prépare une sous-liste des actions
    actionlob = dfAction[["denomination","date_premiere_publication","date_debut","date_fin","date_publication","date_publication_activite","objet_activite","domaines_intervention_actions_menees","action_menee","decision_concernee"]]

    return [cyloby, actionlob]


dev = 1
[dfInfoGenerale,dfAction] = LoadData(dev) 

[cyloby, actionlob] = prepare_data(dfInfoGenerale, dfAction)



#def ArbreEntrepriseCollab()
#    dict = {}
#    svg = ""
#    for item in cyloby.denomination:
#        if item != svg:
#            dict[item] = []
#            svg = item
#
#    for item in cyloby.iterrows():
#          dict[item[1][0]].append(item[1][1])
#    return dict
#    
#dict = ArbreEntrepriseCollab()
#
#
#
#
#
#for i in actionlob:
#    for j in cyloby:
#        if cyloby.denomination == actionlob.denomination:
#            actionlob.