import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface de pilotage du robot Marty")
        self.setFixedSize(800, 800)
        self.interface()

    def interface(self):
        layout = QVBoxLayout()

        self.bouton_avancer = QPushButton("Avancer")
        self.bouton_reculer = QPushButton("Reculer")
        self.bouton_droite = QPushButton("Aller à droite")
        self.bouton_gauche = QPushButton("Aller à gauche")
        
        layout.addWidget(self.bouton_avancer)
        layout.addWidget(self.bouton_reculer)
        layout.addWidget(self.bouton_droite)
        layout.addWidget(self.bouton_gauche)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ControlPanel()
    fenetre.show()
    app.exec()

