import script_joueur
import script_championnat
import script_clubs
import random as r

class Match:
    def __init__(self, equipe_dom, equipe_ext):
        self.equipe_dom = equipe_dom
        self.equipe_ext = equipe_ext
        self.buts_dom = 0
        self.buts_ext = 0
        self.score = 0

    def jouer(self):

        import random

        #on evalue la difference de niveau entre les deux equipes qui s'affrontent
        A= self.equipe_dom.note_att_club - self.equipe_ext.note_def_club
        #en fonction de cette difference, on indique la probabilite de marquer des buts, en laissant une part de hasard
        if A < 0:
            self.buts_dom = int(random.randint(0,10)/(-5*A)) #on divise par 5 pour avoir des valeurs raisonnables
            # et on divise par A pour diminuer la probabilite de marquer contre une equipe ayant une meilleure defense que son attaque
        if A > 0:
            self.buts_dom = int(random.randint(0, 10) * A / 5)
            # vice versa
        if A == 0:
            self.buts_dom = random.randint(0, 2)

        B = self.equipe_ext.note_att_club - self.equipe_dom.note_def_club
        if B < 0 :
            self.buts_ext = random.randint(0, 1)
        if B == 0:
            self.buts_ext = random.randint(0, 2)
        if B > 0:
            self.buts_ext = int(random.randint(0, 10) * B/5)



        self.score = [self.buts_dom, self.buts_ext]

        self.equipe_dom.evol_butsmarques(self.buts_dom)
        self.equipe_ext.evol_butsmarques(self.buts_ext)

        #on attribue les points correspondants au resultat du match
        if self.buts_dom > self.buts_ext:
            self.equipe_dom.evol_points(3)
        elif self.buts_dom == self.buts_ext:
            self.equipe_dom.evol_points(1)
            self.equipe_ext.evol_points(1)
        else:
            self.equipe_ext.evol_points(3)

        #mise à jour des notes des joueurs
        for joueur in self.equipe_dom.joueurs:
            joueur.evol_notejoueur(self.score)

        #on attribue les buts marques aux joueurs de l'equipe à domicile
        for j in range(self.buts_dom):
            a=r.randint(0, 10)
            if a<6: #si c'est un defenseur, on refait le test aleatoire pour baisser la probabilite que ce soit un defenseur qui marque
                a = r.randint(0, 10)
            self.equipe_dom.joueurs[a].evol_buts(1) #on ajoute un but au joueur selectionne

        #on reitère avec l'equipe à l'exterieur
        for joueur in self.equipe_ext.joueurs:
            joueur.evol_notejoueur([self.score[1],self.score[0]])

        for j in range(self.buts_ext):
            a=r.randint(0, 10)
            if a<6:
                a = r.randint(0, 10)
            self.equipe_ext.joueurs[a].evol_buts(1)

        #mise à jour des notes des clubs
        self.equipe_dom.evol_noteclub()
        self.equipe_ext.evol_noteclub()

    # Accesseurs
    def get_equipe_dom(self):
        return self.equipe_dom

    def get_equipe_ext(self):
        return self.equipe_ext

    def get_buts_dom(self):
        return self.buts_dom

    def get_buts_ext(self):
        return self.buts_ext
    def __str__(self):
        return '{} vs {}'.format(self.equipe_dom.nom,self.equipe_ext.nom)
