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
        for i in range(11):
            if resultat=='D':
                self.joueur[i]+=r.randint(-1,0)
            elif resultat=='N':
                self.joueur[i]+=r.randint(-1,1)
            else:
                self.joueur[i]+=r.randint(0,1)
        self.evol_noteclub()
