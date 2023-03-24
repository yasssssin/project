import numpy as np
import random as r

class club:
    def __init__(self,name):
        self.name=name
        self.joueur=[]
        self.noteclub=0
        for i in range(11):
            self.joueur.append(7)
        for elt in self.joueur:
            self.noteclub+=elt
    def evonoteclub(self):
        for elt in self.joueur:
            self.noteclub+=elt
    def evol(self,resultat):
        for i in range(11):
            if resultat=='D':
                self.joueur[i]+=r.randint(-1,0)
            elif resultat=='N':
                self.joueur[i]+=r.randint(-1,1)
            else:
                self.joueur[i]+=r.randint(0,1)
        self.evonoteclub()








