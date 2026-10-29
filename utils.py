# contenant les fonctions pour l'affichage et la gestion des données
from pymongo import MongoClient


# La connexion avec mongodb
client = MongoClient("mongodb://localhost:27017/")

db = client["jeu_video"]

# On récupère la liste des personnages / monstres / scores
personnages_collection = db["personnages"]
monstres_collection = db["monstres"]
scores_collection = db["scores"]

# On affiche les personnages dispo
def personnages_disponible():
    personnages = list(personnages_collection.find())
    return personnages

# On affiche les caractéristiques d'un monstre
def afficher_monstres():
    monstres =list(monstres_collection.find())
    return monstres


# On affiche l'équipe choisie par le joueur
def afficher_choix_de_joueur(equipe):
    print("votre equipe")
    return equipe

# On vérifie le choix du joueur
def verifier_le_choix_du_joueur():
 if verifier_le_choix_du_joueur:
     print("vous avez choisi 3 personnages ")
 else:
     print("vous devez choisi 3 personnages ")