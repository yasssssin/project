import numpy as np
import random as r


class club:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs=[]
        for i in range (11):
            self.joueurs.append(Joueur(i))
        self.points = 0
        self.buts_marqués = 0
        self.noteclub=0

#Accesseurs
    def get_nom(self):
        return self.nom
    def get_joueur(self):
        return self.joueurs
    def get_points(self):
        return self.points
    def get_buts_marqués(self):
        return self.buts_marqués
    def get_noteclub(self):
        return self.noteclub

    def evol_noteclub(self): #evolution de la note cumulée des joueurs de l'équipe
        for elt in self.joueurs:
            self.noteclub=0
            self.noteclub+=elt.get_notejoueur #notejoueur définie dans la classe joueur

    #à mettre dans la classe joueur
    def evol_notejoueur(self,resultat):
        for i in range(11):
            if resultat=='D':
                self.joueur[i]+=r.randint(-1,0)
            elif resultat=='N':
                self.joueur[i]+=r.randint(-1,1)
            else:
                self.joueur[i]+=r.randint(0,1)
        self.evol_noteclub()

    def evol_points(self, points):
        self.points += points

    def evol_butsmarqués(self, buts):
        self.buts_marqués += buts

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)




class championnat:
    def __init__(self,equipes):
        self.equipes=equipes












