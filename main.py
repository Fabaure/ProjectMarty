from math import floor
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
        move_forward(marty, 2)
    elif (key == b's' or key == b'S'):
        move_backward(marty, 2)
    elif (key == b'q' or key == b'Q'):
        move_left(marty, 1)
    elif (key == b'd' or key == b'D'):
        move_right(marty, 1)

def emotions(marty, feels_color, feels_mood, feels_colorhex):
    # function to verify what color marty is standing on and do the appropriate actions
    for i in range(len(feels_color)):
        if(feels_color[i] == getColor(marty)):
            marty.disco_color(feels_colorhex[i])
            marty.eyes(feels_mood[i],500)
            time.sleep(2)
            marty.disco_color(000000)

def createMatrix(dimension):
    matrix = []
    mid = floor(dimension/2)
    for i in range(dimension): # creating the matrix
        row = []
        for j in range(dimension):
            row.append(0)
        matrix.append(row)  # adding rows to the matrix

    for i in range(dimension): # show the matrix in terminal
        for j in range(dimension):
            if(mid == i and mid == j):
                matrix[i][j] = 1
    return matrix

def afficherMatrix(matrix):
        for i in range(len(matrix)): # show the matrix in terminal
            for j in range(len(matrix)):
                print(matrix[i][j], end=" ")
            print()

def sequential(marty, dimension, dance_steps, dance_direction):
    matrix = createMatrix(dimension)
    afficherMatrix(matrix)

    
    for i in range(len(dance_direction)):
        steps = int(dance_steps[i]) * 2
        match dance_direction[i]:
            case "L":
                move_left(marty, steps)
            case "R":
                move_right(marty, steps)
            case "F":
                move_forward(marty, steps)
            case "B":
                move_backward(marty, steps)

def main():
    adresse_ip = "192.168.0.108" # modify accordingly
    marty = Marty("wifi", adresse_ip) # connexion to Maty
    marty.set_marty_name("KAY/0")

    if (marty.is_conn_ready()): 
        # if Marty is connected
        print("Connected to Marty !")

        feels = open('../real.feels', 'r') # open .feels file
        contenu_feels = feels.read() # read the file
        tab_feels = re.split(r'[;\n]+', contenu_feels) # split the content into a table
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

        dance = open('../test.dance', 'r')
        contenu_dance = dance.read()
        tab_dance = re.split(r'[ \n]+', contenu_dance)
        print(tab_dance)
        dance.close()

        if(tab_dance[0] == "SEQ"): # if in absolute mode
            x = 0
            dance_steps = []
            dance_direction = []
            for i in range(2, len(tab_dance)): # disassemble the original table
                if(x == 0):
                    dance_steps.append(tab_dance[i]) # table with the number of steps
                elif(x == 1):
                    dance_direction.append(tab_dance[i]) # table with the direction to take
                x = (x+1)%2

        running = True
        while(marty.is_conn_ready() and running): # loop if Maty is connected
            if(tab_dance[0] == "ABS"): # if in absolute mode
                print("absolute")
            elif(tab_dance[0] == "SEQ"): # if in sequential mode
                print("sequential")
                sequential(marty, int(tab_dance[1]), dance_steps, dance_direction)

            ### emotions(marty, feels_color, feels_mood, feels_colorhex)

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