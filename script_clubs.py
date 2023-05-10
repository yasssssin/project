import numpy as np
import random as r
import script_joueur


class Club:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs=[]
        for i in range (1,7):
            self.joueurs.append(script_joueur.Defenseur(i))
        for i in range(1,6):
            self.joueurs.append(script_joueur.Attaquant(i+6))
        self.points = 0
        self.buts_marqués = 0
        self.noteclub=0
        for elt in self.joueurs:
            self.noteclub+=elt.note
        self.note_att_club=0
        for elt in self.joueurs:
            self.note_att_club+=elt.note_att
            self.note_att_club=self.note_att_club/5
        self.note_def_club=0
        for elt in self.joueurs:
            self.noteclub+=elt.note_def
            self.note_def_club = self.note_def_club / 6

    def evol_noteclub(self): #evolution de la note cumulée des joueurs de l'équipe
        for elt in self.joueurs:
            self.noteclub+=elt.note #notejoueur définie dans la classe joueur

    def evol_points(self, points):
        self.points += points

    def evol_butsmarqués(self, buts):
        self.buts_marqués += buts



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












