import numpy as np
import random as r

class Joueur:

    def __init__(self,nom):
        self.nom=nom
        self.butsmarqués=0
        self.note=r.randint(5,8) #note initale sur 10
        # rajouter des postes pour plus de réalisme

    def evol_buts(self,nb_buts):
        self.butsmarqués+=nb_buts
    def evol_notejoueur(self,resultat):
            if resultat=='D':
                self.note=r.randint(-1,0)
            elif resultat=='N':
                self.note+=r.randint(-1,1)
            else:
                self.note+=r.randint(0,1)

    def get_nom(self):
        return self.nom
    def get_buts_marqués(self):
        return self.butsmarqués
    def get_note(self):
        return self.note
