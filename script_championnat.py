import script_clubs
import script_joueur
import script_match
import itertools
Villes = ['Paris', 'Lens', 'Marseille', 'Monaco', 'Lille', 'Rennes', 'Lyon', 'Reims','Nice', 'Lorient', 'Clermont', 'Toulouse', 'Montpellier', 'Nantes', 'Auxerre','Brest', 'Strasbourg', 'Troyes', 'Angers', 'Guingamp']

# que faire si deux équipes ot le même nombre de points: les  buts marqués.

class Championnat:
    def __init__(self):
            self.clubs = []
            self.matches = []
            for k in Villes :
                self.clubs.append(script_clubs.Club(k))
    # def planifier_matches(self):
    #
    #     for i in range(len(self.clubs)):
    #         for j in range(i + 1, len(self.clubs)):
    #             match_aller = script_match.Match(self.clubs[i], self.clubs[j])
    #             match_retour = script_match.Match(self.clubs[j], self.clubs[i])
    #             self.matches.append(match_aller)
    #             self.matches.append(match_retour)
    # def planifier_matches(self):
    #     comb_match=[]
    #
    #     for i in range(len(self.clubs)):
    #         for j in range(len(self.clubs)):
    #             if i!=j:
    #                 comb_match.append(script_match.Match(self.clubs[i], self.clubs[j]))
    #     nbjournées=2*len(self.clubs)-2
    #     for i in range(nbjournées):
    #
    #         dic={}
    #         for elt in self.clubs:
    #             dic[elt.nom]=0
    #         okk=comb_match.copy()
    #         print(len(comb_match))
    #         for elts in okk:
    #                 if dic[elts.équipe_dom.nom]==0 and dic[elts.équipe_ext.nom]==0:
    #                     self.matches.append(elts)
    #                     ok=comb_match.copy()
    #                     comb_match=[]
    #                     for let in ok:
    #                         if elts.équipe_dom.nom!=let.équipe_dom.nom and elts.équipe_ext.nom!=let.équipe_ext.nom:
    #                             comb_match.append(let)
    #
    #
    #                     dic[elts.équipe_dom.nom]=1
    #                     dic[elts.équipe_ext.nom] =1
    def planifier_matches(self):
        nb_clubs = len(self.clubs)
        nb_journees = 2*(nb_clubs - 1)

        # Création de la liste des combinaisons de matchs
        comb_match = []
        for i in range(nb_clubs):
            for j in range(nb_clubs):
                if i != j:
                    comb_match.append(script_match.Match(self.clubs[i], self.clubs[j]))

        # Planification des matchs par journée
        clubs_disponible= self.clubs[:]
        clubs_disponibles=clubs_disponible.copy()# Déplacer cette ligne avant la boucle for
        for journee in range(nb_journees):
            matchs_journee = []

            # Parcours des clubs disponibles
            while len(clubs_disponible) > 1:
                equipe_dom = clubs_disponible.pop(0)  # Prendre le premier club de la liste
                equipe_ext = clubs_disponible.pop(0)  # Prendre le deuxième club de la liste
                match = script_match.Match(equipe_dom, equipe_ext)
                matchs_journee.append(match)

            # Ajout des matchs de la journée au championnat
            self.matches.extend(matchs_journee)

            # Réorganisation des clubs disponibles pour la prochaine journée
            clubs_disponibles.append(clubs_disponibles[0])
            clubs_disponibles.pop(0)
            clubs_disponible=clubs_disponibles.copy()

    def jouer_matches(self):
        for match in self.matches:
            match.jouer()
    def get_clubs(self):
        return self.clubs


