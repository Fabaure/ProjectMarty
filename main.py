from martypy import Marty

adresse_ip = "192.168.0.101" # à modifier
marty = Marty("wifi", adresse_ip) # connexion à Marty

if (marty.is_conn_ready()): 
    # si Marty est connecté
    print("Connected to Marty!")
    while(marty.is_conn_ready()): # boucle si Marty connecté
        print("Il danse !")
        marty.dance() # exemple
        # code a faire
        marty.close() # deconnesion de Marty
        print("Disconnected from Marty.")
else: 
    # si Marty n'est pas connecté
    print("Failed to connect to Marty T-T.")