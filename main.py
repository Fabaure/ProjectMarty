import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
from martypy import Marty, MartyConnectException
from controlPanel import ControlPanel
from creationPanel import CreationPanel
from mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = MainWindow(None)
    fenetre.show()
    app.exec()