from martypy import Marty
adresse_ip = "192.168.0.108" 
marty = Marty("wifi", adresse_ip, blocking= True)

def progress_callback(bytes_sent: int, total_bytes: int) -> bool:
    percent = (bytes_sent / total_bytes) * 100                                #Calcul how much percent of the file is already sent
    print(f"Progression: {percent:.2f}% ({bytes_sent}/{total_bytes} octets)") #Print the value of last line
    return True 

def rick_roll():
    marty.set_blocking(False) # Put blocking to false so marty can execute multiple things at the same time
    print(marty.is_blocking()) # Verification of the value of "is_blocking()"
    if(marty.is_conn_ready):
        try:
            success = marty.send_file("rick(1).mp3", progress_callback, file_dest="fs") #Sent the file and print the progresse
            if success:
                print("Fichier envoyé avec succès ")
            else:
                print("Envoi du fichier interrompu ")
        except Exception as e:
            print(f"Erreur pendant l'envoi : {e}")
        for i in range (10):            # Do the "Never gonna give you up" dance
            marty.sidestep("left",1,35,1000,)
            marty.arms(45,-45,500)
            marty.sidestep("right",1,35,1000,)
            marty.arms(-45,45,500)
        marty.set_volume(35)            # Set the volume to a define percent
        marty.play_mp3("rick(1).mp3")   # Play the file sent earlier (Actually not playing while dancing but after)
    else:
        print("Marty is sadely not connected")
        return 0
    marty.set_blocking(True)
    return 0
    
rick_roll()
marty.close()