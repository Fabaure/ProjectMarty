from martypy import Marty
import time
adresse_ip = "192.168.0.101" 
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

