from mainWindow import *
from martypy import Marty, MartyConnectException

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = MainWindow(None)
    fenetre.show()
    app.exec()