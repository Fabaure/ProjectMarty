def getColor(marty):
    color = marty.get_ground_sensor_reading("left") # lecture de la couleur
    print("Color : " + str(color))
    if(color < 20):
        print("Black")
    elif(color > 20 and color < 25):
        print("Blue")
    elif(color > 30 and color < 35):
        print("Green")
    elif(color > 45 and color < 55):
        print("Cyan")
    elif(color > 75 and color < 90):
        print("Red")
    elif(color > 90 and color < 105):
        print("Magenta")
    elif(color > 180 and color < 195):
        print("Yellow")

def getDistance(marty):
    distance = marty.get_obstacle_sensor_reading("right") # recupere la distance en millimetres
    print("Distance : " + str(distance))
    if(distance != 0):
        print("Obstacle : Yes")
    else:
        print("Obstacle : No")

def getBattery(marty):
    battery = marty.get_battery_remaining()
    print("Battery : " + str(battery) + "%")
    