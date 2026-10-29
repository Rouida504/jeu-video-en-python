# gérant la logique du combat
import utils 
import models
import random

from utils import monstres_collection,scores_collection



# on choisi un monstre 
def choisir_monstre():
    liste = list(monstres_collection.find())
    donnees = random.choice(liste)
    return choisir_monstre

# On calcule les degats en tenant compte de la defense du monstre
def calcule_les_degats(attaque, defense):
    degats = attaque - defense
    if degats < 1:
        degats = 1
    return degats

# on lance le combat 
def lancer_le_combat():
     return
     

# On verifie si le monstre est mort s'il est mort l'equipe gagne si non il attaque un personnage vivant au hasard 
def verifier_la_mort_du_monstre():

     
# on calcule les dégâts de  monstre sur l'héros
def tour_du_monstre():
    victime = []
    for h in equipe:
     if h["pv"] > 0:
      if not victime:
        return



# On verifie si toute l’equipe est vaincue
def verifier_equipe_vaincue():
    return 



# affiche le score final 
def scores_final():
    scores = list(scores_collection.find())
    return scores

# afficher le classement 
def afficher_le_classement():
    top = list=(scores_collection.find())
    print("classement")
    
# On affiche les trois meilleurs scores
def affiche_les_trois_meilleurs_scores():
    scores = list(scores_collection.find())
    return scores







