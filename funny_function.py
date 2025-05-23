from martypy import Marty
adresse_ip = "192.168.0.100" 
marty = Marty("wifi", adresse_ip)

def rick_roll():
    if(marty.is_conn_ready):
        marty.play_mp3("Rick_rol")
        for i in range (10):
            marty.sidestep("left",1,35,1000,)
            marty.arms(90,-90,1000)
            marty.sidestep("right",1,35,1000,)
            marty.arms(-90,90,1000)
    else:
        print("Marty is sadely not connected")
        return 0