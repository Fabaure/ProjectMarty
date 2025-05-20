from martypy import Marty
import time
adresse_ip = "192.168.0.100" 
marty = Marty("wifi", adresse_ip) 


def angry():
    if(marty.is_conn_ready):
        marty.eyes("angry",500) # Eyes take ether a name of preprogramed expression and a time of execution or an angle of rotation and a time of execution
    else:
        print("Marty is sadely not connected") # Print an error when not connected
        return 0
    return 0

def wide_open():
    if(marty.is_conn_ready):
        marty.eyes("wide",500)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def excited():
    if(marty.is_conn_ready):
        marty.eyes("excited",500)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def wiggle():
    if(marty.is_conn_ready):
        marty.eyes("wiggle",1000)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def eyes_control(angle,time_in_ms):
    if(marty.is_conn_ready):
        marty.eyes(angle,time_in_ms)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def color_control(color,pattern,time_set):
    if(marty.is_conn_ready):
        marty.disco_pattern(int(pattern))
        marty.disco_color(color)
        time.sleep(int(time_set))
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

color = input("What color did you want? : ")
pattern = input("Which pattern did you prefer between 1 and 2 ? : ")
time_set = input("For how much time did you want it? : ")
color_control(color,pattern,time_set)