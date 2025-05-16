from martypy import Marty

def move_forward(marty):
    if(marty):
        print("Marty is well connected")
        marty.walk(2,'auto',0,25,1500)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def move_left(marty):
    if(marty):
        print("Marty is well connected")
        marty.sidestep("left",1,35,1000,)
    else:
        print("Marty is sadely not connected")
        return 0
    
def move_right(marty):
    if(marty):
        print("Marty is well connected")
        marty.sidestep("right",1,35,1000,)
    else:
        print("Marty is sadely not connected")
        return 0
    
def move_dance(marty):
    if(marty):
        print("Marty is well connected")
        marty.dance
    else:
        print("Marty is sadely not connected")
        return 0
