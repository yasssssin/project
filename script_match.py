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
