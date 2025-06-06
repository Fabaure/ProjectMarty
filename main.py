import msvcrt
import time
from martypy import Marty
from sensor import *
from movement import *
import re

def handle_key_events(marty, key):
    # verify if a key is pressed and do the according action
    if (key == b'e' or key == b'E'):
        getColor(marty)
        getDistance(marty)
        getBattery(marty)
        print("--------------")
        time.sleep(0.1)  # stop spam
    if (key == b'z' or key == b'Z'):
        move_forward(marty)
    elif (key == b's' or key == b'S'):
        move_backward(marty)
    elif (key == b'q' or key == b'Q'):
        move_left(marty)
    elif (key == b'd' or key == b'D'):
        move_right(marty)

def emotions(marty, feels_color, feels_mood, feels_colorhex):
    # function to verify what color marty is standing on and do the appropriate actions
    for i in range(len(feels_color)):
        if(feels_color[i] == getColor(marty)):
            marty.disco_color(feels_colorhex[i])
            marty.eyes(feels_mood[i],500)
            time.sleep(2)
            marty.disco_color(000000)


def main():
    adresse_ip = "192.168.0.101" # modify accordingly
    marty = Marty("wifi", adresse_ip) # connexion to Maty
    marty.set_marty_name("KAY/0")

    if (marty.is_conn_ready()): 
        # if Marty is connected
        print("Connected to Marty !")

        feels = open('../real.feels', 'r') # open .feels file
        contenu_feels = feels.read() # read the file
        tab_feels = re.split(r'[;\n]+', contenu_feels) # split the content
        feels.close() # close file

        x = 0
        feels_color = []
        feels_mood = []
        feels_colorhex = []
        for i in range(len(tab_feels)): # disassemble the original table
            if(x == 0):
                feels_color.append(tab_feels[i]) # table with the color of the tile
            elif(x == 1):
                feels_mood.append(tab_feels[i]) # table with the mood
            elif(x == 2):
                feels_colorhex.append(tab_feels[i]) # table with the color (in hexadecimal) of the eyes
            x = (x+1)%3

        dance = open('../cirle.dance', 'r')
        contenu_dance = dance.read()
        tab_dance = re.split(r'[ \n]+', contenu_dance)
        print(tab_dance)
        dance.close()

        running = True
        while(marty.is_conn_ready() and running): # loop if Maty is connected
            if(tab_dance[0] == "ABS"): # if in absolute mode
                print("absolute")
            elif(tab_dance[0] == "SEQ"): # if in sequential mode
                print("sequential")

            emotions(marty, feels_color, feels_mood, feels_colorhex)

            if (msvcrt.kbhit()):  # a key of the keyboard is pressed
                key = msvcrt.getch() # get the key that was pressed
                while msvcrt.kbhit():
                    msvcrt.getch()
                if (key == b'a' or key == b'A'):
                    # if the A key is pressed then stop the program
                    print("Touche A détectée, arrêt.")
                    running = False
                else:
                    handle_key_events(marty, key)
                    time.sleep(0.5)
            else:
                marty.stop('clear queue') # stops movement if no key is pressed
                time.sleep(0.5) # stop spamming of keys
    else: 
        # if Marty isn't connected
        print("Failed to connect to Marty T-T.")

    print("Disconnected from Marty.")
    marty.close() # deconnection of Marty

if __name__ == "__main__":
    main()



    # pour le clavier 
    '''running = True
        while(marty.is_conn_ready() and running): # loop if Maty is connected
            if (msvcrt.kbhit()):  # a key of the keyboard is pressed
                key = msvcrt.getch() # get the key that was pressed
                while msvcrt.kbhit():
                    msvcrt.getch()
                if (key == b'a' or key == b'A'):
                    # if the A key is pressed then stop the program
                    print("Touche A détectée, arrêt.")
                    running = False
                else:
                    handle_key_events(marty, key)
                    time.sleep(0.5)
            else:
                marty.stop('clear queue') # stops movement if no key is pressed
                time.sleep(0.5) # stop spamming of keys
        print("Disconnected from Marty.")
        marty.close() # deconnection of Marty'''
    
        # mouvement seul
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