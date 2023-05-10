import numpy as np
import random as r
#heritage postes joueur attaquant defenseur
class Joueur:

    def __init__(self,nom):
        self.nom=nom
        self.butsmarqués=0
        self.note=0 #note initale sur 10
        # rajouter des postes pour plus de réalisme

    def evol_buts(self,nb_buts):
        self.butsmarqués+=nb_buts
    def evol_notejoueur(self,resultat):
            pass

    def get_nom(self):
        return self.nom
    def get_buts_marqués(self):
        return self.butsmarqués
    def get_note(self):
        return self.note

class Attaquant(Joueur) :
    def __init__(self,nom):
        super().__init__(self,nom)
        self.note_att=r.randint(7,9)
        self.note_def=r.randint(3,5)
        self.note=(self.note_def+self.note_att)/2
    def evol_notejoueur(self,resultat):
        pass

class Defenseur(Joueur):
    def __init__(self,nom):
        super().__init__(self,nom)
        self.note_att=r.randint(3,5)
        self.note_def=r.randint(7,9)
        self.note=(self.note_def+self.note_att)/2
    def evol_notejoueur(self,resultat):
        pass