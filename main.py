from martypy import Marty

adresse_ip = "192.168.0.101" # à modifier
marty = Marty("wifi", adresse_ip) # connexion à Marty
tableau_couleurs = []

if (marty.is_conn_ready()): 
    # si Marty est connecté
    print("Connected to Marty!")
    while(marty.is_conn_ready()): # boucle si Marty connecté
        color = marty.get_ground_sensor_reading("left") # lecture de la couleur
        if(color > 0 and color < 20):
            marty.dance()
        print(color)
        # code a faire
        marty.close() # deconnection de Marty
        print("Disconnected from Marty.")
else: 
    # si Marty n'est pas connecté
    print("Failed to connect to Marty T-T.")