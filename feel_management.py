import re
import time
from sensor import getColor

def emotions(marty, feels_color, feels_mood, feels_colorhex):
    # function to verify what color marty is standing on and do the appropriate actions
    for i in range(len(feels_color)):
        if(feels_color[i] == getColor(marty)):
            marty.disco_color(feels_colorhex[i])
            marty.eyes(feels_mood[i],500)
            time.sleep(2)
            marty.disco_color(000000)

def lectureFichierFeel(marty):
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
    return feels_color, feels_mood, feels_colorhex