import script_championnat
import numpy as np

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem
import script_championnat

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

        # Trie des clubs par points
        clubs_tries = sorted(clubs, key=lambda x: x.get_points(), reverse=True)

        # Parcours des clubs triés
        for i, club in enumerate(clubs_tries):
            resultat += f"{i+1}. Club : {club.get_nom()}\n"
            resultat += f"Points : {club.get_points()}\n"
            resultat += f"Buts marqués : {club.get_buts_marqués()}\n"

            joueurs = club.get_joueur()
            meilleur_joueur = max(joueurs, key=lambda x: x.get_buts_marqués())
            resultat += f"Meilleur joueur : {meilleur_joueur.get_nom()} - Buts marqués : {meilleur_joueur.get_buts_marqués()}\n\n"

        self.text_resultat.setPlainText(resultat)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    interface = ChampionnatInterface()
    interface.show()

    sys.exit(app.exec_())
