import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel, QHeaderView, QComboBox,QLineEdit,QMessageBox
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
import script_championnat


class MainWindow(QMainWindow):
    def __init__(self, championnat):
        super().__init__()
        # on initialise ici le championnat pour avoir les données necesaire à l'iu.
        self.championnat = championnat
        self.matches = self.championnat.matches

        #titre pour l'iu
        self.setWindowTitle("Championnat de Foot")
        #création de la fenetre et de sa mise en page à organiser plus tard
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()

        #Créations des buttons et input box pour l'interface.

        self.results_button = QPushButton("Afficher les résultats du championnat", self)
        self.results_button.clicked.connect(self.afficher_results)
        self.layout.addWidget(self.results_button)

        self.stats_button = QPushButton("Afficher les statistiques des équipes", self)
        self.stats_button.clicked.connect(self.afficher_stats)
        self.layout.addWidget(self.stats_button)

        self.label_fichier = QLabel("Nom du fichier:")
        self.text_fichier = QLineEdit()
        self.layout.addWidget(self.label_fichier)
        self.layout.addWidget(self.text_fichier)



        self.button_sauvegarder = QPushButton("Sauvegarder")
        self.button_sauvegarder.clicked.connect(self.sauvegarder_resultats)
        self.layout.addWidget(self.button_sauvegarder)

        self.matchday_label = QLabel("Sélectionnez une journée de match pour voir les résultats :")
        self.layout.addWidget(self.matchday_label)

        self.matchday_combo = QComboBox()
        for i in range(1, int(len(self.matches) / len(self.championnat.clubs)) + 1):
            self.matchday_combo.addItem("Journée {}".format(i))
        self.layout.addWidget(self.matchday_combo)

        self.matchday_combo.currentIndexChanged.connect(self.afficher_matchday_results)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.main_widget.setLayout(self.layout)

    def sauvegarder_resultats(self):
        fichier = self.text_fichier.text()

        try:
            with open(fichier, "w") as f:
                for row in range(self.table.rowCount()):
                    row_data = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append("")  # Ajoute une chaîne vide si l'élément est None
                    f.write("\t".join(row_data) + "\n")  # Écrit les données de la ligne séparées par une tabulation

            QMessageBox.information(self, "Sauvegarde réussie", "Les résultats ont été sauvegardés avec succès.")
        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de la sauvegarde : {str(e)}")

    def afficher_results(self):
        self.table.clear()
        self.table.setRowCount(len(self.championnat.clubs))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Club", "Points", "Buts marqués", "Note du club"])

        for i, club in enumerate(sorted(self.championnat.clubs, key=lambda x: (x.points,x.buts_marqués), reverse=True)):
            self.table.setItem(i, 0, QTableWidgetItem(club.nom))
            self.table.setItem(i, 1, QTableWidgetItem(str(club.points)))
            self.table.setItem(i, 2, QTableWidgetItem(str(club.buts_marqués)))
            self.table.setItem(i, 3, QTableWidgetItem(str(club.noteclub)))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def afficher_stats(self):
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)

        chart = QChart()

        bar_set = QBarSet("Buts marqués")
        for club in self.championnat.clubs:
             bar_set.append(club.buts_marqués)

        series = QBarSeries()
        series.append(bar_set)

        chart.addSeries(series)

        categories = [club.nom for club in self.championnat.clubs]
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setRange(0, max([club.buts_marqués for club in self.championnat.clubs]) + 5)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.layout.addWidget(chart_view)

    def afficher_matchday_results(self, index):
        matchday = index + 1
        num_teams = len(self.championnat.clubs)
        matches_per_round = num_teams // 2

        start_index = (matchday - 1) * matches_per_round
        end_index = start_index + matches_per_round

        matchday_matches = self.matches[start_index:end_index]

        self.table.clear()
        self.table.setRowCount(len(matchday_matches))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Équipe domicile", "Équipe extérieure", "Score"])

        for i, match in enumerate(matchday_matches):
            self.table.setItem(i, 0, QTableWidgetItem(match.équipe_dom.nom))
            self.table.setItem(i, 1, QTableWidgetItem(match.équipe_ext.nom))
            self.table.setItem(i, 2, QTableWidgetItem(f"{match.buts_dom} - {match.buts_ext}"))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ligue1 = script_championnat.Championnat()
    ligue1.planifier_matches()
    ligue1.jouer_matches()
    main_window = MainWindow(ligue1)
    main_window.show()

    sys.exit(app.exec_())