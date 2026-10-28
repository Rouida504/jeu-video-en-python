# insértion des personnages et monstres dans MongoDB
from utils import personnages_collection, monstres_collection, scores_collection

# on rajoute la liste de 10 personnes avec des caractéristiques prédéfinies (attaque, défense, points de vie)
personnages =[
 {"nom": "Guerrier" , "ATK": 24, "DEF": 8, "PV": 100},
 {"nom": "Druide" , "ATK": 21, "DEF": 9, "PV": 100},
 {"nom": "Archer" , "ATK": 26, "DEF": 7, "PV": 85},
 {"nom": "Voleur" , "ATK": 28, "DEF": 5, "PV": 80},
 {"nom": "Paladin" , "ATK": 20, "DEF": 12, "PV": 120},
 {"nom": "Sorcier" , "ATK": 32, "DEF": 4, "PV": 75},
 {"nom": "Chevalier" , "ATK": 22, "DEF": 10, "PV": 110},
 {"nom": "Moine" , "ATK": 22, "DEF": 9, "PV": 95},
 {"nom": "Berserker" ,"ATK": 29, "DEF": 6, "PV": 90},
 {"nom": "Chasseur" , "ATK": 23, "DEF": 8, "PV": 80},
]

# on rajoute la liste des monstres de plusieurs types 
monstres =[
 {"nom": "Gobelin", "ATK": 10, "DEF": 6, "pv": 150},
 {"nom": "Orc", "ATK": 10, "DEF": 8, "pv": 180},
 {"nom": "Dragon", "ATK": 10, "DEF": 12, "pv": 200},
 {"nom": "Zombie", "ATK": 10, "DEF": 7, "pv": 160},
 {"nom": "Troll", "ATK": 10, "DEF": 10, "pv": 190},
 {"nom": "Spectre", "ATK": 24, "DEF": 6, "pv": 170},
 {"nom": "Golem", "ATK": 21, "DEF": 14, "pv": 210},
 {"nom": "Vampire", "ATK": 26, "DEF": 9, "pv": 175},
 {"nom": "Loup-garou", "ATK": 24, "DEF": 8, "pv": 185},
 {"nom": "Squelette", "ATK": 19, "DEF": 7, "pv": 155},
]

# on rajoute la liste des scores 
scores = [
    {"joueur": "sdfgg", "score": 6},
    {"joueur": "Essayez 2", "score": 9},
    {"joueur": "Try3", "score": 6},
    {"joueur": "rme", "score": 10},
    {"joueur": "dsfgddf", "score": 35},
    {"joueur": "rme", "score": 14},
    {"joueur": "rme", "score": 54},
    {"joueur": "rme", "score": 51},
]
# on verifier si les personnage /les monstres n'existe pas deja pour eviter de faire les doublons 
personnages_inscrits = ["personnages_collection"]
if personnages_collection in personnages_inscrits:
    print("existe deja")
else:
    print("n'existe pas ")

# monstres
monstres_inscrits = ["monstres_collection"]
if monstres_collection in monstres_inscrits:
    print("existe deja ")
else:
    print(" n'existe pas ")

# enregistre ces données dans les collections correspondantes
print("personnages ,monstres sont pret ")
