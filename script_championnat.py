import script_clubs
import script_joueur
import script_match
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


