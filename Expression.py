from martypy import Marty
import time
addresse_ip = "192.168.0.101" 
marty = Marty("wifi", addresse_ip) 


def angry():
    if(marty.is_conn_ready):
        marty.eyes("angry",500) # Eyes take ether a name of preprogramed expression and a time of execution or an angle of rotation and a time of execution
    else:
        print("Marty is sadely not connected") # Print an error when not connected
        return 0
    return 0

def wide_open(): # Open marty's eyes.
    if(marty.is_conn_ready):
        marty.eyes("wide",500)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def excited(): # Create an excited expression on marty's face
    if(marty.is_conn_ready):
        marty.eyes("excited",500)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def wiggle(): # Make marty's eyes wiggle
    if(marty.is_conn_ready):
        marty.eyes("wiggle",1000)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def eyes_control(angle,time_in_ms): # Permit to controle angle and duration of marty's eyes movements
    if(marty.is_conn_ready):
        marty.eyes(angle,time_in_ms)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def color_control(color,pattern,time_set): # Permit to different color, pattern and duration for marty's eyes movements
    if(marty.is_conn_ready):
        marty.disco_pattern(int(pattern))
        marty.disco_color(color)
        time.sleep(int(time_set))
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def feel_control(color,emotion): # Function used in .feel reading to show good eyes color and expression
    if(marty.is_conn_ready):
        marty.disco_color(color)
        marty.eyes(emotion,500)
        time.sleep(2)
        marty.disco_color(000000)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

marty.close()