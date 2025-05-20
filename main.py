import msvcrt
from martypy import Marty
from sensor import *

def main():
    adresse_ip = "192.168.0.108" # à modifier
    marty = Marty("wifi", adresse_ip) # connexion à Marty
    marty.set_marty_name("KAY/0")

    if (marty.is_conn_ready()): 
        # si Marty est connecté
        print("Connected to Marty !")
        running = True
        while(marty.is_conn_ready() and running): # boucle si Marty connecté
            if (msvcrt.kbhit()):  # une touche a été pressée
                key = msvcrt.getch()
                if key == b'a' or key == b'A':
                    print("Touche A détectée, arrêt.")
                    running = False
                if key == b'e' or key == b'E':
                    getColor(marty)
                    getDistance(marty)
                    getBattery(marty)
        print("Disconnected from Marty.")
        marty.close() # deconnection de Marty
    else: 
        # si Marty n'est pas connecté
        print("Failed to connect to Marty T-T.")

if __name__ == "__main__":
    main()