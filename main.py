# proposant le menu principal et gérant les interactions
import utils
import game
import random
from utils import personnages_collection

# Le menu principal
def main():
    while True:
        print("\n=== JEU DE COMBAT ===")
        print("1. Demarrer le jeu")
        print("2. Afficher le classement")
        print("3. Quitter")

        try:
            choix = int(input("Ton choix : "))
            
            if choix == 1:
                demarrer_le_jeu()
            elif choix == 2:
                game.afficher_le_classement()
            elif choix == 3:
                print("Au revoir !")
                break 
            else:
                print("Choix invalide faut choisir entre 1, 2 ou 3.")
        except ValueError:
            print(" il faut taper un chiffre ")


# Démarrer le jeu 
def demarrer_le_jeu():

#Demander le nom du joueur
    nom = input("Entre ton nom de joueur ")
    
# Afficher la liste des personnages disponibles depuis la base de données
def personnages_disponible():
    print("Personnages disponibles")
    personnages = list(personnages_collection.find())
    return
    

#  le joueur choisi 3 personnages pour l'equipe 
    
options = ["personnages_collection"]
choix_du_joueur = random.choice(options)
print("le joueur a choisi :", choix_du_joueur)

   
#  on lancer le combat avec le nom et l'équipe
print("Le combat commence")
game.lancer_le_combat(nom, equipe)


# Afficher la liste des personnages depuis la bdd
def afficher_liste_des_personnages():
    personnages = list(personnages_collection.find())
    return personnages


# Lancement du programme principal
if __name__ == "__main__":
    main()
