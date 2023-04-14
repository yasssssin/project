import numpy as np
import random as r

class Joueur:

    def __init__(self,nom):
        self.nom=nom
        self.butsmarqués=0
        self.note=r.randint(5,8) #note initale sur 10

    def evol_buts(self,nb_buts):
        self.butsmarqués+=nb_buts
