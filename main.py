import script_championnat
import numpy as np

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem
import script_championnat
from matplotlib import pyplot as plt
class ChampionnatInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Resultats de la ligue 1")
        self.layout = QVBoxLayout()
        # On créer un onglet pour y afficher les résultats
        self.label_resultat = QLabel("Résultat du championnat:")
        self.text_resultat = QTextEdit()
        self.layout.addWidget(self.label_resultat)
        self.layout.addWidget(self.text_resultat)

        # On met le bouton calculer d'abord sinon le on a l'impression que le bouton est dans 'l'onglet nom du fichier"
        self.button_calculer = QPushButton("Simuler Championnat")
        self.button_calculer.clicked.connect(self.calculer_championnat)
        self.layout.addWidget(self.button_calculer)

        self.label_fichier = QLabel("Nom du fichier:")
        self.text_fichier = QLineEdit()
        self.layout.addWidget(self.label_fichier)
        self.layout.addWidget(self.text_fichier)



        self.button_sauvegarder = QPushButton("Sauvegarder")
        self.button_sauvegarder.clicked.connect(self.sauvegarder_resultats)
        self.layout.addWidget(self.button_sauvegarder)

        self.setLayout(self.layout)


    def calculer_championnat(self):
        self.ligue1 = script_championnat.Championnat()
        self.ligue1.planifier_matches()
        self.ligue1.jouer_matches()
        #On met les variables ici pour qu'il n'y ai pas une équipe qui finnisse par gagner tous le temps après quelques simulations

        # Obtention des résultats du championnat
        resultat = "Classement du championnat :\n"
        clubs = self.ligue1.get_clubs()


        # On trie les clubs par points selon les points
        clubs.sort(key=lambda x: x.get_points(), reverse=True)
        # ici on utilise key=lambda pour créer une fonction 'inine' sinon on devrait faire unn boucle for pour recuperer les points puis trier les clubs

        # Parcours des clubs triés
        for i, club in enumerate(clubs):
            resultat += "{}. Club : {}\n".format(i+1, club.get_nom())
            resultat += "Points : {}\n".format(club.get_points())
            resultat += "Buts marqués : {}\n".format(club.get_buts_marqués())

            joueurs = club.get_joueur()
            meilleur_joueur = max(joueurs, key=lambda x: x.get_buts_marqués())
            resultat += "Meilleur joueur : {} - Buts marqués : {}\n\n".format(meilleur_joueur.get_nom(),meilleur_joueur.get_buts_marqués())

        self.text_resultat.setPlainText(resultat)
        self.creer_boutons_clubs()

    def sauvegarder_resultats(self):
        fichier = self.text_fichier.text()

        if fichier == "":
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un nom de fichier.")
            return

        resultat = self.text_resultat.toPlainText()

        try:
            with open(fichier, "w") as f:
                f.write(resultat)

            QMessageBox.information(self, "Sauvegarde réussie", "Les résultats ont été sauvegardés avec succès.")
        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de la sauvegarde : {str(e)}")

    def afficher_graphique_club(self, club):
        joueurs = club.get_joueur()
        noms_joueurs = [joueur.get_nom() for joueur in joueurs]
        buts_marques = [joueur.get_buts_marqués() for joueur in joueurs]

        plt.bar(noms_joueurs, buts_marques)
        plt.xlabel("Joueurs")
        plt.ylabel("Buts marqués")
        plt.title("Statistiques des buts marqués par joueur")

        plt.show()
    def creer_boutons_clubs(self):
        clubs = self.ligue1.get_clubs()

        for club in clubs:
            bouton_club = QPushButton(club.get_nom())
            bouton_club.clicked.connect(lambda _, c=club: self.afficher_graphique_club(c))
            self.layout.addWidget(bouton_club)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    interface = ChampionnatInterface()
    interface.show()

    sys.exit(app.exec_())
