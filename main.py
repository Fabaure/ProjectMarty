from martypy import Marty
from sensor import *

def main():
    adresse_ip = "192.168.0.101" # à modifier
    marty = Marty("wifi", adresse_ip) # connexion à Marty
    marty.set_marty_name("KAY/0")

    if (marty.is_conn_ready()): 
        # si Marty est connecté
        print("Connected to Marty !")
        while(marty.is_conn_ready()): # boucle si Marty connecté
            getColor(marty)
            getDistance(marty)
            getBattery(marty)
            # code a faire
            marty.close() # deconnection de Marty
            print("Disconnected from Marty.")
    else: 
        # si Marty n'est pas connecté
        print("Failed to connect to Marty T-T.")

if __name__ == "__main__":
    main()