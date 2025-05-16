from martypy import Marty

adresse_ip = "192.168.0.101" # à modifier
marty = Marty("wifi", adresse_ip) # connexion à Marty
marty.set_marty_name("KAY/0")

def detectColor():
    color = marty.get_ground_sensor_reading("left") # lecture de la couleur
    print(color)
    if(color < 20):
        print("Noir")
    elif(color > 20 and color < 25):
        print("Bleu foncé")
    elif(color > 30 and color < 35):
        print("Vert")
    elif(color > 45 and color < 55):
        print("Bleu ciel")
    elif(color > 75 and color < 90):
        print("Rouge")
    elif(color > 90 and color < 105):
        print("Violet")
    elif(color > 180 and color < 195):
        print("Jaune")
    
    

if (marty.is_conn_ready()): 
    # si Marty est connecté
    print("Connected to Marty!")
    while(marty.is_conn_ready()): # boucle si Marty connecté
        detectColor()
        # code a faire
        marty.close() # deconnection de Marty
        print("Disconnected from Marty.")
else: 
    # si Marty n'est pas connecté
    print("Failed to connect to Marty T-T.")