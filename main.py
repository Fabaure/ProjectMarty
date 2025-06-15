from martypy import Marty
from dance_management import lectureFichierDance
import keyboard
from movement import *
from sensor import *

def main():
    adresse_ip = "192.168.0.108" # modify accordingly
    marty = Marty("wifi", adresse_ip) # connexion to Maty
    marty.set_marty_name("KAY/0")

    if (marty.is_conn_ready()): 
        # if Marty is connected
        print("Connected to Marty !")

        

        running = True
        while(marty.is_conn_ready() and running): # loop if Maty is connected
            lectureFichierDance(marty)

            ### emotions(marty, feels_color, feels_mood, feels_colorhex)

            keyboard(marty)

    else: 
        # if Marty isn't connected
        print("Failed to connect to Marty T-T.")

    print("Disconnected from Marty.")
    marty.close() # deconnection of Marty

if __name__ == "__main__":
    main()
    
        # autonomous mouvement
    '''getBattery(marty)
        if(getDistance(marty) == True):
             move_forward(marty)
        if(getDistance(marty) == False):
            print('obstacle')
            move_backward(marty)
            move_backward(marty)
            move_left(marty)
            move_left(marty)
            move_left(marty)'''