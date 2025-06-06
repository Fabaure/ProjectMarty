import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
from martypy import Marty, MartyConnectException
from controlPanel import ControlPanel
from creationPanel import CreationPanel
from mainWindow import MainWindow

if __name__ == "__main__":
    adresse_ip = "192.168.0.100" 
    try:
        marty = Marty("wifi", adresse_ip) 
        print("Marty connecté !")
    except MartyConnectException as e:
        print("Impossible de se connecter à Marty")
        marty = None
    app = QApplication(sys.argv)
    fenetre = MainWindow(marty)
    fenetre.show()
    app.exec()