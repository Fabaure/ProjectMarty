from martypy import Marty

def progress_callback(bytes_sent: int, total_bytes: int) -> bool:
    percent = (bytes_sent / total_bytes) * 100                                #Calcul how much percent of the file is already sent
    print(f"Progression: {percent:.2f}% ({bytes_sent}/{total_bytes} octets)") #Print the value of last line
    return True 

def rick_roll(marty):
    marty.set_blocking(False) # Put blocking to false so marty can execute multiple things at the same time
    print(marty.is_blocking()) # Verification of the value "is_blocking()"
    if(marty.is_conn_ready):
        try:
            success = marty.send_file("rick(1).mp3", progress_callback, file_dest="fs") #Sent the file and print the progress
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
    marty.set_blocking(True)        #Set blocking to true so it doesn't affect other function
    return 0

def playChoosenSound(marty, choosenMusic):
    if(marty):
        marty.set_blocking(False)   # Put blocking to false so marty can execute multiple things at the same time
        print(marty.is_blocking())  # Verification of the value "is_blocking()"
        if(marty.is_conn_ready):
            try:
                success = marty.send_file(choosenMusic, progress_callback, file_dest="fs")  #Sent the ChoosenMusic file and print the progress
                if success:
                    print("Fichier envoyé avec succès ")
                else:
                    print("Envoi du fichier interrompu ")
            except Exception as e:
                print(f"Erreur pendant l'envoi : {e}")
            for i in range (10):             # Do the "Never gonna give you up" dance
                marty.sidestep("left",1,35,1000,)
                marty.arms(45,-45,500)
                marty.sidestep("right",1,35,1000,)
                marty.arms(-45,45,500)
            marty.set_volume(35)            # Set the volume to a define percent
            marty.play_mp3(choosenMusic)    # Play the file sent earlier (Actually not playing while dancing but after)
        else:
            print("Marty is sadely not connected")
            return 0
        marty.set_blocking(True)    #Set blocking to true so it doesn't affect other function
    return 0

def setVolumeFromInput(marty, choosenVolume): 
    if marty :
        if(marty.is_conn_ready):
            marty.set_volume(choosenVolume) #Set the volume to a define percent
            print("Nouveau volume")
        else :
            print("Marty is sadely not connected")
            return 0
        return 0

rick_roll()
Marty.close()