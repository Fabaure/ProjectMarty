def getColor(marty):
    # recupere la couleure sous marty
    color = marty.get_ground_sensor_reading("left") # lecture de la couleur
    print("Color : " + str(color))
    if(color < 19):
        print("Black")
    elif(color > 19 and color < 27):
        print("Blue")
    elif(color > 27 and color < 37):
        print("Green")
    elif(color > 45 and color < 57):
        print("Cyan")
    elif(color > 75 and color < 90):
        print("Red")
    elif(color > 90 and color < 110):
        print("Magenta")
    elif(color > 180 and color < 205):
        print("Yellow")

def getDistance(marty):
    # recupere la distance devant marty
    distance = marty.get_obstacle_sensor_reading("right") # recupere la distance en millimetres
    print("Distance : " + str(distance))
    if(distance != 0):
        print("Obstacle : Yes")
    else:
        print("Obstacle : No")

def getBattery(marty):
    # recupere le pourcentage de la batterie de marty
    battery = marty.get_battery_remaining()
    print("Battery : " + str(battery) + "%")
    