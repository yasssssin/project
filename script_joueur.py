import numpy as np
import random as r
#heritage postes joueur attaquant defenseur
#Classe mère joeurs
class Joueur:
    def __init__(self,nom):
        self.nom=nom
        self.butsmarques=0
        self.note=0 #note initale sur 10
        # rajouter des postes pour plus de realisme

    def evol_buts(self,nb_buts):
        self.butsmarques+=nb_buts
# classe definie finalement dans la classe fille
    def evol_notejoueur(self,resultat):
        pass
#Accesseurs
    def get_nom(self):
        return self.nom

    def get_buts_marques(self):
        return self.butsmarques

    def get_note(self):
        return self.note


# classes filles on ne definie ici que la methode de evolnotejoueurs
class Attaquant(Joueur) :
    def __init__(self,nom):
        super().__init__(self)
        #deux notes une d'attaque et une de defense
        self.note_att=r.randint(7,9)
        self.note_def=r.randint(3,5)
        self.note=(self.note_def+self.note_att)/2
    #on evolue la note des joeurs en fonction de si ce sont des attaquants on augmente leur note si ils ont marque plein de buts
    def evol_notejoueur(self,resultat):
        if resultat[0]>=1 and self.note_att<10:
            self.note_att+=0.5*r.randint(0,1)
        elif resultat[0]<=1 and self.note_att>0:
            self.note_att+=0.5*r.randint(-1,0)


class Defenseur(Joueur):
    def __init__(self,nom):
        super().__init__(nom)
        self.note_att=r.randint(3,5)
        self.note_def=r.randint(7,9)
        self.note=(self.note_def+self.note_att)/2

    # on evolue la note des joeurs en fonction de si ce sont des defenseurs on augmente leur notes si ils ont par pris beaucoup de buts
    def evol_notejoueur(self,resultat):
        if resultat[1] >= 2 and self.note_def>0:
            self.note_def += 0.5 * r.randint(-1, 0)
        if resultat[1] < 2 and self.note_def<0:
            self.note_def += 0.5 * r.randint(0, 1)