import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface de pilotage du robot Marty")
        self.setFixedSize(800, 800)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ControlPanel()
    fenetre.show()
    app.exec()
