import script_joueur
import script_championnat
import script_clubs

class Match:
    def __init__(self, équipe_dom, équipe_ext):
        self.équipe_dom = équipe_dom
        self.équipe_ext = équipe_ext
        self.buts_dom = 0
        self.buts_ext = 0
        self.score = 0

    def jouer(self):

        import random
        self.buts_dom = random.randint(0, 5) #à pondérer par les notes att et def

        self.buts_ext = random.randint(0, 5)

        self.score = (self.buts_dom, self.buts_ext)

        self.équipe_dom.evol_butsmarqués(self.buts_dom)
        self.équipe_ext.evol_butsmarqués(self.buts_ext)

        if self.buts_dom > self.buts_ext:
            self.équipe_dom.evol_points(3)
        elif self.buts_dom == self.buts_ext:
            self.équipe_dom.evol_points(1)
            self.équipe_ext.evol_points(1)
        else:
            self.équipe_ext.evol_points(3)

        for joueur in self.équipe_dom.get_joueurs():
            joueur.evol_buts(self.buts_dom)
            joueur.evol_notejoueur(self.score)
        for joueur in self.équipe_ext.get_joueurs():
            joueur.evol_buts(self.buts_ext)
            joueur.evol_notejoueur(self.score)


        équipe_dom.evol_noteclub(self)
        équipe_ext.evol_noteclub(self)

        assert self.buts_dom > self.buts_ext or self.buts_dom == self.buts_ext, "Erreur: l'équipe qui a gagné n'a pas marqué plus de buts que l'adversaire"

    # Accesseurs
    def get_équipe_dom(self):
        return self.équipe_dom

    def get_équipe_ext(self):
        return self.équipe_ext

    def get_buts_dom(self):
        return self.buts_dom

    def get_buts_ext(self):
        return self.buts_ext
