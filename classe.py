import numpy as np
import random as r
import script_joueur


class Club:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs=[]
        #on ajoute 6 joueurs défensifs et 5 joueurs offensifs pour créer une équipe
        for i in range (1,7):
            self.joueurs.append(script_joueur.Defenseur(i))
        for i in range(1,6):
            self.joueurs.append(script_joueur.Attaquant(i+6))
        self.points = 0
        self.buts_marqués = 0
        self.noteclub=0
        #on définit la note du club comme la somme des notes des joueurs
        #et les notes d'attaque et de défense comme les moyennes des joueurs la composant
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
        self.noteclub=0
        for elt in self.joueurs:
            self.noteclub+=elt.note #notejoueur définie dans la classe joueur

    def evol_points(self, points):
        self.points += points

    def evol_butsmarqués(self, buts):
        self.buts_marqués += buts
    def __str__(self):
        return self.nom



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


import script_joueur
import script_championnat
import script_clubs
import random as r

class Match:
    def __init__(self, équipe_dom, équipe_ext):
        self.équipe_dom = équipe_dom
        self.équipe_ext = équipe_ext
        self.buts_dom = 0
        self.buts_ext = 0
        self.score = 0

    def jouer(self):

        import random

        #on évalue la différence de niveau entre les deux équipes qui s'affrontent
        A= self.équipe_dom.note_att_club - self.équipe_ext.note_def_club
        #en fonction de cette différence, on indique la probabilité de marquer des buts, en laissant une part de hasard
        if A < 0:
            self.buts_dom = int(random.randint(0,10)/(-5*A)) #on divise par 5 pour avoir des valeurs raisonnables
            # et on divise par A pour diminuer la probabilité de marquer contre une équipe ayant une meilleure défense que son attaque
        if A > 0:
            self.buts_dom = int(random.randint(0, 10) * A / 5)
            # vice versa
        if A == 0:
            self.buts_dom = random.randint(0, 2)

        B = self.équipe_ext.note_att_club - self.équipe_dom.note_def_club
        if B < 0 :
            self.buts_ext = random.randint(0, 1)
        if B == 0:
            self.buts_ext = random.randint(0, 2)
        if B > 0:
            self.buts_ext = int(random.randint(0, 10) * B/5)



        self.score = [self.buts_dom, self.buts_ext]

        self.équipe_dom.evol_butsmarqués(self.buts_dom)
        self.équipe_ext.evol_butsmarqués(self.buts_ext)

        #on attribue les points correspondants au résultat du match
        if self.buts_dom > self.buts_ext:
            self.équipe_dom.evol_points(3)
        elif self.buts_dom == self.buts_ext:
            self.équipe_dom.evol_points(1)
            self.équipe_ext.evol_points(1)
        else:
            self.équipe_ext.evol_points(3)

        #mise à jour des notes des joueurs
        for joueur in self.équipe_dom.joueurs:
            joueur.evol_notejoueur(self.score)

        #on attribue les buts marqués aux joueurs de l'équipe à domicile
        for j in range(self.buts_dom):
            a=r.randint(0, 10)
            if a<6: #si c'est un défenseur, on refait le test aléatoire pour baisser la probabilité que ce soit un défenseur qui marque
                a = r.randint(0, 10)
            self.équipe_dom.joueurs[a].evol_buts(1) #on ajoute un but au joueur selectionné

        #on réitère avec l'équipe à l'extérieur
        for joueur in self.équipe_ext.joueurs:
            joueur.evol_notejoueur([self.score[1],self.score[0]])

        for j in range(self.buts_ext):
            a=r.randint(0, 10)
            if a<6:
                a = r.randint(0, 10)
            self.équipe_ext.joueurs[a].evol_buts(1)

        #mise à jour des notes des clubs
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
    def __str__(self):
        return '{} vs {}'.format(self.équipe_dom.nom,self.équipe_ext.nom)

import itertools
Villes = ['Paris', 'Lens', 'Marseille', 'Monaco', 'Lille', 'Rennes', 'Lyon', 'Reims','Nice', 'Lorient', 'Clermont', 'Toulouse', 'Montpellier', 'Nantes', 'Auxerre','Brest', 'Strasbourg', 'Troyes', 'Angers', 'Guingamp']

class Championnat:
    # intitialisation des variables d'instance
    def __init__(self):
            self.clubs = []
            self.matches = []
            for k in Villes :
                self.clubs.append(script_clubs.Club(k))

    # creation du calendrier des matches
    def planifier_matches(self):
        matchesallers = []
        matchesretour = []
        #on separe en deux les équipes
        groupe1 = self.clubs[:len(self.clubs)//2]
        groupe2 = self.clubs[len(self.clubs) // 2:]
        print(groupe1[0])
        print(groupe2[0])
        # on crée tous les matches selon la méthode de rotation autour du premier élément
        for i in range(len(self.clubs)-1):
            for n in range(len(groupe1)):
                matchesallers.append(script_match.Match(groupe1[n],groupe2[n]))
                matchesretour.append(script_match.Match(groupe2[n],groupe1[n]))

            groupe2.append(groupe1[-1])
            groupe1=[groupe1[0]]+[groupe2[0]]+groupe1[1:-1]
            groupe2.pop(0)

        self.matches.extend(matchesallers)
        self.matches.extend(matchesretour)
    # méthode pour simuler les matches du championnat
    def jouer_matches(self):
        for match in self.matches:
            match.jouer()
    # accésseurs
    def get_clubs(self):
        return self.clubs


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

            #if resultat=='D':
             #   self.note+=r.randint(-1,0)
            #elif resultat=='N':
             #   self.note+=r.randint(-1,1)
            #else:
             #   self.note+=r.randint(0,1)

    def get_nom(self):
        return self.nom
    def get_buts_marqués(self):
        return self.butsmarqués
    def get_note(self):
        return self.note

class Attaquant(Joueur) :
    def __init__(self,nom):
        super().__init__(self)
        self.note_att=r.randint(7,9)
        self.note_def=r.randint(3,5)
        self.note=(self.note_def+self.note_att)/2
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
    def evol_notejoueur(self,resultat):
        if resultat[1] >= 2 and self.note_def>0:
            self.note_def += 0.5 * r.randint(-1, 0)
        if resultat[1] < 2 and self.note_def<0:
            self.note_def += 0.5 * r.randint(0, 1)









