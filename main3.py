import sys
import script_championnat
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel, QHeaderView, QComboBox,QLineEdit,QMessageBox
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, championnat):
        super().__init__()
        # on initialise ici le championnat pour avoir les donnees necesaires à l'iu.
        self.championnat = championnat
        self.matches = self.championnat.matches

        #titre pour l'iu
        self.setWindowTitle("Championnat de Foot")
        #creation de la fenetre et de sa mise en page à organiser plus tard
        self.widget_f = QWidget()
        self.setCentralWidget(self.widget_f)
        self.layout = QVBoxLayout()

        #Creations des buttons et input box pour l'interface.

        self.boutton_resultats = QPushButton("Afficher les resultats du championnat", self)
        self.boutton_resultats.clicked.connect(self.afficher_resultats)
        self.layout.addWidget(self.boutton_resultats)

        self.boutton_stats = QPushButton("Afficher les statistiques des equipes", self)
        self.boutton_stats.clicked.connect(self.afficher_stats)
        self.layout.addWidget(self.boutton_stats)

        self.label_fichier = QLabel("Nom du fichier:")
        self.text_fichier = QLineEdit()
        self.layout.addWidget(self.label_fichier)
        self.layout.addWidget(self.text_fichier)

        self.boutton_sauvegarder = QPushButton("Sauvegarder")
        self.boutton_sauvegarder.clicked.connect(self.sauvegarder_resultats)
        self.layout.addWidget(self.boutton_sauvegarder)

        self.journee_label = QLabel("Selectionnez une journee de match pour voir les resultats :")
        self.layout.addWidget(self.journee_label)
# choix déroulant de la journée à afficher
        self.journee_combo = QComboBox()
        for i in range(1, 2*(len(self.championnat.clubs)-1)+1):
            self.journee_combo.addItem("Journee {}".format(i))
        self.layout.addWidget(self.journee_combo)
        #definition du numéro de journée avec le numero de la selection dans le combo
        self.journee_combo.currentIndexChanged.connect(self.afficher_journee_resultats)

#création de la table pour y mettre les résultats(table partagée pour tous les résultats)
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.widget_f.setLayout(self.layout)
# creation des objet du graphe en baton
        self.chart = QChart()
        self.chart_plot = QChartView(self.chart)
        self.axes_y=QValueAxis()

        self.axes_y.setRange(0, max([club.buts_marques for club in self.championnat.clubs]) + 5)
        #On rajoute les axes et on choisit les axes ou ils vont (à gauche ou en bas avec Qt .AligneLeft
        self.chart.addAxis(self.axes_y, Qt.AlignLeft)
        self.axes_x = QBarCategoryAxis()
        categories = [club.nom for club in self.championnat.clubs]
        self.axes_x.append(categories)
        self.chart.addAxis(self.axes_x, Qt.AlignBottom)


    def sauvegarder_resultats(self):
        fichier = self.text_fichier.text()
# On fait une exeption ici pour que l"='eereur s'affiche dans l'interface.
        try:
            f=open(fichier, "w")
            for ligne in range(self.table.rowCount()):
                    lignes = []
                    for colonne in range(self.table.columnCount()):
                        lignes.append(self.table.item(ligne, colonne).text())
                    f.write("\t".join(lignes) + "\n")
            f.close()
            QMessageBox.information(self, "Sauvegarde reussie", "Les resultats ont ete sauvegardes avec succès.")
        except Exception as e:
            QMessageBox.warning(self, "Erreur", "Erreur lors de la sauvegarde : {}".format(str(e)))
#affichage des resultats dans un tableau
    def afficher_resultats(self):
        self.table.clear()
        # On defini la taille du tableau
        self.table.setRowCount(len(self.championnat.clubs))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Club", "Points", "Buts marques", "Note du club"])
        #On remplit le tableau avec les nom,point buts marques et note club
        for i, club in enumerate(sorted(self.championnat.clubs, key=lambda x: (x.points,x.buts_marques), reverse=True)):
            self.table.setItem(i, 0, QTableWidgetItem(club.nom))
            self.table.setItem(i, 1, QTableWidgetItem(str(club.points)))
            self.table.setItem(i, 2, QTableWidgetItem(str(club.buts_marques)))
            self.table.setItem(i, 3, QTableWidgetItem(str(club.noteclub)))
        # fonction pour mettre la bonne taille pour la largeur des colonnes
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def afficher_stats(self):
        self.table.clear()
        # il faut vider la table pour ne pas que les anciennes valeurs ne restent a chaque fois que l'on appuis sur le bouton
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        # on rempli les bars à mettre dans le diagramme
        bar = QBarSet("Buts marques")
        for club in self.championnat.clubs:
             bar.append(club.buts_marques)
        if len(self.chart.series()) > 0:
            self.chart.removeSeries(self.chart.series()[0])
        # on crée la liste de bar qui remplira le graph
        liste_bar = QBarSeries()
        liste_bar.append(bar)

        self.chart.addSeries(liste_bar)
        self.chart_plot.resize(2240,1300)
        # meme soucis ici la fenetre reste derrierre l'interface si on la ferme pas avant d'appuyer sur le bouton
        self.chart_plot.close()
        self.chart_plot.show()
#methode pour le bouton combo et les differentes journées.
    def afficher_journee_resultats(self, journee):
        #definition des valeurs pour les journée(nb de matchs,quels matches début et fin dans la liste des matches pour chaque journées)
        nb_equipe = len(self.championnat.clubs)
        matches_par_journee = nb_equipe // 2

        debut_jour = (journee) * matches_par_journee
        fin_jour = debut_jour + matches_par_journee

        matches_jour = self.matches[debut_jour:fin_jour]
        #creation de la table avec la legende
        self.table.clear()
        self.table.setRowCount(len(matches_jour))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["equipe domicile", "equipe exterieure", "Score"])
        #t le remplisssage du classement et autres attributs d'une equipe
        for i, match in enumerate(matches_jour):
            self.table.setItem(i, 0, QTableWidgetItem(match.equipe_dom.nom))
            self.table.setItem(i, 1, QTableWidgetItem(match.equipe_ext.nom))
            self.table.setItem(i, 2, QTableWidgetItem("{} - {}".format(match.buts_dom,match.buts_ext)))
# même chose réglage de la largeur des colonnes
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
# lanceur de la simulation ouverture de la MainWindow


def lancerlesimulateur():
    #ouverture de l'interface
    app = QApplication(sys.argv)

    ligue1 = script_championnat.Championnat()
    ligue1.planifier_matches()
    ligue1.jouer_matches()
    main_window = MainWindow(ligue1)
    main_window.show()
    main_window.resize(2200,1300)

    sys.exit(app.exec_())

