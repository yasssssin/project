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
