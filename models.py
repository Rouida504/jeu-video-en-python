# contenant les classes pour les personnages et les monstres 
# faire une classe pour personnage ( nom ,l’attaque, la défense et les points de vie )
class Personnage:
    def __init__(self,nom, attaque , defense , pv):
        self.nom = nom
        self.attaque = attaque
        self.defense  = defense
        self.pv = pv

  # on verifier s'il est tjr  vivant 
    def est_vivant(self):
        return self.pv > 0

# aussi pour les monstres ( nom, l’attaque, la défense et les points de vie)
class Monstres : 
    def __init__(self,nom, attaque, defense , pv):
         self.nom = nom
         self.attaque = attaque
         self.defense  = defense
         self.pv = pv 

  # on verifier s'il est tjr vivant 
    def est_vivant(self):
        return self.pv > 0