import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from martypy import Marty

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface de pilotage du robot Marty")
        self.setFixedSize(800, 800)
        self.interface()

    def interface(self):
        layout = QVBoxLayout()

        self.btn_forward = QPushButton("Move forward")
        self.btn_backward = QPushButton("Move backward")
        self.btn_right = QPushButton("Move to right")
        self.btn_left = QPushButton("Move to left")
        self.btn_dance = QPushButton("Dance")
        
        layout.addWidget(self.btn_forward)
        layout.addWidget(self.btn_backward)
        layout.addWidget(self.btn_right)
        layout.addWidget(self.btn_left)
        layout.addWidget(self.btn_dance)


        self.btn_dance.clicked.connect(lambda: self.action())

        self.setLayout(layout)


    def action(self):
        marty.dance()


if __name__ == "__main__":
    adresse_ip = "192.168.0.101" # à modifier
    marty = Marty("wifi", adresse_ip) # connexion à Marty
    app = QApplication(sys.argv)
    fenetre = ControlPanel()
    fenetre.show()
    app.exec()

