import numpy as np
import random as r
#heritage postes joueur attaquant defenseur
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
class Club:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs=[]
        for i in range (11):
            self.joueurs.append(Joueur(i))
        self.points = 0
        self.buts_marqués = 0
        self.noteclub=0

    def evol_noteclub(self): #evolution de la note cumulée des joueurs de l'équipe
        for elt in self.joueurs:
            self.noteclub=0
            self.noteclub+=elt.get_notejoueur #notejoueur définie dans la classe joueur

    def evol_points(self, points):
        self.points += points

    def evol_butsmarqués(self, buts):
        self.buts_marqués += buts

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)


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

class Match:
    def __init__(self, équipe_dom, équipe_ext):
        self.équipe_dom = équipe_dom
        self.équipe_ext = équipe_ext
        self.buts_dom = 0
        self.buts_ext = 0
        self.score = 0

    def jouer(self):

        import random

        A= self.équipe_dom.note_att_club - self.équipe_ext.note_def_club
        if A < 0:
            self.buts_dom = random.randint(0,1)
        if A == 0:
            self.buts_dom = random.randint(0, 2)
        if A > 0:
            self.buts_dom = int(random.randint(0, 10)*A/10)

        B = self.équipe_ext.note_att_club - self.équipe_dom.note_def_club
        if B < 0 :
            self.buts_ext = random.randint(0, 1)
        if B == 0:
            self.buts_ext = random.randint(0, 2)
        if B > 0:
            self.buts_ext = int(random.randint(0, 10) * B / 10)



        self.score = [self.buts_dom, self.buts_ext]

        self.équipe_dom.evol_butsmarqués(self.buts_dom)
        self.équipe_ext.evol_butsmarqués(self.buts_ext)

        if self.buts_dom > self.buts_ext:
            self.équipe_dom.evol_points(3)
        elif self.buts_dom == self.buts_ext:
            self.équipe_dom.evol_points(1)
            self.équipe_ext.evol_points(1)
        else:
            self.équipe_ext.evol_points(3)

        for joueur in self.équipe_dom.joueurs:
            joueur.evol_notejoueur(self.score)
        i=self.buts_dom
        for j in range(self.buts_dom):
            a=r.randint(0, 10)
            if a<6:
                a = r.randint(0, 10)
            self.équipe_dom.joueurs[a].evol_buts(1)
        for joueur in self.équipe_ext.joueurs:

            joueur.evol_notejoueur([self.score[1],self.score[0]])
        for j in range(self.buts_ext):
            a=r.randint(0, 10)
            if a<6:
                a = r.randint(0, 10)
            self.équipe_ext.joueurs[a].evol_buts(1)


        self.équipe_dom.evol_noteclub()
        self.équipe_ext.evol_noteclub()

    # Accesseurs
    def get_équipe_dom(self):
        return self.équipe_dom

    def get_équipe_ext(self):
        return self.équipe_ext

    def get_buts_dom(self):
        return self.buts_dom

    def get_buts_ext(self):
        return self.buts_ext

class Championnat:

    def __init__(self):
        self.clubs = []
        self.matches = []
        for k in Villes :
            self.clubs.append(Club(k))
    def planifier_matches(self):

        for i in range(len(self.clubs)):
            for j in range(i + 1, len(self.clubs)):
                match_aller = Match(self.clubs[i], self.clubs[j])
                match_retour = Match(self.clubs[j], self.clubs[i])
                self.matches.append(match_aller)
                self.matches.append(match_retour)

    def jouer_matches(self):
        for match in self.matches:
            match.jouer()
    def get_clubs(self):
        return self.clubs
