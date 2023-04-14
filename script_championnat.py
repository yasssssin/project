import script_clubs
import script_joueur
import script_match

Villes=['Paris','Lens','Marseille','Monaco','Lille','Rennes','Lyon','Reims',
        'Nice','Lorient','Clermont','Toulouse','Montpellier','Nantes','Auxerre',
        'Brest','Strasbourg','Troyes','Angers','Guingamp']
class Championnat:

    def __init__(self):
        self.clubs = []
        self.matches = []
        for k in Villes :
            self.clubs.append(script_clubs.club(k))
    def planifier_matches(self):

        for i in range(len(self.clubs)):
            for j in range(i + 1, len(self.clubs)):
                match_aller = script_match.Match(self.clubs[i], self.clubs[j])
                match_retour = script_match.Match(self.clubs[j], self.clubs[i])
                self.matches.append(match_aller)
                self.matches.append(match_retour)

    def jouer_matches(self):
        for match in self.matches:
            match.jouer()


