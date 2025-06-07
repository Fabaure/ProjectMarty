from martypy import Marty
adresse_ip = "192.168.0.101" 
marty = Marty("wifi", adresse_ip, blocking= True)

def progress_callback(bytes_sent: int, total_bytes: int) -> bool:
    percent = (bytes_sent / total_bytes) * 100
    print(f"Progression: {percent:.2f}% ({bytes_sent}/{total_bytes} octets)")
    return True 

def rick_roll():
    marty.set_blocking(False)
    print(marty.is_blocking())
    if(marty.is_conn_ready):
        marty.set_volume(15)
        try:
            success = marty.send_file("rick(1).mp3", progress_callback, file_dest="fs")
            if success:
                print("Fichier envoyé avec succès ")
            else:
                print("Envoi du fichier interrompu ")
        except Exception as e:
            print(f"Erreur pendant l'envoi : {e}")
        marty.play_mp3("rick(1).mp3")
        for i in range (10):
            marty.sidestep("left",1,35,500,)
            marty.arms(45,-45,500)
            marty.sidestep("right",1,35,500,)
            marty.arms(-45,45,500)
    else:
        print("Marty is sadely not connected")
        return 0
    marty.set_blocking(True)
    return 0
    
rick_roll()
marty.close()