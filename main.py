import sys
from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = MainWindow(None)
    fenetre.show()
    app.exec()