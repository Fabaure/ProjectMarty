import msvcrt
import time
from Movement import *
from sensor import *
from Expression import *


def handle_key_events(marty, key):
    # verify if a key is pressed and do the according action
    if (key == b'e' or key == b'E'):
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

def keyboard_loop(marty):
    while True:
        if msvcrt.kbhit(): # a key of the keyboard is pressed
            key = msvcrt.getch() # get the key that was pressed
            while msvcrt.kbhit():
                msvcrt.getch()
            if key in [b'a', b'A']:
                # if the A key is pressed then stop the program
                print("Touche A détectée, arrêt.")
                break
            else:
                handle_key_events(marty, key)
                if marty:
                    handle_key_events(marty, key)
                else:
                    print(f"Touche {key} détectée, mais Marty non connecté.")
        else:
            if marty:
                marty.stop('clear queue')  # stops movement if no key is pressed
        time.sleep(0.1)  # stop spamming of keys