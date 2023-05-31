import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel, QHeaderView, QComboBox,QLineEdit,QMessageBox
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
import script_championnat


class MainWindow(QMainWindow):
    def __init__(self, championnat):
        super().__init__()
        # on initialise ici le championnat pour avoir les donnees necesaire à l'iu.
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

        self.journee_combo = QComboBox()
        for i in range(1, int(len(self.matches) / len(self.championnat.clubs)) + 1):
            self.journee_combo.addItem(f"Journee {i}")
        self.layout.addWidget(self.journee_combo)

        self.journee_combo.currentIndexChanged.connect(self.afficher_journee_resultats)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.widget_f.setLayout(self.layout)

    def sauvegarder_resultats(self):
        fichier = self.text_fichier.text()

        try:
            with open(fichier, "w") as f:
                for ligne in range(self.table.rowCount()):
                    lignes = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(ligne, column)
                        if item is not None:
                            lignes.append(item.text())
                        else:
                            lignes.append("")  # Ajoute une chaîne vide si l'element est None
                    f.write("\t".join(lignes) + "\n")  # ecrit les donnees de la ligne separees par une tabulation

            QMessageBox.information(self, "Sauvegarde reussie", "Les resultats ont ete sauvegardes avec succès.")
        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de la sauvegarde : {str(e)}")

    def afficher_resultats(self):
        self.table.clear()
        self.table.setRowCount(len(self.championnat.clubs))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Club", "Points", "Buts marques", "Note du club"])

        for i, club in enumerate(sorted(self.championnat.clubs, key=lambda x: (x.points,x.buts_marques), reverse=True)):
            self.table.setItem(i, 0, QTableWidgetItem(club.nom))
            self.table.setItem(i, 1, QTableWidgetItem(str(club.points)))
            self.table.setItem(i, 2, QTableWidgetItem(str(club.buts_marques)))
            self.table.setItem(i, 3, QTableWidgetItem(str(club.noteclub)))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def afficher_stats(self):
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)

        chart = QChart()

        bar_set = QBarSet("Buts marques")
        for club in self.championnat.clubs:
             bar_set.append(club.buts_marques)

        series = QBarSeries()
        series.append(bar_set)

        chart.addSeries(series)

        categories = [club.nom for club in self.championnat.clubs]
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setRange(0, max([club.buts_marques for club in self.championnat.clubs]) + 5)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        chart_view = QChartView(chart)
        # chart_view.setRenderHint(QPainter.Antialiasing)

        self.layout.addWidget(chart_view)

    def afficher_journee_resultats(self, journee):
        nb_teams = len(self.championnat.clubs)
        matches_par_journee = nb_teams // 2

        debut_jour = (journee) * matches_par_journee
        fin_jour = debut_jour + matches_par_journee

        matches_jour = self.matches[debut_jour:fin_jour]

        self.table.clear()
        self.table.setRowCount(len(matches_jour))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["equipe domicile", "equipe exterieure", "Score"])

        for i, match in enumerate(matches_jour):
            self.table.setItem(i, 0, QTableWidgetItem(match.equipe_dom.nom))
            self.table.setItem(i, 1, QTableWidgetItem(match.equipe_ext.nom))
            self.table.setItem(i, 2, QTableWidgetItem("{} - {}".format(match.buts_dom,match.buts_ext)))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ligue1 = script_championnat.Championnat()
    ligue1.planifier_matches()
    ligue1.jouer_matches()
    main_window = MainWindow(ligue1)
    main_window.show()

    sys.exit(app.exec_())