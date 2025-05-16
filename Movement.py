from martypy import Marty

adresse_ip = "192.168.0.101" 
marty = Marty("wifi", adresse_ip) 

def move_forward():
    if(marty.is_conn_ready):
        print("Marty is well connected")
        marty.walk(2,'auto',0,25,1500)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def move_left():
    if(marty.is_conn_ready):
        print("Marty is well connected")
        marty.sidestep("left",1,35,1000,)
    else:
        print("Marty is sadely not connected")
        return 0
    
def move_right():
    if(marty.is_conn_ready):
        print("Marty is well connected")
        marty.sidestep("right",1,35,1000,)
    else:
        print("Marty is sadely not connected")
        return 0


move_forward()
for i in range(10):
    move_left() 
    move_right()