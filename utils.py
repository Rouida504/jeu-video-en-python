from pymongo import MongoClient

# La connexion avec mongodb
client = MongoClient("mongodb://localhost:27017/")

db = client["jeu_video"]

# On récupère la liste des personnages / monstres / scores
personnages_collection = db["personnages"]
monstres_collection = db["monstres"]
scores_collection = db["scores"]

# On affiche les persos dispo
def personnages_disponible():
    personnages = list(personnages_collection.find())
    return personnages

# On affiche les caractéristiques d'un monstre
# On affiche l'équipe choisie par le joueur
def afficher_choix_de_joueur():
    equipe = list(personnages_collection.find())
    return equipe

# On vérifie le choix du joueur
choix_du_joueur = True
if choix_du_joueur:
    print("Choix validé")
else:
    print("choix n'est pas validé ") 
    


# On affiche les trois meilleurs scores
def affiche_les_trois_meilleurs_scores():
   scores = scores_collection.find()
   return scores