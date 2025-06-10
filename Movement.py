from martypy import Marty
import time

adresse_ip = "192.168.0.100" 
marty = Marty("wifi", adresse_ip) 

def move_forward():
    if(marty.is_conn_ready): # Control that marty is well connected
        marty.walk(2,'auto',0,25,1500) #walk take in argmument number_of_steps , starting feet, turn degre , distance in mm , time of execution
    else:
        print("Marty is sadely not connected") # Print an error when not connected
        return 0
    return 0

def move_left():
    if(marty.is_conn_ready):
        marty.sidestep("left",1,35,1000,) #Take the side of step , the number of steps , degree of steps , time to execute
    else:
        print("Marty is sadely not connected")
        return 0
    
def move_right(): #Same than left but to the right
    if(marty.is_conn_ready):
        marty.sidestep("right",1,35,1000,)
    else:
        print("Marty is sadely not connected")
        return 0

def move_backward():
    if(marty.is_conn_ready):
        marty.walk(2,'auto',0,-25,1500) # Walk still work the same way , but negative distance make it walk backward 
    else:
        print("Marty is sadely not connected")
        return 0
    return 0
