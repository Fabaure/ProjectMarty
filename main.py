from Interface import *
from martypy import Marty, MartyConnectException

if __name__ == "__main__":
    adresse_ip = "192.168.0.100" 
    try:
        marty = Marty("wifi", adresse_ip) 
        print("Marty connecté !")
    except MartyConnectException as e:
        print("Impossible de se connecter à Marty")
        marty = None
    app = QApplication(sys.argv)
    fenetre = ControlPanel(marty)
    fenetre.show()
    app.exec()