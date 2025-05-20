import msvcrt
import time
import keyboard
from martypy import Marty
from sensor import *
from movement import *

def handle_key_events(marty):
    # verify if a key is pressed and do the according action
    if (keyboard.is_pressed("e") or keyboard.is_pressed("E")):
        getColor(marty)
        getDistance(marty)
        getBattery(marty)
        print("--------------")
        time.sleep(0.1)  # stop spam
    if (keyboard.is_pressed("z") or keyboard.is_pressed("Z")):
        move_forward(marty)
    elif (keyboard.is_pressed("s") or keyboard.is_pressed("S")):
        move_backward(marty)
    elif (keyboard.is_pressed("q") or keyboard.is_pressed("Q")):
        move_left(marty)
    elif (keyboard.is_pressed("d") or keyboard.is_pressed("D")):
        move_right(marty)
    else:
        marty.stop("clear and stop")  # stops movement if no key is pressed


def main():
    adresse_ip = "192.168.0.100" # modify accordingly
    marty = Marty("wifi", adresse_ip) # connexion to Maty
    marty.set_marty_name("KAY/0")

    if (marty.is_conn_ready()): 
        # if Marty is connected
        print("Connected to Marty !")
        running = True
        while(marty.is_conn_ready() and running): # loop if Maty is connected
            if (keyboard.is_pressed("a") or keyboard.is_pressed("A")):
                # if the A key is pressed then stop the program
                print("Touche A détectée, arrêt.")
                running = False
            else:
                handle_key_events(marty)
            time.sleep(0.1) # stop le spam
        print("Disconnected from Marty.")
        marty.close() # deconnection of Marty
    else: 
        # if Marty isn't connected
        print("Failed to connect to Marty T-T.")

if __name__ == "__main__":
    main()